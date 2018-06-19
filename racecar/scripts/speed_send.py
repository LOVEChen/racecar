#!/usr/bin/env python

import rospy
from std_msgs.msg import String 
from sensor_msgs.msg import Joy
from std_msgs.msg import Float64 
import can
import cantools
from joy_feedback_ros.msg import FFset


db = cantools.db.load_file('J7.dbc')
msg=db.get_message_by_name('ECU1')
vehspd_msg = db.get_message_by_name('CCVS')
gear_msg = db.get_message_by_name('ECU6')

can.rc['interface'] = 'socketcan_ctypes'
can.rc['channel'] = 'can0'
can_bus = can.interface.Bus()

def callback(speed):
#	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
#	rospy.loginfo("axis: %f,%f,%f", data.axes[0], data.axes[1], data.axes[2] )
	#d = msg.encode({'S_EngineSpeed': 1500})

	rpm = speed.data/5.0
	d = msg.encode({'S_EngineSpeed': abs(rpm)})
 	send_msg = can.Message(arbitration_id=msg.frame_id, data=d)
	can_bus.send(send_msg)

	vehspd = speed.data/100
        d = vehspd_msg.encode({'CCVS_SPEED': abs(vehspd)})
        send_msg = can.Message(arbitration_id=vehspd_msg.frame_id, data=d)
        can_bus.send(send_msg)

        gear = 1
        d = gear_msg.encode({'S_AM': gear})
        send_msg = can.Message(arbitration_id=gear_msg.frame_id, data=d)
        can_bus.send(send_msg)


	# pub ffset value from vehspd
	ff1 = abs(vehspd/4)
	ff2 = 30 + abs(vehspd*5/3)
	if ff1 > 100:
		ff1 = 100
	if ff2 > 100:
		ff2 = 100
	pub = rospy.Publisher('/ffset', FFset, queue_size=10)
	pub.publish(ff1, ff2)
	
	#rospy.loginfo(data) 
	rospy.loginfo("rpm: %f, veh:%f, ffset: %d %d",rpm, vehspd, ff1, ff2)



def listener():
	rospy.loginfo("Hey I am here")
	rospy.init_node('listener', anonymous=True)

	rospy.Subscriber("/vesc/commands/motor/speed", Float64, callback)  
	#rospy.Subscriber("/vesc/joy", Joy, callback)  

	
	rospy.spin()  
if __name__ == '__main__':
	listener()







