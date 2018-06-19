sudo modprobe kvaser_usb
sudo modprobe vcan

sudo ip link add dev can0 type can bitrate 250000
#sudo ip link set can0 type can bitrate 250000
sudo ip link set can0 up
sudo ip link add dev vcan0 type vcan
sudo ip link set vcan0 up
