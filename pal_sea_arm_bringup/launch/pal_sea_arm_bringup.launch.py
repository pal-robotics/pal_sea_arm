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


from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument

from launch_pal.include_utils import include_scoped_launch_py_description
from launch_pal.arg_utils import LaunchArgumentsBase
from launch_pal.robot_arguments import CommonArgs
from pal_sea_arm_description.launch_arguments import SEAArmArgs

from dataclasses import dataclass


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    end_effector: DeclareLaunchArgument = SEAArmArgs.end_effector
    ft_sensor: DeclareLaunchArgument = SEAArmArgs.ft_sensor
    torque_estimation: DeclareLaunchArgument = SEAArmArgs.torque_estimation
    wrist_model: DeclareLaunchArgument = SEAArmArgs.wrist_model
    use_sim_time: DeclareLaunchArgument = CommonArgs.use_sim_time
    is_public_sim: DeclareLaunchArgument = CommonArgs.is_public_sim
    namespace: DeclareLaunchArgument = CommonArgs.namespace

    arm_type: DeclareLaunchArgument = DeclareLaunchArgument(
        'arm_type', default_value='pal-sea-arm-standalone',
        choices=['pal-sea-arm-standalone', 'tiago-pro',
                 'tiago-sea', 'tiago-sea-dual'],
        description='The arm model')

    sim_type: DeclareLaunchArgument = CommonArgs.sim_type
    mj_control: DeclareLaunchArgument = CommonArgs.mj_control
    world_name: DeclareLaunchArgument = CommonArgs.world_name
    gazebo_version: DeclareLaunchArgument = CommonArgs.gazebo_version


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

    default_controllers = include_scoped_launch_py_description(
        pkg_name='pal_sea_arm_controller_configuration',
        paths=['launch', 'default_controllers.launch.py'],
        launch_arguments={"end_effector": launch_args.end_effector,
                          "ft_sensor": launch_args.ft_sensor,
                          "torque_estimation": launch_args.torque_estimation,
                          "namespace": launch_args.namespace,
                          "use_sim_time": launch_args.use_sim_time,
                          "is_public_sim": launch_args.is_public_sim
                          })

    launch_description.add_action(default_controllers)

    play_motion2 = include_scoped_launch_py_description(
        pkg_name='pal_sea_arm_bringup',
        paths=['launch', 'arm_standalone_play_motion2.launch.py'],
        launch_arguments={"use_sim_time": launch_args.use_sim_time})

    launch_description.add_action(play_motion2)

    robot_state_publisher = include_scoped_launch_py_description(
        pkg_name='pal_sea_arm_description',
        paths=['launch', 'robot_state_publisher.launch.py'],
        launch_arguments={"end_effector": launch_args.end_effector,
                          "ft_sensor": launch_args.ft_sensor,
                          "arm_type": launch_args.arm_type,
                          "wrist_model": launch_args.wrist_model,
                          "torque_estimation": launch_args.torque_estimation,
                          "namespace": launch_args.namespace,
                          "use_sim_time": launch_args.use_sim_time,
                          "sim_type": launch_args.sim_type,
                          "mj_control": launch_args.mj_control,
                          "world_name": launch_args.world_name,
                          "gazebo_version": launch_args.gazebo_version,
                          })

    launch_description.add_action(robot_state_publisher)

    return


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
