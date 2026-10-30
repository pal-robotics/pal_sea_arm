# Copyright (c) 2024 PAL Robotics S.L. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import GroupAction, OpaqueFunction
from launch.conditions import LaunchConfigurationNotEquals, IfCondition, UnlessCondition
from launch.actions import DeclareLaunchArgument
from controller_manager.launch_utils import generate_load_controller_launch_description
from launch.substitutions import LaunchConfiguration
from launch_pal.include_utils import include_scoped_launch_py_description
from launch_pal.arg_utils import LaunchArgumentsBase, read_launch_argument
from launch_pal.robot_arguments import CommonArgs
from pal_sea_arm_description.launch_arguments import SEAArmArgs

from dataclasses import dataclass


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    end_effector: DeclareLaunchArgument = SEAArmArgs.end_effector
    ft_sensor: DeclareLaunchArgument = SEAArmArgs.ft_sensor
    torque_estimation: DeclareLaunchArgument = SEAArmArgs.torque_estimation
    use_sim_time: DeclareLaunchArgument = CommonArgs.use_sim_time
    is_public_sim: DeclareLaunchArgument = CommonArgs.is_public_sim
    namespace: DeclareLaunchArgument = CommonArgs.namespace
    wrist_model: DeclareLaunchArgument = SEAArmArgs.wrist_model


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):
    pkg_name = 'pal_sea_arm_controller_configuration'
    pkg_share_folder = get_package_share_directory(
        pkg_name)

    joint_state_broadcaster = GroupAction(
        [generate_load_controller_launch_description(
            controller_name='joint_state_broadcaster',
            controller_params_file=os.path.join(
                pkg_share_folder,
                'config', 'joint_state_broadcaster.yaml'))
         ],
        forwarding=False)
    launch_description.add_action(joint_state_broadcaster)

    joint_torque_state_broadcaster = GroupAction(
        [generate_load_controller_launch_description(
            controller_name='joint_torque_state_broadcaster',
            controller_params_file=os.path.join(
                pkg_share_folder,
                'config', 'joint_torque_state_broadcaster.yaml'))
         ],
        forwarding=False,
        condition=IfCondition(LaunchConfiguration("torque_estimation"))
    )
    launch_description.add_action(joint_torque_state_broadcaster)

    sea_state_broadcaster = include_scoped_launch_py_description(
        pkg_name='pal_sea_arm_controller_configuration',
        paths=['launch', 'sea_state_broadcaster_controller.launch.py'],
        launch_arguments={'side': ''},
        condition=IfCondition(LaunchConfiguration("torque_estimation"))
    )

    launch_description.add_action(sea_state_broadcaster)

    arm_controller = include_scoped_launch_py_description(
        pkg_name=pkg_name,
        paths=['launch', 'arm_controller.launch.py'])

    launch_description.add_action(arm_controller)

    gravity_compensation_controller_effort = include_scoped_launch_py_description(
        pkg_name='pal_sea_arm_controller_configuration',
        paths=['launch', 'gravity_compensation_controller.launch.py'],
        launch_arguments={"side": '',
                          "root_link": 'arm_root_link',
                          "wrist_model": LaunchConfiguration('wrist_model')
                          },
        condition=UnlessCondition(LaunchConfiguration("is_public_sim"))
    )

    launch_description.add_action(gravity_compensation_controller_effort)

    input_state_broadcaster = include_scoped_launch_py_description(
        pkg_name='input_state_broadcaster',
        paths=['launch', 'input_state_broadcaster.launch.py'],
        launch_arguments={"side": '',
                          "prefix": ''},
        condition=UnlessCondition(LaunchConfiguration("is_public_sim"))
    )

    launch_description.add_action(input_state_broadcaster)

    ft_sensor_controller = include_scoped_launch_py_description(
        pkg_name=pkg_name,
        paths=['launch', 'ft_sensor_controller.launch.py'],
        launch_arguments={"ft_sensor": LaunchConfiguration('ft_sensor')},
        condition=LaunchConfigurationNotEquals('ft_sensor', 'no-ft-sensor'))

    launch_description.add_action(ft_sensor_controller)

    launch_description.add_action(OpaqueFunction(
        function=configure_end_effector_controller))

    return


def configure_end_effector_controller(context, *args, **kwargs):
    # Load end_effector controller
    end_effector = read_launch_argument('end_effector', context)
    end_effector_underscore = end_effector.replace('-', '_')

    if end_effector not in ["no-end-effector", "pen-gripper"]:
        ee_pkg_name = f'{end_effector_underscore}_controller_configuration'
        ee_launch_file = f'{end_effector_underscore}_controller.launch.py'

        end_effector_controller = include_scoped_launch_py_description(
            pkg_name=ee_pkg_name,
            paths=['launch', ee_launch_file],
        )
        return [end_effector_controller]
    else:
        pass


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
