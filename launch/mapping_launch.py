from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    pkg_share = get_package_share_directory('dynamic_occupancy_map')
    rviz_dir = os.path.join(pkg_share, 'rviz')
    data_dir = os.path.join(pkg_share, 'data')

    bag_dir_arg = DeclareLaunchArgument(
        'bag_dir',
        default_value=data_dir
    )

    dataset_name_arg = DeclareLaunchArgument(
        'dataset_name',
        default_value='street'
    )

    bag_play = ExecuteProcess(
        cmd=[
            'ros2', 'bag', 'play',
            PathJoinSubstitution([
                LaunchConfiguration('bag_dir'),
                LaunchConfiguration('dataset_name')
            ])
        ],
        output='screen'
    )

    return LaunchDescription([
        bag_dir_arg,
        dataset_name_arg,
        # bag_play,
        Node(
            package='dynamic_occupancy_map',
            executable='map_sim_example',
            name='map_sim_example',
            output='screen'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz3',
            arguments=['-d', os.path.join(rviz_dir, 'original_pointcloud.rviz')],
            output='screen'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', os.path.join(rviz_dir, 'future_status.rviz')],
            output='screen'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz',
            arguments=['-d', os.path.join(rviz_dir, 'boxes.rviz')],
            output='screen'
        ),
    ])

