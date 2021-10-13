# -*- coding:utf-8 -*-
'''!
  @file touch.ino
  @brief detect the touch status of 5 electric fields (up, down, left, right, center), which can be: touch, click and double click
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
    initialization function, return 0 if initialization succeeds, and return other numbers if initialization fails
  '''
  while(myGesture.begin()!= True):
    print("Begin err!!! Please check whether the connection is correct")
  print("begin success")

  '''
    enable touch detection function, returning -1 means the setup fails, and 0 means the setup succeeds
  '''
  while(myGesture.enable_touch_detection()!=0):
    print("enable gestures err")
  print("enable gestures success")

def loop():
  '''
    get the sensor data
  '''
  myGesture.sensor_data_recv()

  '''
    get touch data
    touch data:
              DOUBLE_TAP_CENTER/DOUBLE_TAP_RIGHT/DOUBLE_TAP_UP/DOUBLE_TAP_LEFT/DOUBLE_TAP_DOWN
              TAP_CENTER/TAP_RIGHT/TAP_UP/TAP_LEFT/TAP_DOWN
              TPUCH_CENTER/TOUCH_RIGHT/TOUCH_UP/TOUCH_LEFT/TOUCH_DOWN
  '''
  info = myGesture.get_touch_info()
  if(info & myGesture.DOUBLE_TAP_CENTER):
    print("Double Tap Center electrode")
  elif(info & myGesture.DOUBLE_TAP_RIGHT):
    print("Double Tap Right electrode")
  elif(info & myGesture.DOUBLE_TAP_UP):
    print("Double Tap Up electrode")
  elif(info & myGesture.DOUBLE_TAP_LEFT):
    print("Double Tap Left electrode")
  elif(info & myGesture.DOUBLE_TAP_DOWN):
    print("Double Tap Down electrode")
  elif(info & myGesture.TAP_CENTER):
    print("Tap Center electrode")
  elif(info & myGesture.TAP_RIGHT):
    print("Tap Right electrode")
  elif(info & myGesture.TAP_UP):
    print("Tap Up electrode")
  elif(info & myGesture.TAP_LEFT):
    print("Tap Left electrode")
  elif(info & myGesture.TAP_DOWN):
    print("Tap Down electrode")
  elif(info & myGesture.TPUCH_CENTER):
    print("Touch Center electrode")
  elif(info & myGesture.TOUCH_RIGHT):
    print("Touch Right electrode")
  elif(info & myGesture.TOUCH_UP):
    print("Touch Up electrode")
  elif(info & myGesture.TOUCH_LEFT):
    print("Touch Left electrode")
  elif(info & myGesture.TOUCH_DOWN):
    print("Touch Down electrode")


if __name__ == "__main__":
  setup()
  while True:
    loop()
