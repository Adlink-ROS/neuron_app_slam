# Neuron APP: SLAM

# Support Platform:

* ADLINK Controller:
  - ROScube-I
  - ROScube-X
  - ROScube starterkit
* ROS version:
  - ROS 2 foxy

# Usage
1. Click application in Neuron App to open workspace. It will build the resource at first time it's opened.
   ![](readme_resource/open_app.png)
   
2-1. Click "packages" on the right side.
2-2. Open list by click "resources" -> "user-workspace" -> "napp_slam"
   ![](readme_resource/click_resourse_slam.png)
1. Launch SLAM and Rviz 
   
   * For simulation, launch SLAM application and Gazebo simultaneously.
   ```
   ros2 launch napp_slam gazebo_slam.launch.py
   ```
2. Teleop NeuronBot2 to explore the world
   ```
   # Run on the other terminal
   source /opt/ros/foxy/setup.bash
   ros2 run teleop_twist_keyboard teleop_twist_keyboard
   ```
   ![](readme_resource/slam_teleop_8x.gif)
3. Save the map
   ```
   source /opt/ros/foxy/setup.bash 
   ros2 launch napp_slam map_saver_cli.launch.py
   ```

   Then, you shall turn off SLAM.
