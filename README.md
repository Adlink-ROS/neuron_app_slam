# Neuron APP: SLAM

# Support Platform:

* ADLINK Controller:
  - ROScube-I
  - ROScube-X
  - ROScube starterkit
* ROS version:
  - ROS 2 foxy

# Usage

## Quickstart

**Please enter workspace of SLAM in Neuron IDE before you start Neuron App.**

***Note! If pictures is too small for your equipment. please click [Here](https://github.com/Adlink-ROS/neuron_app_slam/blob/master/README.md) to open github page.***

1. Open "Packages:Resources" on the right side.

2. Open list by clicking "user-workspace" -> "napp_slam"

     ![](readme_resource/click_resourse_slam.png)


***NOTE!!! Following instruction would need : Right click desired launch file and click "Run" -> "Run Launch File" as image bellow***

   ![](readme_resource/launch_slam.png)

3. Launch SLAM and Rviz, choose **ONE**  file to launch: 

     * For simulation, launch SLAM application and Gazebo simultaneously: **Launch gazebo_slam.launch.py in napp_slam**

     * Deploy on Neuronbot2: **Launch neuronbot_slam.launch.py in napp_slam**

4. The mouse teleop panel would show up after launching SLAM. Teleop NeuronBot2 to explore the world, click and drag on the mouse teleop.

   ![](readme_resource/mouse_slam.gif)

5. Save the map, **Launch map_saver_cli.launch.py in napp_slam**

   The saved map will be stored in directory of neuron_app_slam, which is "yourmap.yaml" and "yourmap.pgm".

   Then, you shall turn off SLAM.
