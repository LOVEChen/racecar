#Enviroment Setup
source  ~/catkin_ws/devel/setup.bash 

if [ $# -lt 2 ];
then
   echo -e "\n Usage: `basename $0` ROS_MASTER_IP ROS_CLIENT_IP"
else
   export ROS_MASTER_URI="http://$1:11311"
   export ROS_IP="$2"
   printenv | grep ROS
fi
#export ROS_MASTER_URI="http://192.168.1.213:11311"
#export ROS_IP="192.168.1.229"
#launch usb_cam view.launch

