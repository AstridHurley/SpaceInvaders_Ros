import rospy
import random
from std_msgs.msg import Int32

#funcion
def talker():
	pub = rospy.Publisher('chatter', Int32, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(0.1) #0.2Hz=5seg
	while not rospy.is_shutdown():
		num_str = (random.randrange(10)) % rospy.get_time()
		rospy.loginfo(num_str)
		pub.publish(num_str)
		rate.sleep()
	print("Reward ",rew)	
if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass


