import RPi.GPIO as GPIO
import time
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
        f = open("data.txt", "r")
        data = f.read().split('+')
        print(data)

        if (data != [""] and abs(int(data[0])) <= 100 and abs(int(data[1])) <= 100):

            if (int(data[0]) > 0):
                bw1.ChangeDutyCycle(0)
                fw1.ChangeDutyCycle(float(data[0]))
            else:
                fw1.ChangeDutyCycle(0)
                bw1.ChangeDutyCycle(-1 * float(data[0]))
            

            if (int(data[1]) > 0):
                bw2.ChangeDutyCycle(0)
                fw2.ChangeDutyCycle(float(data[1]))
            else:
                fw2.ChangeDutyCycle(0)
                bw2.ChangeDutyCycle(-1 * float(data[1]))
        
        time.sleep(0.02)

except KeyboardInterrupt:
    pass

fw1.stop()
bw1.stop()
fw2.stop()
bw2.stop()

GPIO.cleanup()
