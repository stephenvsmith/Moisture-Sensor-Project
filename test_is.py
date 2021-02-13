from ISStreamer.Streamer import Streamer
from time import sleep

ACCESS_KEY = "ist_qKI-afoTgpg8HUGD3eY_mnAlB1tmcuhk"
BUCKET_KEY = "BAWCM9RFDKDF"
BUCKET_NAME = "test initial state"

# create a Streamer instance
streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)

# send some data
for i in range(20):
    myString = "This is message #%d" % i
    streamer.log("Message",myString)
    sleep(3) 

# flush and close the stream
streamer.flush()
