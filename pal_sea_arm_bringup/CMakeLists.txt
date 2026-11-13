cmake_minimum_required(VERSION 3.10)
project(pal_sea_arm_bringup)

find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()
if(pal_module_cmake_FOUND)
  pal_register_modules(
    module/10_play_motion2.yaml
  )
elseif(DEFINED ENV{PAL_DISTRO})
  message(FATAL_ERROR "The pal_module_cmake package was not found. Modules not registered.")
endif()

install(
  PROGRAMS scripts/regen_em_file.py scripts/calibrate_ft_sensor.sh
  DESTINATION lib/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_auto_package(INSTALL_TO_SHARE config launch)