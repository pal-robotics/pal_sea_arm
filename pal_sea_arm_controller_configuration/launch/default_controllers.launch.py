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
from launch.conditions import LaunchConfigurationNotEquals
from launch.actions import DeclareLaunchArgument
from controller_manager.launch_utils import generate_load_controller_launch_description

from launch_pal.include_utils import include_scoped_launch_py_description
from launch_pal.arg_utils import LaunchArgumentsBase, CommonArgs, read_launch_argument
from launch_pal.robot_arguments import TiagoSEAArgs

from dataclasses import dataclass


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    end_effector: DeclareLaunchArgument = TiagoSEAArgs.end_effector
    ft_sensor: DeclareLaunchArgument = TiagoSEAArgs.ft_sensor
    use_sim_time: DeclareLaunchArgument = CommonArgs.use_sim_time
    namespace: DeclareLaunchArgument = CommonArgs.namespace


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):
    pkg_name = 'pal_sea_arm_controller_configuration'
    pkg_share_folder = get_package_share_directory(
        pkg_name)

    joint_state_broadcaster = GroupAction(
        [generate_load_controller_launch_description(
            controller_name='joint_state_broadcaster',
            controller_type='joint_state_broadcaster/JointStateBroadcaster',
            controller_params_file=os.path.join(
                pkg_share_folder,
                'config', 'joint_state_broadcaster.yaml'))
         ],
        forwarding=False)
    launch_description.add_action(joint_state_broadcaster)

    arm_controller = include_scoped_launch_py_description(
        pkg_name=pkg_name,
        paths=['launch', 'arm_controller.launch.py'])

    launch_description.add_action(arm_controller)

    ft_sensor_controller = include_scoped_launch_py_description(
        pkg_name=pkg_name,
        paths=['launch', 'ft_sensor_controller.launch.py'],
        condition=LaunchConfigurationNotEquals('ft_sensor', 'no-ft-sensor'))

    launch_description.add_action(ft_sensor_controller)

    launch_description.add_action(OpaqueFunction(function=configure_end_effector_controller))

    return


def configure_end_effector_controller(context, *args, **kwargs):

    # Load end_effector controller
    end_effector = read_launch_argument('end_effector', context)
    end_effector_underscore = end_effector.replace('-', '_')

    ee_pkg_name = f'{end_effector_underscore}_controller_configuration'
    ee_launch_file = f'{end_effector_underscore}_controller.launch.py'

    end_effector_controller = include_scoped_launch_py_description(
        pkg_name=ee_pkg_name,
        paths=['launch', ee_launch_file])

    return [end_effector_controller]


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
