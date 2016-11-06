import RPi.GPIO as GPIO
import time

leftPwr = 0
rightPwr = 0


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

try:
    while True:

        if (int(leftPwr) > 0):
            bw1.ChangeDutyCycle(0)
            fw1.ChangeDutyCycle(float(leftPwr))
        else:
            fw1.ChangeDutyCycle(0)
            bw1.ChangeDutyCycle(-1 * float(leftPwr))


        if (int(rightPwr) > 0):
            bw2.ChangeDutyCycle(0)
            fw2.ChangeDutyCycle(float(rightPwr))
        else:
            fw2.ChangeDutyCycle(0)
            bw2.ChangeDutyCycle(-1 * float(rightPwr))
        
        time.sleep(0.02)

except KeyboardInterrupt:
    pass

fw1.stop()
bw1.stop()
fw2.stop()
bw2.stop()

GPIO.cleanup()
