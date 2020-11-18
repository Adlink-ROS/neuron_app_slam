import os
from glob import glob
from setuptools import setup

package_name = 'napp_slam'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ChenYing Kuo',
    maintainer_email='chenying.kuo@adlinktech.com',
    description='Neuron APP launch script for SLAM',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'teleop_twist_keyboard = napp_slam.teleop_twist_keyboard:main'
        ],
    },
)
