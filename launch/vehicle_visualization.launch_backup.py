import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    urdf_file_name = 'urdf/vehicle.xacro'
    print("urdf_file_name : {}".format(urdf_file_name))

    urdf = os.path.join(
    	get_package_share_directory('vehicle_model'),
    	urdf_file_name)
    
    print("urdf_path : {}".format(urdf))

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            arguments=[str(urdf)]), 
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            output='screen'
        )
        
    ])
