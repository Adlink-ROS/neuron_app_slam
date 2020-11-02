import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (IncludeLaunchDescription, GroupAction)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    # Path
    gazebo_launch_dir = os.path.join(get_package_share_directory('neuronbot2_gazebo'), 'launch')
    nb2slam_launch_dir = os.path.join(get_package_share_directory('neuronbot2_slam'), 'launch')

    # Parameters
    use_sim_time = LaunchConfiguration('use_sim_time', default='True')
    open_rviz = LaunchConfiguration('open_rviz', default='True')
    ## mememan_world.model / phenix_world.model
    world_model = LaunchConfiguration('world_model', default='mememan_world.model')

    neuron_app_bringup = GroupAction([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(gazebo_launch_dir, 'neuronbot2_world.launch.py')),
            launch_arguments={'use_sim_time': use_sim_time,
                              'world_model': world_model}.items()),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(nb2slam_launch_dir, 'gmapping_launch.py')),
            launch_arguments={'use_sim_time': use_sim_time,
                              'open_rviz': open_rviz}.items()),
    ])

    ld = LaunchDescription()
    ld.add_action(neuron_app_bringup)
    return ld
