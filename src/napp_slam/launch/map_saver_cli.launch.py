import os

from launch import LaunchDescription
from launch_ros.actions.node import Node

def generate_launch_description():

    map_saver_cli = Node(
        package='nav2_map_server',
        executable='map_saver_cli',
        parameters=[{'save_map_timeout': 10000}],
        arguments=['-f', 'yourmap'],
        output='screen'
    )

    ld = LaunchDescription()
    ld.add_action(map_saver_cli)
    return ld
