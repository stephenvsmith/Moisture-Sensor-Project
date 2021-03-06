import RPi.GPIO as GPIO
from time import sleep

channel_out = 8
channel_in = 10
channel_led_out = 12
GPIO.setmode(GPIO.BOARD) # This sets the board numbering scheme (channel 17 for BCM)
GPIO.setup(channel_out, GPIO.OUT) # We are saying that the channel is an output
GPIO.setup(channel_in,GPIO.IN) # We are saying that the channel is an input
GPIO.setup(channel_led_out,GPIO.OUT)

GPIO.output(channel_out,1)
for i in range(100):
    if GPIO.input(channel_in)==1:
        GPIO.output(channel_led_out,1)
        sleep(1)
    else:
        GPIO.output(channel_led_out,0) 
        sleep(0.2)

GPIO.cleanup()
# It is a good idea to use GPIO.cleanup(channel) after the program is done
print("Program is now over.\n")
