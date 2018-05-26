source ~/catkin_ws/devel/setup.bash
cd ~/catkin_ws/src/racecar/racecar/scripts
#source rosenv.sh 192.168.1.98 192.168.1.228
#source rosenv.sh 192.168.1.247 192.168.1.247
source rosenv.sh 192.168.5.227 192.168.5.227
#source rosenv.sh 192.168.5.136 192.168.5.136
roslaunch racecar teleop_cli.launch

