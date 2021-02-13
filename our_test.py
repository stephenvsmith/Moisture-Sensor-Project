import RPi.GPIO as GPIO
import time

channel = 11
GPIO.setmode(GPIO.BOARD) # This sets the board numbering scheme (channel 17 for BCM)
GPIO.setup(channel, GPIO.IN) # We are saying that the channel is an input

def callback(channel):
    if GPIO.input(channel):
        print("No water detected\n")
    else:
        print("Water detected!\n")

GPIO.add_event_detect(channel,GPIO.BOTH,bouncetime=300) # goes in a loop to determine changes in the edge
GPIO.add_event_callback(channel,callback) # Adds a function to call when the event detect is called - this one is good because it won't miss a change in state
print("Before entering the loop")
while True:
   time.sleep(10)

# It is a good idea to use GPIO.cleanup(channel) after the program is done
