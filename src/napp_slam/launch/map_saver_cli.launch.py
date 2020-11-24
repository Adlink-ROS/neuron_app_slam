import os

from launch import LaunchDescription
from launch_ros.actions.node import Node
from pathlib import Path

def generate_launch_description():

    map_saver_cli = Node(
        package='nav2_map_server',
        executable='map_saver_cli',
        parameters=[{'save_map_timeout': 10000}],
        arguments=['-f', str(Path.home())+'/neuron_app_slam/yourmap'],
        output='screen'
    )

    ld = LaunchDescription()
    ld.add_action(map_saver_cli)
    return ld
