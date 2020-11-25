import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (IncludeLaunchDescription, GroupAction)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions.node import Node

def generate_launch_description():
    teleop_joy_launch = os.path.join(get_package_share_directory('teleop_twist_joy'), 'launch')
    napp_teleop_joy = GroupAction([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(teleop_joy_launch, 'teleop-launch.py')),
            launch_arguments={'joy_config': 'xbox'}.items()),
    ])
    ld = LaunchDescription()
    ld.add_action(napp_teleop_joy)
    return ld
