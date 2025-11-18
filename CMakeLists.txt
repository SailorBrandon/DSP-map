cmake_minimum_required(VERSION 3.5)
project(dynamic_occupancy_map)

# if(POLICY CMP0074)
#   cmake_policy(SET CMP0074 NEW)
# endif()

add_definitions(-std=c++17 -g -O3 -ftree-vectorize -ffast-math -march=native -lpthread)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(visualization_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(gazebo_msgs REQUIRED)
find_package(pcl_conversions REQUIRED)
find_package(PCL REQUIRED)

add_definitions(${PCL_DEFINITIONS})

include_directories(
  include
  ${PCL_INCLUDE_DIRS}
  /usr/local/include/munkres
)

set(MunkresLIB
  /usr/local/lib/libmunkres.a
)

add_executable(map_sim_example src/map_sim_example.cpp)

ament_target_dependencies(map_sim_example
  rclcpp
  sensor_msgs
  geometry_msgs
  visualization_msgs
  nav_msgs
  std_msgs
  gazebo_msgs
  pcl_conversions
)

target_link_libraries(map_sim_example
  ${PCL_LIBRARIES}
  ${MunkresLIB}
)

install(TARGETS map_sim_example
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY launch rviz
  DESTINATION share/${PROJECT_NAME}
)

install(DIRECTORY data
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
