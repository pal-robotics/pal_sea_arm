cmake_minimum_required(VERSION 3.8)
project(pal_sea_arm_description)

find_package(ament_cmake_auto REQUIRED)

ament_auto_find_build_dependencies()

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()

  foreach(arm_model pal-sea-arm-standalone tiago-pro tiago-sea tiago-sea-dual)
    # Separated to speed up tests, otherwise it's over 13min
    foreach(end_effector no-end-effector pal-pro-gripper)
        foreach(ft_sensor no-ft-sensor rokubi)
          add_launch_test(
            test/test_description.launch.py
            TARGET "pal_sea_arm_description_${arm_model}_${end_effector}_${ft_sensor}"
            ARGS "arm_model:=${arm_model}" "end_effector:=${end_effector}" "ft_sensor:=${ft_sensor}"
          )
        endforeach()
    endforeach()
  endforeach()

endif()


# Install Python modules
ament_python_install_package(${PROJECT_NAME})

ament_auto_package(INSTALL_TO_SHARE config gazebo launch meshes robots ros2_control urdf) #test
