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

1. Click application in Neuron App to open workspace. **Click SLAM.**  It will build the resource at first time it's opened.
     ![](readme_resource/open_app.png)
   
2-1. Click "packages" on the right side.

2-2. Open list by click "RESOURCES" -> "user-workspace" -> "napp_slam"
     ![](readme_resource/click_resourse_slam.png)
     

***NOTE!!! Following instruction would need : Right click desired launch file and click "Run" -> "Run Launch File" as image bellow***

   ![](readme_resource/launch_slam.png)
     
3. Launch SLAM and Rviz, choose **ONE**  file to launch: 
   
     * For simulation, launch SLAM application and Gazebo simultaneously: **Launch gazebo_slam.launch.py**
     
     * Deploy on Neuronbot2: **Launch neuronbot_inspection.launch.py**

4. Teleop NeuronBot2 to explore the world, click and drag on the mouse teleop.
   
   ![](readme_resource/mouse_slam.gif)
   
5. Save the map, **Launch map_saver_cli.launch.py**

   The saved map will be stored in directory of neuron_app_slam, which is "yourmap.yaml" and "yourmap.pgm".

   Then, you shall turn off SLAM.
