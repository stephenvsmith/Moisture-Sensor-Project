import RPi.GPIO as GPIO
from time import sleep

channel = 8
GPIO.setmode(GPIO.BOARD) # This sets the board numbering scheme (channel 17 for BCM)
GPIO.setup(channel, GPIO.OUT) # We are saying that the channel is an output

for i in range(10):
    GPIO.output(channel,1)
    sleep(2.2)
    GPIO.output(channel,GPIO.LOW)
    sleep(0.2)
GPIO.cleanup()
# It is a good idea to use GPIO.cleanup(channel) after the program is done
