# Vehicle_model

This is to exercise the urdf and ROS2 frame in virtual environment

# Requirements
I tested them in Ubuntu20.04 and ROS2 foxy.

* lgsvl_simulator : https://github.com/lgsvl/simulator/releases/tag/2020.06
* lgsvl_msg : https://github.com/endland/lgsvl_msg
* ros2_lgsvl_bridge : https://github.com/endland/ros2_lgsvl_bridge

# Building
download lgsvl_simulator from upper link
pull the repositories to your workspace

```
colcon build --symlink-install --packages-select lgsvl_msg
colcon build --symlink-install --packages-select ros2_lgsvl_bridge
colcon build --symlink-install --packages-select vehicle_model
sourc install/setup.bash
```

# Running

```
lgsvl_bridge [--port 9090] [--log D]
./simulator
ros2 launch vehicle_model vehicle_visualization.launch.py

```

![Alt text](/simulator.png)
