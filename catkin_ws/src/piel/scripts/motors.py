#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import rospy
from std_msgs.msg import String


GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

fw1 = GPIO.PWM(7, 50)
bw1 = GPIO.PWM(11, 50)
fw2 = GPIO.PWM(13, 50)
bw2 = GPIO.PWM(16, 50)

fw1.start(0)
bw1.start(0)
fw2.start(0)
bw2.start(0)


def callback(data):
    #rospy.loginfo(data.data)
    pwrSet = data.data.split("+")
    leftPwr = pwrSet[0]
    rightPwr = pwrSet[1]
    rospy.loginfo(leftPwr)
    
    if (int(leftPwr) > 0 and int(leftPwr) <= 100):
        bw1.ChangeDutyCycle(0)
        fw1.ChangeDutyCycle(float(leftPwr))
    elif (int(leftPwr) >= -100):
        fw1.ChangeDutyCycle(0)
        bw1.ChangeDutyCycle(-1 * float(leftPwr))


    if (int(rightPwr) > 0 and int(rightPwr) <= 100):
        bw2.ChangeDutyCycle(0)
        fw2.ChangeDutyCycle(float(rightPwr))
    elif (int(rightPwr) >= -100):
        fw2.ChangeDutyCycle(0)
        bw2.ChangeDutyCycle(-1 * float(rightPwr))
            

    
def listener():
    rospy.init_node('motors', anonymous=True)

    rospy.Subscriber("commands", String, callback)
    
    rospy.spin()
    
if __name__ == '__main__':
    listener()

fw1.stop()
bw1.stop()
fw2.stop()
bw2.stop()

GPIO.cleanup()