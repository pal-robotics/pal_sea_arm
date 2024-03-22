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

from dataclasses import dataclass

from ament_index_python.packages import get_package_share_directory
from controller_manager.launch_utils import generate_load_controller_launch_description
from launch_pal.param_utils import parse_parametric_yaml
from launch_pal.arg_utils import LaunchArgumentsBase, read_launch_argument
from launch.actions import DeclareLaunchArgument, SetLaunchConfiguration
from launch.actions import OpaqueFunction, GroupAction
from launch.conditions import LaunchConfigurationNotEquals
from launch.substitutions import LaunchConfiguration
from launch import LaunchDescription, LaunchContext
from launch_pal.robot_arguments import TiagoSEAArgs


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    ft_sensor: DeclareLaunchArgument = TiagoSEAArgs.ft_sensor
    side: DeclareLaunchArgument = DeclareLaunchArgument(
        name='side',
        default_value='',
        choices=['', 'left', 'right'],
        description='side of the ft sensor')


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

    launch_description.add_action(OpaqueFunction(
        function=setup_controller_configuration,
        condition=LaunchConfigurationNotEquals('ft_sensor', 'no-ft-sensor')))

    launch_controller = GroupAction([generate_load_controller_launch_description(
        controller_name=LaunchConfiguration("controller_name"),
        controller_type='force_torque_sensor_broadcaster/ForceTorqueSensorBroadcaster',
        controller_params_file=LaunchConfiguration("controller_config"))],
        condition=LaunchConfigurationNotEquals('ft_sensor', 'no-ft-sensor'))

    launch_description.add_action(launch_controller)

    return


def setup_controller_configuration(context: LaunchContext):

    side = read_launch_argument('side', context)
    ft_sensor = read_launch_argument('ft_sensor', context)

    ft_prefix = "ft_sensor"
    wrist_prefix = "wrist"
    if side:
        ft_prefix = f"ft_sensor_{side}"
        wrist_prefix = f"wrist_{side}"

    controller_name = f"{ft_prefix}_controller"
    remappings = {"FT_SIDE_PREFIX": ft_prefix,
                  "WRIST_SIDE_PREFIX": wrist_prefix}

    param_file = os.path.join(
        get_package_share_directory('pal_sea_arm_controller_configuration'),
        'config', f'{ft_sensor}_controller.yaml')

    parsed_yaml = parse_parametric_yaml(source_files=[param_file], param_rewrites=remappings)

    return [SetLaunchConfiguration('controller_name', controller_name),
            SetLaunchConfiguration('controller_config', parsed_yaml)]


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
