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
* Remove base_link from arm urdf
* Change parameter and naming
* Change tiago_pro_arm ro pal_sea_arm and combine both urdf
* Contributors: Jordan Palacios, thomaspeyrucain
