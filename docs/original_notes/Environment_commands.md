cd 0_vo  (This version needs Ubuntu 24.04, ROS2 Jazzy, and GZ Harmonic 8.9.0 combination)

📌 🧭 ❤️ ✅ 🔥 🎯 ➡️ ⭐
###################


####    Run 0_vo
This folder contain many workspaces
(yard_20x20, house, and saye_world) in addition to the default world.

# ⭐ Terminal— sorce package is (opt/ros/jazzy/share/nav2_bringup/launch)

~$ ros2 launch nav2_bringup tb4_simulation_launch.py   slam:=True   headless:=False   # default world

# For costum world
ros2 launch nav2_bringup tb4_simulation_launch.py   slam:=True   headless:=False   world:=/home/dhayaa/0_vo/my_worlds/vo_office_30x20_corridor_1.sdf


# Saving the map
ros2 run nav2_map_server map_saver_cli -f ~/0_vo/maps/office  # map1 is the name of the map (map1.yaml, map1.pgm)

# Run the simulation with saved map
ros2 launch nav2_bringup tb4_simulation_launch.py \
  slam:=False \
  use_localization:=True \
  map:=/home/dhayaa/0_vo/maps/depot.yaml \
  headless:=False

# If you also want to use your custom world
ros2 launch nav2_bringup tb4_simulation_launch.py \
  slam:=False \
  use_localization:=True \
  map:=/home/dhayaa/0_vo/maps/office.yaml \
  world:=/home/dhayaa/0_vo/my_worlds/vo_office_30x20_corridor_1.sdf \
  headless:=False

# If you want to use your own Nav2 params (recommended)
ros2 launch nav2_bringup tb4_simulation_launch.py \
  slam:=False \
  use_localization:=True \
  map:=/home/dhayaa/0_vo/maps/office.yaml \
  params_file:=/home/dhayaa/tb4_cfg/nav2_params.yaml \
  world:=/home/dhayaa/my_worlds/vo_office_30x20_corridor_1.sdf \
  headless:=False  

# To view the frames
ros2 run tf2_tools view_frames   # the pdf file will saved in home directory

# To kill gazebo
pkill -f 'gz sim'     
pkill -f 'gz gui'      
pkill -x gz  


🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
📌 Working on (warehouse_world.sdf)
# ⭐ Terminal— SLAM
ros2 launch nav2_bringup tb4_simulation_launch.py   slam:=True   headless:=False   world:=/home/dhayaa/0_vo/my_worlds/warehouse_world.sdf

# ⭐ Terminal 2— save the map
ros2 run nav2_map_server map_saver_cli -f ~/0_vo/maps/warehouse  # map1 is the name of the map (map1.yaml, map1.pgm)

# ⭐ Terminal— Localization
ros2 launch nav2_bringup tb4_simulation_launch.py \
  slam:=False \
  use_localization:=True \
  map:=/home/dhayaa/0_vo/maps/warehouse.yaml \
  world:=/home/dhayaa/0_vo/my_worlds/warehouse_world.sdf \
  headless:=False