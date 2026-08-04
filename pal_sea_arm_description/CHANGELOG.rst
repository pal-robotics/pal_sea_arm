^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package pal_sea_arm_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.0.3 (2024-03-22)
------------------
* Merge branch 'dtk/fix/restructure' into 'humble-devel'
  Dtk/fix/restructure
  See merge request robots/pal_sea_arm!23
* update copyright year
* Update copyright year
* Add missing robot_state_publisher dependency
* Add missing pal_sea_arm_controller_configuration dependency
* fix order of loading urdf args and ros2_control macro
* Comment custom end effector for now
* Use common sim time arg and set it to True by default for simulation laucnh files
* Change all occurences of no-ee to no-end-effector
* Migrate tests
* Change urdf-check to no-end-effector
* Restructure launch files
* Add namespace to urdf file
* Remove space after colon in urdf to avoid this issue: https://github.com/ros2/launch_ros/issues/214
* Add arm model check in urdf
* Contributors: David ter Kuile, Noel Jimenez, davidterkuile

2.8.4 (2026-08-04)
------------------
* Adding missing rh8d description dep
* Contributors: oscarmartinez

2.8.3 (2026-07-30)
------------------
* Proper launch of the RH8D hand
  Removes the mimic flag and properly loads the topic based system (used
  for the HW hand)
* Contributors: Óscar Martínez

2.8.2 (2026-07-20)
------------------
* add pen-gripper as ee
* Contributors: susannamastromauro

2.8.1 (2026-07-06)
------------------

2.8.0 (2026-07-03)
------------------

2.7.0 (2026-07-02)
------------------
* Merge branch 'fix_arm_4_inertia' into 'humble-devel'
  Fix inertia rotation of arm 4 link
  See merge request robots/pal_sea_arm!139
* Arm link 4 : use same inertia origin as old fake-forearm link
* Remove rotation from arm link 4 inertia
* Merge branch 'rm/fake_forearm' into 'humble-devel'
  Remove fake_forearm end effector
  See merge request robots/pal_sea_arm!137
* Remove fake_forearm end effector
* Contributors: Aina, Aina Irisarri, Pierre Fernbach, Sai Kishor Kothakota

2.6.0 (2026-06-25)
------------------
* Add condition for 4dof arm without ee
* Change fakeforearm to 4dof without end effector
* Removing incorrect tool offset in 5dof
* Contributors: Aina, Óscar Martínez

2.5.1 (2026-06-17)
------------------
* Match axis with ROS 1 version
* Contributors: Aina

2.5.0 (2026-06-04)
------------------

2.4.1 (2026-05-29)
------------------
* Fix axis
* Contributors: Aina

2.4.0 (2026-05-20)
------------------
* Update end_effector_camera.urdf.xacro
* Contributors: martinaannicelli

2.3.1 (2026-05-12)
------------------
* reduce 7 limit for spherical and straight wrist
* reduce limit 7 TP spherical
* Reducing arm_7 upper/lower bound
* Contributors: ileniaperrella

2.3.0 (2026-05-12)
------------------
* Fix rotation direction
* Remove unused meshes
* Link 5 short wrist with the tiago pro one
* Merge spherical wrist with the tiago pro one
* Contributors: Aina

2.2.1 (2026-04-29)
------------------
* change values limits joint6
* Contributors: susannamastromauro

2.2.0 (2026-04-28)
------------------
* tmp remove dependency
* Split end effectors into sides
* Add kangaroo arms
* Contributors: Aina

2.1.1 (2026-04-16)
------------------
* Add error_protection and idle_mode_on_stop parameters to true
* Contributors: Noel Jimenez

2.1.0 (2026-04-15)
------------------
* Add arguments to support the new gazebo
* Contributors: thomas.peyrucain

2.0.1 (2026-04-10)
------------------

2.0.0 (2026-03-31)
------------------
* delete comment
* fix property joint_type
* set 3th and 5th as infinite joints
* fix collision arm 6th and 7th
* fix 6th link standalone
* add 7th link collision
* delete comment
* remove use_sim_time
* delete whitespace
* add 5th joint in short and straight wrist properties
* Fix spherical wrist properties and origins
* fix 1st joint
* fix 7th joint
* Fix rotate axe for joint 6
* Fix module
* adding limit j1
* change limits j3
* fix z\_ value of base_link
* fix limits j1 and j3
* add continuous joint and remove camera param
* remove camera parameter from yaml file
* include arm_7_link collision
* update arm-standalone
* fix simulation and 7-link-mesh
* Contributors: Aina, susannamastromauro

1.25.0 (2026-03-18)
-------------------
* Add missing limits_v2 for the arm_5_joint when using short-wrist
* Add support for short-wrist
* Contributors: Noel Jimenez

1.24.0 (2026-02-18)
-------------------
* Add new limits values
* Add limits_v2
* Contributors: Aina

1.23.2 (2026-02-10)
-------------------
* adding calibration_tool param
* Contributors: silviamasiello

1.23.1 (2026-02-03)
-------------------
* update limit for straight wrist
* Contributors: ileniaperrella

1.23.0 (2026-02-02)
-------------------

1.22.1 (2026-01-08)
-------------------

1.22.0 (2025-12-05)
-------------------
* Add gazebo_version xacro argument
* Contributors: Noel Jimenez

1.21.0 (2025-10-29)
-------------------

1.20.2 (2025-10-29)
-------------------
* Fix humble tests excluding allegro hand end-effector
* Contributors: Noel Jimenez

1.20.1 (2025-10-27)
-------------------
* Add condition for allegro_hand dependencies
* Contributors: Noel Jimenez

1.20.0 (2025-10-23)
-------------------
* Add the new weight taking into account the cables and screws
* Remove difference between S+ and S- motors
* Update license
* Contributors: Aina, thomaspeyrucain

1.19.1 (2025-10-13)
-------------------
* Merge branch 'fix/condition_private_packages' into 'humble-devel'
  Add PAL_DISTRO condition for non-public packages
  See merge request robots/pal_sea_arm!94
* Add PAL_DISTRO condition for non-public packages
* Merge branch 'feature/add_end_effector_camera' into 'humble-devel'
  Add the option of realsense d405
  See merge request robots/pal_sea_arm!80
* Fixing description end effector camera
* Unifying joint in macro of cameras
* Adding realsense 435
* Add the option of realsense d405
* Merge branch 'ipe/update-velocity-limits' into 'humble-devel'
  update velocity limits for S+, S- and XS
  See merge request robots/pal_sea_arm!92
* update velocity limits for S+, S- and XS
* Contributors: Noel Jimenez, ileniaperrella, thomaspeyrucain, vivianamorlando

1.19.0 (2025-09-08)
-------------------
* Add missing sim_type xacro args
* Fixed arm controller configuration file
* fixed real time simulation command interface
* restored to original version
* change xacro parameter and launch argument name
* changed mujoco xacro parameter name
* changed world launch argument name
* added mujoco command interface
* Improved mujoco model structure
* Improved launch arguments
* Added arm_type and wrist_model argument
* Imporved argument
* Improved logic for the mujoco robot description
* Changed default arm_type
* reduced number of arguments
* Changed arm kp value
* Fixed frame orientation
* Fixed arm joint names
* changed kp value
* changed mesh name
* changed link definition
* changed macro name
* Added mujoco tags
* Contributors: David ter Kuile, Ortisa Poci

1.18.7 (2025-08-01)
-------------------
* Fixing link 5, 6 & 7
* Contributors: susannamastromauro

1.18.6 (2025-07-29)
-------------------

1.18.5 (2025-07-28)
-------------------

1.18.4 (2025-07-28)
-------------------
* Merge branch 'tpe/fix_tiago_pro_s' into 'humble-devel'
  Fix inertia parameter
  See merge request robots/pal_sea_arm!85
* Fix inertia parameter
* Contributors: thomas.peyrucain, thomaspeyrucain

1.18.3 (2025-07-23)
-------------------

1.18.2 (2025-06-17)
-------------------

1.18.1 (2025-06-06)
-------------------
* Use pal_urdf_utils meshes
* Change path related to restructure path for pal_urdf_utils
* Remove sensors from pal_sea_arm_description
* Change path for ftsensor into a more detailed one
* Contributors: Aina

1.18.0 (2025-05-29)
-------------------

1.17.5 (2025-05-28)
-------------------

1.17.4 (2025-04-29)
-------------------

1.17.3 (2025-04-28)
-------------------

1.17.2 (2025-04-17)
-------------------
* Replace use_sim
* Fix param use_sim_time name
* Add allegro hand as end effector
* Contributors: Aina, davidterkuile

1.17.1 (2025-04-11)
-------------------

1.17.0 (2025-04-10)
-------------------

1.16.0 (2025-04-09)
-------------------

1.15.3 (2025-04-09)
-------------------

1.15.2 (2025-04-03)
-------------------

1.15.1 (2025-03-31)
-------------------

1.15.0 (2025-03-27)
-------------------
* Better transmissions names
* Support in the pal_sea_arm_description
* Adding missing dep
* SEA transmission optional loading
* Adding absolute_position joint state interface
* Adapted to new data loading mechanism
* added torque state interface
* added paths to sea data
* Contributors: Daniel Costanzi, oscarmartinez

1.14.5 (2025-02-28)
-------------------
* Merge branch 'tpe/add_inertia_version' into 'humble-devel'
  Add Inertia version for the new arm
  See merge request robots/pal_sea_arm!56
* Update arm.properties.xacro
* Address comments
* Add Inertia version for the new arm
* Contributors: davidterkuile, thomas.peyrucain, thomaspeyrucain

1.14.4 (2025-02-19)
-------------------
* Merge branch 'tpe/fix_ft_sensor' into 'humble-devel'
  Fix ATI sensor in gazebo simulation
  See merge request robots/pal_sea_arm!62
* Fix ATI sensor in gazebo simulation
* Contributors: thomas.peyrucain, thomaspeyrucain

1.14.3 (2025-02-05)
-------------------

1.14.2 (2025-01-23)
-------------------
* Merge branch 'tpe/update_collision_model' into 'humble-devel'
  Update collision model to match the link5 specific shape
  See merge request robots/pal_sea_arm!59
* Rotate collision link
* Update collision model to match the link5 specific shape
* Contributors: thomas.peyrucain, thomaspeyrucain

1.14.1 (2025-01-21)
-------------------
* Rename ati mesh because of a mujoco bug if 2 meshes are called the same
* Contributors: thomas.peyrucain

1.14.0 (2025-01-16)
-------------------
* Merge branch 'tpe/simplify-3d-model' into 'humble-devel'
  Add simplyfied models
  See merge request robots/pal_sea_arm!55
* Remove comments
* Simplify arm_7_link + update ATI meshes and inertia
* Add simplyfied models
* Contributors: thomas.peyrucain, thomaspeyrucain

1.13.0 (2024-11-07)
-------------------

1.12.0 (2024-10-29)
-------------------
* Add xacro tests
* Contributors: Aina

1.11.6 (2024-10-21)
-------------------
* Merge branch 'tpe/fix_joint_limit' into 'humble-devel'
  Fix joint limit
  See merge request robots/pal_sea_arm!51
* Fix joint limit
* Merge branch 'air/feat/add_camera' into 'humble-devel'
  Add camera link
  See merge request robots/pal_sea_arm!50
* Adding real 5th mesh
* Add camera link
* Merge branch 'tpe/fix_inertia_wrist' into 'humble-devel'
  Fix wrist inertia
  See merge request robots/pal_sea_arm!48
* Fix wrist inertia
* Merge branch 'ipe/update-vel-lim' into 'humble-devel'
  update joint max velocity limit for tiago pro
  See merge request robots/pal_sea_arm!49
* update joint max velocity limit for tiago pro
* Contributors: Aina, ileniaperrella, thomas.peyrucain, thomaspeyrucain, vivianamorlando

1.11.5 (2024-10-09)
-------------------
* Merge branch 'fix/syntax_warning' into 'humble-devel'
  Fix SyntaxWarning messages when comparing values
  See merge request robots/pal_sea_arm!46
* Fix SyntaxWarning messages when comparing values
* Add reflect on the 5th joint
* Contributors: Noel Jimenez, thomas.peyrucain, thomaspeyrucain

1.11.4 (2024-10-08)
-------------------
* Merge branch 'dtk/fix/joint-limit-tiago-pro-7-joint' into 'humble-devel'
  reduce joint limits according to test with robot
  See merge request robots/pal_sea_arm!27
* reduce joint limits according to test with robot
* Merge branch 'vmo/fix_joint_6' into 'humble-devel'
  Fixing the 6 axis joint
  See merge request robots/pal_sea_arm!45
* Fix to use same urdf for tiago sea and tiago pro
* Adding meshes for tc
* add material + fix 7th joint
* Change joint limit
* Fixing the 6 axis joint
* Contributors: thomas.peyrucain, thomaspeyrucain, vivianamorlando

1.11.3 (2024-10-02)
-------------------
* Merge branch 'tpe/fix_wrist' into 'humble-devel'
  Switch back the wrist as before to respect the ft norms + update joint limits of joint 6
  See merge request robots/pal_sea_arm!44
* Update collision model
* Switch back the wrist as before to respect the ft norms + update joint limits of joint 6
* Contributors: thomas.peyrucain, thomaspeyrucain

1.11.2 (2024-09-30)
-------------------

1.11.1 (2024-09-27)
-------------------
* Merge branch 'omm/final_std' into 'humble-devel'
  Final arm std
  See merge request robots/pal_sea_arm!42
* Update on link 7 + fix joint limits
* Limits new structure
* Proper orientation of 5th joint in spherical wrist
* Contributors: oscarmartinez, thomas.peyrucain, thomaspeyrucain

1.11.0 (2024-09-19)
-------------------
* Set default wrist to straight
* Gripper with rokubi position fixed
* Removing checks
* Orientation std
* Fixed link 6 and tool_changer rotation
* Standalone meshes
* Updated tests
* Suggested changes
* Proper colors for ATI FT
* Support for different FT models at the same time
* Final checks
* TC working for all combinations
* No TC working for all combinations
* Arms versions std
* FT sensor std
* Fixed straight wrist joint orientation
* Initial support for all arms, with tests
* Arm std with new wrist type arg
* Contributors: David ter Kuile, oscarmartinez

1.10.1 (2024-09-09)
-------------------

1.10.0 (2024-08-06)
-------------------
* Update robot_state_publisher_model
* Contributors: davidterkuile

1.0.9 (2024-07-11)
------------------
* Add degree to radian conversion in joint 1 soft limit
* Contributors: David ter Kuile

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

1.0.5 (2024-05-09)
------------------
* Merge branch 'omm/feat/arm_name_std' into 'humble-devel'
  Changed arm_model to arm_type in the URDF
  See merge request robots/pal_sea_arm!25
* Changed arm_model to arm_type in the URDF
* Contributors: davidterkuile, oscarmartinez

1.0.4 (2024-04-26)
------------------
* Remove unused tags and add offset tag
* Fix correct actuator name in transmission macro
* 1.0.3
* Update Changelog
* update copyright year
* Update copyright year
* Add missing robot_state_publisher dependency
* Add missing pal_sea_arm_controller_configuration dependency
* fix order of loading urdf args and ros2_control macro
* Comment custom end effector for now
* Use common sim time arg and set it to True by default for simulation laucnh files
* Change all occurences of no-ee to no-end-effector
* Migrate tests
* Change urdf-check to no-end-effector
* Restructure launch files
* Add namespace to urdf file
* Remove space after colon in urdf to avoid this issue: https://github.com/ros2/launch_ros/issues/214
* Add arm model check in urdf
* Contributors: David ter Kuile, Noel Jimenez, davidterkuile

1.0.2 (2024-03-07)
------------------
* Merge branch 'dtk/fix/add-linter-tests' into 'humble-devel'
  Add linter tests and update linting
  See merge request robots/pal_sea_arm!21
* Add tests packages to package.xml
* Add linter tests and update linting
* Contributors: David ter Kuile, davidterkuile

1.0.1 (2024-01-29)
------------------

1.0.0 (2024-01-29)
------------------
* Merge branch 'ros2-migration' into 'humble-devel'
  Ros2 migration
  See merge request robots/pal_sea_arm!17
* fix name of the ros2_control gripper
* update to 3.8 the cmake_minimum_required Version
* added ament_python_install_package for pal_sea_arm_description
* fix deg_to_rad extension
* update limits for joint 4 + weights
* change with simple transmission
* update launch files
* number arg deleted
* impl. node pal_sea_arm_utils
* delete number element in the arm transmission
* integration of the ft
* clean robot_state_publisheclean robot_state_publisherr
* spawn the arm in rviz with pal-pro-gripper
* migration of pal_sea_arm_description folder
* migration of CMakeLists.txt and package.xml to ros2
* Contributors: Adria Roig, ileniaperrella

0.1.3 (2023-10-27)
------------------
* Merge branch 'add/missing_folder' into 'master'
  Add gazebo folder to the install rules
  See merge request robots/pal_sea_arm!14
* Add gazebo folder to the install rules
* Contributors: Jordan Palacios, thomas.peyrucain

0.1.2 (2023-10-24)
------------------
* Merge branch 'add_sea_transmissions' into 'master'
  add the SEA simple transmissions for all the arm joints
  See merge request robots/pal_sea_arm!10
* rename the macro to arm_pro_simple_transmission and fix a minor bug
* add the SEA simple transmissions for all the arm joints
* Contributors: Sai Kishor Kothakota

0.1.1 (2023-10-23)
------------------
* Merge branch 'update-joints-limits' into 'master'
  Updated joint limits to match real robot
  See merge request robots/pal_sea_arm!13
* updated joint limits to match real robot
* Contributors: Jordan Palacios, danielcostanzi

0.1.0 (2023-10-20)
------------------
* Merge branch 'fix/ft_naming' into 'master'
  Change arm_ft\_ to wrist_ft to match TIAGo
  See merge request robots/pal_sea_arm!12
* Change arm_ft\_ to wrist_ft to match TIAGo
* Merge branch 'fix/rostest' into 'master'
  Fix typo on rostest
  See merge request robots/pal_sea_arm!11
* Add test dependencies
* Fix typo on rostest + add dependency
* Merge branch 'new_name' into 'master'
  Change tiago_pro_arm ro pal_sea_arm and combine both urdf
  See merge request robots/pal_sea_arm!9
* Improve wheight of the links + fix link collision that was to small to visualize the marker in moveit
* Add dependency
* Address comments + fix colors
* Extract inertial and joints parameters to fusion both urdf
* Remove arm_base_link from arm urdf
* Change parameter and naming
* Change tiago_pro_arm ro pal_sea_arm and combine both urdf
* Contributors: Jordan Palacios, thomaspeyrucain
