#!/usr/bin/env python
import time
import rospy
import threading
from std_msgs.msg import String
from socketIO_client import SocketIO, LoggingNamespace


socketIO = SocketIO('localhost:3000')

commands = "0+0"

def onCommand(*args):
    global commands
    commands = args[0]
    
class SocketThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
            socketIO.on("commands", onCommand)           
            socketIO.wait()

socketThread = SocketThread("socketThread")
socketThread.start()

def talker():
    global commands
    pub = rospy.Publisher('commands', String, queue_size=10)
    rospy.init_node('commandsocket', anonymous=True)
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        rospy.loginfo(commands)
        pub.publish(commands)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    
    
socketThread.join()