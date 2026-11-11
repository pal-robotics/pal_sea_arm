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

from dataclasses import dataclass
import os


from ament_index_python.packages import get_package_share_directory
from controller_manager.launch_utils import generate_load_controller_launch_description
from launch import LaunchContext, LaunchDescription
from launch.actions import DeclareLaunchArgument, SetLaunchConfiguration
from launch.actions import GroupAction, LogInfo, OpaqueFunction
from launch.conditions import LaunchConfigurationNotEquals
from launch.substitutions import LaunchConfiguration
from launch_pal.arg_utils import LaunchArgumentsBase, read_launch_argument
from launch_pal.param_utils import parse_parametric_yaml
from pal_sea_arm_description.launch_arguments import SEAArmArgs

DEPRECATION_WARNING = (
    '[DEPRECATED] ft_sensor_controller.launch.py is deprecated and will be '
    'removed in a future release. Please use ft_sensor_broadcaster.launch.py '
    'instead.')


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    ft_sensor: DeclareLaunchArgument = SEAArmArgs.ft_sensor
    side: DeclareLaunchArgument = DeclareLaunchArgument(
        name='side',
        default_value='',
        description='side of the ft sensor')
    location: DeclareLaunchArgument = DeclareLaunchArgument(
        name='location',
        default_value='wrist',
        choices=['wrist', 'ankle'],
        description='Set to "ankle" if configuring an ankle FT sensor instead of a wrist one')


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

    launch_description.add_action(OpaqueFunction(
        function=setup_controller_configuration,
        condition=LaunchConfigurationNotEquals('ft_sensor', 'no-ft-sensor')))

    launch_controller = GroupAction([generate_load_controller_launch_description(
        controller_name=LaunchConfiguration('controller_name'),
        controller_params_file=LaunchConfiguration('controller_config'))],
        condition=LaunchConfigurationNotEquals('ft_sensor', 'no-ft-sensor'))

    launch_description.add_action(launch_controller)

    return


def setup_controller_configuration(context: LaunchContext):

    side = read_launch_argument('side', context)
    ft_sensor = read_launch_argument('ft_sensor', context)
    location = read_launch_argument('location', context)

    ft_prefix = 'ankle_ft' if location == 'ankle' else 'ft_sensor'
    link_prefix = 'ankle' if location == 'ankle' else 'wrist'

    if side:
        ft_prefix += f'_{side}'
        link_prefix += f'_{side}'

    controller_name = f'{ft_prefix}_controller'
    remappings = {'FT_SIDE_PREFIX': ft_prefix,
                  'LINK_SIDE_PREFIX': link_prefix}

    param_file = os.path.join(
        get_package_share_directory('pal_sea_arm_controller_configuration'),
        'config', f'{ft_sensor}_controller.yaml')

    parsed_yaml = parse_parametric_yaml(source_files=[param_file], param_rewrites=remappings)

    return [SetLaunchConfiguration('controller_name', controller_name),
            SetLaunchConfiguration('controller_config', parsed_yaml)]


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    ld.add_action(LogInfo(msg=DEPRECATION_WARNING))

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
