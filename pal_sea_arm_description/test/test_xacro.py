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
from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument
from pal_sea_arm_description.launch_arguments import SEAArmArgs

from urdf_test.xacro_test import define_xacro_test

xacro_file_path = Path(
    get_package_share_directory('pal_sea_arm_description'),
    'robots',
    'pal_sea_arm.urdf.xacro',
)

arm_args = (
    SEAArmArgs.tool_changer,
    SEAArmArgs.ft_sensor
)

arm_standalone = DeclareLaunchArgument(
    name='pal-sea-arm-standalone',
    choices=['pal-sea-arm-standalone'])

tiago_pro = DeclareLaunchArgument(
    name='tiago-pro',
    choices=['tiago-pro'])

tiago_sea_dual = DeclareLaunchArgument(
    name='tiago-sea-dual',
    choices=['tiago-sea-dual'])

tiago_sea = DeclareLaunchArgument(
    name='tiago-sea',
    choices=['tiago-sea'])

straigh_wrist = DeclareLaunchArgument(
    name='straigh-wrist',
    choices=['straigh-wrist'])

end_effector = SEAArmArgs.end_effector
if not os.environ.get('PAL_DISTRO'):
    _orig = SEAArmArgs.end_effector
    _choices = getattr(_orig, 'choices', None)
    _name = getattr(_orig, 'name', None)
    filtered_choices = [c for c in _choices if 'allegro-hand' not in str(c)]
    end_effector = DeclareLaunchArgument(name=_name, choices=filtered_choices)

test_xacro_laser = define_xacro_test(
    xacro_file_path, arm_standalone, SEAArmArgs.wrist_model)
test_xacro_laser = define_xacro_test(
    xacro_file_path, tiago_pro, SEAArmArgs.wrist_model)
test_xacro_laser = define_xacro_test(
    xacro_file_path, tiago_sea_dual, straigh_wrist)
test_xacro_laser = define_xacro_test(
    xacro_file_path, tiago_sea, straigh_wrist)
test_xacro_laser = define_xacro_test(
    xacro_file_path, arm_args, SEAArmArgs.wrist_model, end_effector)
