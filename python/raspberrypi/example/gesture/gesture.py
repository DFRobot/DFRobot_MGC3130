# -*- coding:utf-8 -*-
'''!
  @file gesture.ino
  @brief gesture recognition, which can be up-->down ,down-->up ,left-->right ,right-->left,Circle clockwise,Circle counterclockwise.
  @copyright Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license The MIT License (MIT)
  @author [yangfeng]<feng.yang@dfrobot.com>
  @version V1.0
  @date 2021-09-18
  @url  https://github.com/DFRobot/DFRobot_MGC3130
'''
import sys
sys.path.append("../../") # set system path to top
import time
from DFRobot_MGC3130 import *
import RPi.GPIO as GPIO

# IO numbering is in BCM format
myGesture = DFRobot_MGC3130(d_pin=20,mclr_pin = 21,bus = 1)

def setup():
  '''
    initialization function, return true if initialization succeeds, false if initialization fails
  '''
  while(myGesture.begin()!= True):
    print("Begin err!!! Please check whether the connection is correct")
  print("begin success")

  '''
     turn off gesture recognition function, returning -1 means the setup fails, and 0 means the setup succeeds
  '''
  while(myGesture.enable_gestures()!=0):
    print("enable gestures err")
  print("enable gestures success")

def loop():

  '''
    get the sensor data
  '''
  myGesture.sensor_data_recv()

  '''
    gesture information: FILCK_R/FILCK_L/FILCK_U/FILCK_D/CIRCLE_CLOCKWISE/CIRCLE_COUNTERCLOCKWISE
  '''
  info = myGesture.get_gesture_info()
  if(info == myGesture.FILCK_R):
    print("Flick Left to Right")
  elif(info == myGesture.FILCK_L):
    print("Flick Right to Left")
  elif(info == myGesture.FILCK_U):
    print("Flick Down to Up")
  elif(info == myGesture.FILCK_D):
    print("Flick Up to Down")
  elif(info == myGesture.CIRCLE_CLOCKWISE):
    print("Circle clockwise")
  elif(info == myGesture.CIRCLE_COUNTERCLOCKWISE):
    print("Circle counterclockwise")

if __name__ == "__main__":
  setup()
  while True:
    loop()
