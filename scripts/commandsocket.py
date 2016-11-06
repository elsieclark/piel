import RPi.GPIO as GPIO
import time

from socketIO_client import SocketIO, LoggingNamespace
socketIO = SocketIO('localhost:3000')

def onCommand(*args):
    print(args[0])

while (True):
    socketIO.on("commands", onCommand)
    socketIO.wait(seconds=1)
    socketIO.off("sequencePi")