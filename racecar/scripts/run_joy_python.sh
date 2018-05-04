source ~/catkin_ws/devel/setup.bash 
cd ~/catkin_ws/src/racecar/racecar/
roscore &
rosparam load config/racecar-v2/joy_teleop.yaml 
cd scripts/
python joy_teleop.py

