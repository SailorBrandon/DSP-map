cmake_minimum_required(VERSION 3.8)
project(dynamic_occupancy_map)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(message_filters REQUIRED)
find_package(image_transport REQUIRED)
find_package(visualization_msgs REQUIRED)
find_package(gazebo_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(PCL REQUIRED)
find_package(pcl_conversions REQUIRED)
add_definitions(${PCL_DEFINITIONS})

set(MunkresLIB
  /usr/local/lib/libmunkres.a
)

add_executable(map_sim_example src/map_sim_example.cpp)
target_include_directories(map_sim_example PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>
  ${PCL_INCLUDE_DIRS}
  /usr/local/include/munkres
)
target_compile_features(map_sim_example PUBLIC cxx_std_14)
target_compile_options(map_sim_example PRIVATE
  -g
  -O3
  -ftree-vectorize
  -ffast-math
  -march=native
)
ament_target_dependencies(map_sim_example
  rclcpp
  std_msgs
  sensor_msgs
  message_filters
  image_transport
  pcl_conversions
  visualization_msgs
  gazebo_msgs
  geometry_msgs
)

target_link_libraries(map_sim_example
  ${PCL_LIBRARIES}
  ${MunkresLIB}
  pthread
)

install(TARGETS
  map_sim_example
  DESTINATION lib/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

install(DIRECTORY launch 
  DESTINATION share/${PROJECT_NAME}
)
install(DIRECTORY rviz 
  DESTINATION share/${PROJECT_NAME}
)



ament_package()