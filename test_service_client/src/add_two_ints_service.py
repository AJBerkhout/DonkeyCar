#!/usr/bin/env python

from __future__ import print_function

#imports the services defined in our package
#services were created by copying a tutorial one
#and adding it to services in cmakelist
from test_service_client.srv import AddTwoInts, AddTwoIntsResponse

import rospy

#logic for handling the request
#takes the requests and sums the a and b parameters
#then uses the response to send the sum back
def handle_add_two_ints(req):
    print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
    return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')

    #creates a service called add_two_ints
    #uses the AddTwoInts service type defined in our catkin package
    #uses the handler function, which accepts a 'request' of the service type
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print("Ready to add two ints.")

    #runs like an infinite  loop
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()

    
