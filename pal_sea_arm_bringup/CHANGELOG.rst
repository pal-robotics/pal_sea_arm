^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package pal_sea_arm_bringup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.0.3 (2024-03-22)
------------------
* Merge branch 'dtk/fix/restructure' into 'humble-devel'
  Dtk/fix/restructure
  See merge request robots/pal_sea_arm!23
* update copyright year
* Restructure launch files pal-sea-arm-bringup
* Contributors: David ter Kuile, davidterkuile

1.0.2 (2024-03-07)
------------------

1.0.1 (2024-01-29)
------------------

1.0.0 (2024-01-29)
------------------
* Merge branch 'fix-dep' into 'humble-devel'
  fix depend.
  See merge request robots/pal_sea_arm!18
* fix depend joint_trajectory_controller
* Merge branch 'ros2-migration' into 'humble-devel'
  Ros2 migration
  See merge request robots/pal_sea_arm!17
* delete configs file that are already defined in the TIAGo PRO pkgs
* add jtc jsb exec_depend
* clean the yaml file for play_motion2 deleting ft_sensor param
* fix typo
* delete the ft_sensor param in the joyteleop bc not necessary
* uncomment the gripper in the joytelop config files
* update to 3.8 the cmake_minimum_required Version
* clean default controller + playmotion2 added
* update motions files
* add launch files foor bringup
* fix motion file indentation
* enable regen_em_file to generate the configs file in the bringup
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
* Address comments + fix colors
* Change tiago_pro_arm ro pal_sea_arm and combine both urdf
* Contributors: Jordan Palacios, thomaspeyrucain
