from picamera import PiCamera, Color
from time import sleep
from subprocess import call

camera = PiCamera()

#sleep(3)
#camera.capture('/home/pi/Desktop/python_test_image.jpg')

file_h264 = "new_test.h264"
file_mp4 = "new_testmp4.mp4"

camera.start_recording(file_h264)
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text = "Yoooooooooo"
sleep(5)
camera.stop_recording()

command = "MP4Box -add " + file_h264 + " " + file_mp4
call([command], shell=True)


