# Copyright (c) 2026 PAL Robotics S.L. All rights reserved.
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
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from launch_pal.arg_utils import LaunchArgumentsBase
from launch_pal.include_utils import include_scoped_launch_py_description
from launch_pal.robot_arguments import CommonArgs


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    use_sim_time: DeclareLaunchArgument = CommonArgs.use_sim_time


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

    pkg_share_dir = get_package_share_directory('pal_sea_arm_bringup')

    motions_folder = os.path.join(
        pkg_share_dir, 'config', 'motions')

    planner_motions_folder = os.path.join(
        pkg_share_dir, 'config', 'motion_planner')

    play_motion2 = include_scoped_launch_py_description(
        pkg_name='play_motion2',
        paths=['launch', 'play_motion2.launch.py'],
        launch_arguments={
            'use_sim_time': LaunchConfiguration('use_sim_time'),
            'motions_file': os.path.join(motions_folder, 'arm_standalone_motions.yaml'),
            'motion_planner_config': os.path.join(planner_motions_folder, 'motion_planner.yaml')
        })

    launch_description.add_action(play_motion2)
    return


def generate_launch_description():
    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
