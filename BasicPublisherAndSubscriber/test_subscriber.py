#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def subscriber():

    #create a new subscriber with a topic of string_publish and
    #with a message type of String, and a callback_function that
    #has a parameter, the message, that gets run anytime the subscriber recieves a message
    sub = rospy.Subscriber('string_publish', String, callback_function)

    #run like an infinite while loop
    rospy.spin()

def callback_function(message):
    #prints out the string recieved in the messages data
    rospy.loginfo("I received %s"%message.data)

if __name__ == "__main__":
    rospy.init_node("simple_subscriber")
    subscriber()