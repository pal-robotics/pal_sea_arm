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
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration
from launch.actions import DeclareLaunchArgument, SetLaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch_pal.include_utils import include_scoped_launch_py_description
from launch_pal.arg_utils import LaunchArgumentsBase
from launch_pal.robot_arguments import TiagoSEAArgs

from dataclasses import dataclass


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    end_effector: DeclareLaunchArgument = TiagoSEAArgs.end_effector
    ft_sensor: DeclareLaunchArgument = TiagoSEAArgs.ft_sensor

    # For future changes in the wrist
    wrist_model: DeclareLaunchArgument = TiagoSEAArgs.wrist_model

    arm_model: DeclareLaunchArgument = DeclareLaunchArgument(
        'arm_model', default_value='pal-sea-arm-standalone',
        choices=['pal-sea-arm-standalone', 'tiago-pro', 'tiago-sea', 'tiago-sea-dual'],
        description='The arm model')


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

    set_sim_time = SetLaunchConfiguration('use_sim_time', 'True')
    launch_description.add_action(set_sim_time)

    robot_state_publisher = include_scoped_launch_py_description(
        pkg_name='pal_sea_arm_description',
        paths=['launch', 'robot_state_publisher.launch.py'],
        launch_arguments={"end_effector": launch_args.end_effector,
                          "ft_sensor": launch_args.ft_sensor,
                          "wrist_model": launch_args.wrist_model,
                          "arm_model": launch_args.arm_model,
                          "use_sim_time": LaunchConfiguration('use_sim_time')
                          })

    launch_description.add_action(robot_state_publisher)

    joint_state_pub_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen')

    launch_description.add_action(joint_state_pub_gui)

    rviz_config_file = PathJoinSubstitution(
        [FindPackageShare('pal_sea_arm_description'), 'config', 'show.rviz'])

    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_file],
        output='screen',
        parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time')}])

    launch_description.add_action(rviz)

    return


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
