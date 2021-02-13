import RPi.GPIO as GPIO
from ISStreamer.Streamer import Streamer
from time import sleep

ACCESS_KEY = "ist_qKI-afoTgpg8HUGD3eY_mnAlB1tmcuhk"
BUCKET_KEY = "BAWCM9RFDKDF"
BUCKET_NAME = "test initial state"

# create a Streamer instance
streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)

channel = 11
GPIO.setmode(GPIO.BOARD) # This sets the board numbering scheme (channel 17 for BCM)
GPIO.setup(channel, GPIO.IN) # We are saying that the channel is an input

def callback(channel):
    if GPIO.input(channel):
        print("No water detected\n")
        print("Sending to Initial State\n")
        myString = "No water detected"
        streamer.log("Message",myString)
        streamer.flush()
        print("Sent to IS\n")
    else:
        print("Water detected!\n")
        print("Sending to Initial State\n")
        myString = "Water detected!"
        streamer.log("Message",myString)
        streamer.flush()
        print("Sent to IS\n")

GPIO.add_event_detect(channel,GPIO.BOTH,bouncetime=300) # goes in a loop to determine changes in the edge
GPIO.add_event_callback(channel,callback) # Adds a function to call when the event detect is called - this one is good because it won't miss a change in state
print("Before entering the loop")
while True:
    sleep(1)

# It is a good idea to use GPIO.cleanup(channel) after the program is done
