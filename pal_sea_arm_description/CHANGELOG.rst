^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package pal_sea_arm_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.1.9 (2024-09-12)
------------------
* Merge branch 'ipe/sea-transmiss-depend' into 'master'
  add sea_transmission dependency with condition
  See merge request robots/pal_sea_arm!40
* fix typo
* update package format
* add sea_transmission dependency with condition
* Contributors: davidterkuile, ileniaperrella

0.1.8 (2024-09-09)
------------------
* Merge branch 'ipe/update-limit-4' into 'master'
  update limit joint 4
  See merge request robots/pal_sea_arm!39
* update limit joint 4
* Contributors: davidterkuile, ileniaperrella

0.1.7 (2024-05-29)
------------------
* Merge branch 'dtk/fix/joint-7-joint-limit-tiago-pro' into 'master'
  Update joint limit for joint 7 tiago pro
  See merge request robots/pal_sea_arm!29
* Update joint limit for joint 7 tiago pro
* Contributors: David ter Kuile, davidterkuile

0.1.6 (2024-03-11)
------------------

0.1.5 (2023-12-04)
------------------
* Merge branch 'tpe/fix/standalone_arm_limits' into 'master'
  Fix motions for the standalone arm + joint 4 Fix elbow joint limit
  See merge request robots/pal_sea_arm!16
* Fix motions for the standalone arm + joint 4 Fix elbow joint limit
* Contributors: Sai Kishor Kothakota, thomas.peyrucain

0.1.4 (2023-12-04)
------------------
* Merge branch 'fix_elbow_joint_limit' into 'master'
  Fix elbow joint limit
  See merge request robots/pal_sea_arm!15
* fix elbow joint limit
* Contributors: Luca Marchionni, Sai Kishor Kothakota

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
