^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package pal_sea_arm_controller_configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.0.3 (2024-03-22)
------------------
* Merge branch 'dtk/fix/restructure' into 'humble-devel'
  Dtk/fix/restructure
  See merge request robots/pal_sea_arm!23
* Update copyright year
* Remove unused imports for flake test
* Refactor arm_controller
* Remove unused default_safety_parameters
* Create force-torque sensor related launch file
* Restructure launch files
* Contributors: David ter Kuile, Noel Jimenez, davidterkuile

2.8.4 (2026-08-04)
------------------

2.8.3 (2026-07-30)
------------------

2.8.2 (2026-07-20)
------------------
* Add prefix argument and change value for no side
* Add no controller when ee is pen-gripper
* Contributors: Aina

2.8.1 (2026-07-06)
------------------
* Merge branch 'change/publish_rate/ft_broadcaster' into 'humble-devel'
  Set the publish rate of the force-torque broadcasters to 100 Hz
  See merge request robots/pal_sea_arm!141
* Set the publish rate of the force-torque broadcasters to 100 Hz
* Contributors: Sai Kishor Kothakota

2.8.0 (2026-07-03)
------------------
* Merge branch 'use/ft_broadcaster' into 'humble-devel'
  Use ft broadcaster instead of ft_controller
  See merge request robots/pal_sea_arm!140
* Deprecate ft_sensor_controller launch configuration
* Add FT Sensor Broadcaster configuration
* Contributors: Sai Kishor Kothakota

2.7.0 (2026-07-02)
------------------
* Merge branch 'feat/add_input_broadcaster' into 'humble-devel'
  Add input broadcaster by default
  See merge request robots/pal_sea_arm!138
* Add alum condition for dependency
* Fix side
* Add input broadcaster by default
* Contributors: Aina, Aina Irisarri

2.6.0 (2026-06-25)
------------------

2.5.1 (2026-06-17)
------------------

2.5.0 (2026-06-04)
------------------
* Change is_ankle to location to better scalability
* Add dynamic prefix to handle ankle ft
* Contributors: Aina

2.4.1 (2026-05-29)
------------------

2.4.0 (2026-05-20)
------------------

2.3.1 (2026-05-12)
------------------

2.3.0 (2026-05-12)
------------------

2.2.1 (2026-04-29)
------------------
* add launch_argument ft_sensor
* fix errors
* Contributors: susannamastromauro

2.2.0 (2026-04-28)
------------------

2.1.1 (2026-04-16)
------------------

2.1.0 (2026-04-15)
------------------

2.0.1 (2026-04-10)
------------------
* Fixing open loop param
* adding depend gravity_compensation_controller2
* adding check side for standalone
* adding gravity_compensation_controller_effort
* Contributors: susannamastromauro, vivianamorlando

2.0.0 (2026-03-31)
------------------
* add torque_estimation condition
* fix simulation and 7-link-mesh
* Contributors: susannamastromauro

1.25.0 (2026-03-18)
-------------------
* Raise on incompatibility of short-wrist and torque mode
* Add support for short-wrist
* Contributors: Noel Jimenez

1.24.0 (2026-02-18)
-------------------

1.23.2 (2026-02-10)
-------------------

1.23.1 (2026-02-03)
-------------------

1.23.0 (2026-02-02)
-------------------
* fix pipeline
* add root_link instead of torso_lift_link to adapt teleop station
* Contributors: ileniaperrella

1.22.1 (2026-01-08)
-------------------
* Add "Hardware Components Activity" module dependency
* Contributors: Noel Jimenez

1.22.0 (2025-12-05)
-------------------

1.21.0 (2025-10-29)
-------------------
* Merge branch 'tpe/add_open_loop' into 'humble-devel'
  Add back openloop to controller
  See merge request robots/pal_sea_arm!99
* Add back openloop to controller
* Contributors: thomas.peyrucain, thomaspeyrucain

1.20.2 (2025-10-29)
-------------------

1.20.1 (2025-10-27)
-------------------

1.20.0 (2025-10-23)
-------------------

1.19.1 (2025-10-13)
-------------------
* Merge branch 'fix/condition_private_packages' into 'humble-devel'
  Add PAL_DISTRO condition for non-public packages
  See merge request robots/pal_sea_arm!94
* Add PAL_DISTRO condition for non-public packages
* Merge branch 'fix/tolerance_fix' into 'humble-devel'
  tmp fix removing tolerance
  See merge request robots/pal_sea_arm!81
* Remove tolerance
* Contributors: Aina, Noel Jimenez, ileniaperrella

1.19.0 (2025-09-08)
-------------------
* Fixed arm controller configuration file
* restored to original version
* Fixed arm_prefix in sea_state_broadcaster
* changed mujoco simulation update_rate argument
* Added mujoco_controller_manager config file
* Added mujoco tags
* Contributors: Ortisa Poci

1.18.7 (2025-08-01)
-------------------

1.18.6 (2025-07-29)
-------------------
* Increasing sea_state_broadcaster frequency
* Contributors: oscarmartinez

1.18.5 (2025-07-28)
-------------------
* Remove trajectory constraint
* Contributors: Aina Irisarri

1.18.4 (2025-07-28)
-------------------

1.18.3 (2025-07-23)
-------------------
* Merge branch 'ipe/fix/open-loop' into 'humble-devel'
  add open_loop to arm controller
  See merge request robots/pal_sea_arm!84
* add open_loop to arm controller
* Contributors: Sai Kishor Kothakota, ileniaperrella

1.18.2 (2025-06-17)
-------------------

1.18.1 (2025-06-06)
-------------------

1.18.0 (2025-05-29)
-------------------
* Default controller launch and missing dep
* Adding sea_state_broadcaster as a side controller
* Contributors: oscarmartinez

1.17.5 (2025-05-28)
-------------------
* increase trajectory tolerance to ~10deg
* update arm_controller with trajectory constraint
* Contributors: ileniaperrella

1.17.4 (2025-04-29)
-------------------
* Fixing the parsing order for master calibration
* Contributors: oscarmartinez

1.17.3 (2025-04-28)
-------------------

1.17.2 (2025-04-17)
-------------------

1.17.1 (2025-04-11)
-------------------
* Renaming current of effort and proper launch mechanism
* Contributors: oscarmartinez

1.17.0 (2025-04-10)
-------------------
* Adding config and launching mechanism for GC in torque
* Add intertia shaping dependency
* Config files based on actuator type
* Added launcher and config files for IS
* Contributors: davidterkuile, oscarmartinez

1.16.0 (2025-04-09)
-------------------
* Using parameter from Common Args
* Adapting to new gravity behaviour
* Contributors: oscarmartinez

1.15.3 (2025-04-09)
-------------------

1.15.2 (2025-04-03)
-------------------
* Create gravity compensation controller
* Update launch args of arm_controller.launch.py
* Contributors: David ter Kuile

1.15.1 (2025-03-31)
-------------------
* Remove choices for ft-sensor side for triago compatibility
* Contributors: David ter Kuile

1.15.0 (2025-03-27)
-------------------
* Support in pal_sea_arm_bringup
* Support in pal_sea_arm_controller_configuration
* SEA transmission optional loading
* added joint torque state broadcaster
* Contributors: Daniel Costanzi, oscarmartinez

1.14.5 (2025-02-28)
-------------------

1.14.4 (2025-02-19)
-------------------
* Merge branch 'tpe/fix_ft_sensor' into 'humble-devel'
  Fix ATI sensor in gazebo simulation
  See merge request robots/pal_sea_arm!62
* Fix ATI sensor in gazebo simulation
* Contributors: thomas.peyrucain, thomaspeyrucain

1.14.3 (2025-02-05)
-------------------
* Use ft_sensor suffix for force-torque sensor name
* Contributors: Noel Jimenez

1.14.2 (2025-01-23)
-------------------

1.14.1 (2025-01-21)
-------------------

1.14.0 (2025-01-16)
-------------------

1.13.0 (2024-11-07)
-------------------
* Set update_rate for joint_state_broadcaster
* Contributors: Noel Jimenez

1.12.0 (2024-10-29)
-------------------

1.11.6 (2024-10-21)
-------------------

1.11.5 (2024-10-09)
-------------------

1.11.4 (2024-10-08)
-------------------

1.11.3 (2024-10-02)
-------------------

1.11.2 (2024-09-30)
-------------------
* Merge branch 'vmo/ati_controller' into 'humble-devel'
  Adding ati controller
  See merge request robots/pal_sea_arm!43
* Adding ati controller
* Contributors: thomaspeyrucain, vivianamorlando

1.11.1 (2024-09-27)
-------------------

1.11.0 (2024-09-19)
-------------------

1.10.1 (2024-09-09)
-------------------

1.10.0 (2024-08-06)
-------------------
* Use controller_type from the controllers config
* Contributors: Noel Jimenez

1.0.9 (2024-07-11)
------------------

1.0.8 (2024-07-09)
------------------
* Add warning for pal_module_cmake not found
* add modules for description and controller*
* Contributors: Aina, Noel Jimenez

1.0.7 (2024-06-26)
------------------
* Merge branch 'dtk/move-robot-args' into 'humble-devel'
  Change import for launch args
  See merge request robots/pal_sea_arm!30
* Create standalone robot args for sea arms
* Contributors: David ter Kuile, davidterkuile

1.0.6 (2024-05-22)
------------------
* Merge branch 'feat/auto-generated_srdf_files' into 'humble-devel'
  add no-end-effector condition in controllers
  See merge request robots/pal_sea_arm!26
* linters
* add no-end-effector condition in controllers
* Contributors: Aina Irisarri, davidterkuile

1.0.5 (2024-05-09)
------------------

1.0.4 (2024-04-26)
------------------
* 1.0.3
* Update Changelog
* Update copyright year
* Remove unused imports for flake test
* Refactor arm_controller
* Remove unused default_safety_parameters
* Create force-torque sensor related launch file
* Restructure launch files
* Contributors: David ter Kuile, Noel Jimenez

1.0.2 (2024-03-07)
------------------

1.0.1 (2024-01-29)
------------------

1.0.0 (2024-01-29)
------------------
* Merge branch 'ros2-migration' into 'humble-devel'
  Ros2 migration
  See merge request robots/pal_sea_arm!17
* remove unused type param from controller config files
* update to 3.8 the cmake_minimum_required Version
* clean default controller + playmotion2 added
* update launch files
* update motions files
* default controllers added
* controller_configuration configs file
* add more dependencies to pal_sea_arm_controller_configuration
* migration of pal_sea_arm_description folder
* migration of CMakeLists.txt and package.xml to ros2
* Contributors: Adria Roig, ileniaperrella

0.1.3 (2023-10-27)
------------------

0.1.2 (2023-10-24)
------------------

0.1.1 (2023-10-23)
------------------

0.1.0 (2023-10-20)
------------------
* Merge branch 'new_name' into 'master'
  Change tiago_pro_arm ro pal_sea_arm and combine both urdf
  See merge request robots/pal_sea_arm!9
* Changes after removing pal_sea_arm_controller_configuration_gazebo
* Address comments + fix colors
* Change tiago_pro_arm ro pal_sea_arm and combine both urdf
* Contributors: Jordan Palacios, thomaspeyrucain
