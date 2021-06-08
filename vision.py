from cscore import *
import cv2
import numpy as np

camWidth = 1280
camHeight = 960

cs = CameraServer.getInstance()
cs.enableLogging()

camera = cs.startAutomaticCapture()
camera.setResolution(camWidth, camHeight)

sink = cs.getVideo()

while True:
   time, input_img 

   if time == 0: # There is an error
      continue