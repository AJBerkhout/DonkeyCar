#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publisher():

    pub = rospy.Publisher('string_publish', String, queue_size=10)

    #rate of message publishing in Hertz
    rate = rospy.Rate(1)

    msg_to_publish = String()

    counter = 0

    #runs as long as ros is running
    while not rospy.is_shutdown():
        string_to_publish = "Published count is %d"%counter
        counter += 1

        #writes the string to the message
        msg_to_publish.data = string_to_publish
        
        pub.publish(msg_to_publish)

        #serves as a print statement, outputs the message
        rospy.loginfo(string_to_publish)

        #waits for the time based on the rate
        rate.sleep()

if __name__ == "__main__":
    
    #creates a ros node called simple publisher
    rospy.init_node("simple_publisher")
    publisher()



    