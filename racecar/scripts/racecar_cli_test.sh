source ~/catkin_ws/devel/setup.bash
cd ~/catkin_ws/src/racecar/racecar/scripts
#source rosenv.sh 192.168.1.98 192.168.1.228
source rosenv.sh 192.168.1.225 192.168.1.225
#source rosenv.sh 192.168.5.136 192.168.5.136
roslaunch racecar teleop_cli.launch

