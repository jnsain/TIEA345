import picamera
import time

camera = picamera.PiCamera()
camera.capture('demo3.jpg')

camera.start_recording('video.h264')
time.sleep(15)
camera.stop_recording()
