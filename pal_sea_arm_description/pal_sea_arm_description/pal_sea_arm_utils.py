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

def get_pal_sea_arm_hw_suffix(
        end_effector=None,
        ft_sensor=None):
    """

    Generate a substitution that creates a text suffix combining the specified pal_sea_arm args.

    The arguments are read as string.

    For instance, the suffix for: end_effector='pal-gripper', ft_sensor='robuki'
    would be 'pal-gripper_schunk-ft'.
    """
    suffix = '_'
    if end_effector is not None:
        suffix += end_effector
        suffix += '_'
    if ft_sensor is not None and ft_sensor != 'no-ft-sensor':
        suffix += ft_sensor
        suffix += '_'
    suffix = suffix[:-1]  # remove last _
    return suffix
