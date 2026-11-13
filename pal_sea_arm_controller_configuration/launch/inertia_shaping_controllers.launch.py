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
from ament_index_python.packages import get_package_share_path
from ament_index_python.resources import get_resource, get_resources
from controller_manager.launch_utils import (
    generate_controllers_spawner_launch_description_from_dict
)
from launch import LaunchContext, LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import OpaqueFunction

from launch_pal.arg_utils import LaunchArgumentsBase, read_launch_argument
from launch_pal.calibration_utils import apply_master_calibration
from launch_pal.param_utils import parse_parametric_yaml
from launch_pal.robot_arguments import CommonArgs
import yaml


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    side: DeclareLaunchArgument = CommonArgs.side


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

    # Launches (inactive) 7 IS controllers
    launch_description.add_action(OpaqueFunction(
        function=setup_inertia_shaping_controllers))

    return


def setup_inertia_shaping_controllers(context: LaunchContext):

    side = read_launch_argument('side', context)

    arm_prefix = 'arm'
    if side:
        arm_prefix = f'arm_{side}'

    params_path = os.path.join(
        get_package_share_directory('pal_sea_arm_controller_configuration'),
        'config', 'inertia_shaping_controller'
    )

    inertia_shaping_controllers_dict = {}
    for i in range(1, 8):

        controller_name = f'{arm_prefix}_{i}_joint_inertia_shaping_controller'

        # Get the config file based on the actuator type
        actuator_positon = f'{arm_prefix}_{i}'
        actuator_type = get_actuator_type(actuator_positon)

        if not actuator_type:
            raise RuntimeError(f'Failed to determine actuator type for {actuator_positon}. '
                               f'Please ensure sea_data resources exist.')

        param_file = os.path.join(
            params_path, f'{actuator_type}_params.yaml'
        )

        # Calibrate and remap
        remappings = {'ARM_SIDE_PREFIX': arm_prefix,
                      'JOINT_POSITION': i,
                      'ACTUATOR_TYPE': actuator_type,
                      'PARAMS_PATH': params_path}

        parsed_yaml = parse_parametric_yaml(
            source_files=[param_file], param_rewrites=remappings)

        calibrated_yaml = apply_master_calibration(parsed_yaml)

        inertia_shaping_controllers_dict.update(
            {controller_name: calibrated_yaml}
        )

    inertia_shaping_controllers = generate_controllers_spawner_launch_description_from_dict(
        inertia_shaping_controllers_dict,
        extra_spawner_args=['--inactive'],
    )

    return [inertia_shaping_controllers]


def get_actuator_type(actuator_position: str) -> str:

    resource_type = 'sea_data'
    resources = get_resources(resource_type)
    if not resources:
        return ''

    # Take the first resource only
    pkg = next(iter(resources.keys()))
    pkg_share_path = get_package_share_path(pkg)
    sea_data_path = pkg_share_path / get_resource(resource_type, pkg)[0]
    actuator_sea_data_path = sea_data_path / f'{actuator_position}_actuator'
    actuator_metadata_path = actuator_sea_data_path / 'actuator_metadata.yaml'

    if not actuator_metadata_path.exists():
        return ''

    try:
        with open(actuator_metadata_path, 'r') as file:
            metadata = yaml.safe_load(file)
            # Extract the actuator type from the metadata
            if metadata and 'actuator_type' in metadata:
                return metadata['actuator_type']
    except (yaml.YAMLError, IOError) as e:
        print(f'Error reading actuator metadata: {e}')

    return ''


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
