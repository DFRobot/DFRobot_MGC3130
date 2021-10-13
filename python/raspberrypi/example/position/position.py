# -*- coding:utf-8 -*-
'''!
  @file position.ino
  @brief position recognition, data on X, Y and Z axes (zero at southwest position of touch plate, silkscreen at Down)
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
    turn off proximity detection function, returning -1 means the setup fails, and 0 means the setup succeeds
  '''
  while(myGesture.enable_approach_detection()!=0):
    print("enable approach detection err")
  print("enable approach detection success")

def loop():
  '''
    get the sensor data
  '''
  myGesture.sensor_data_recv()

  '''
    monitor position information, returning true means position information existed and false means not 
  '''
  if(myGesture.have_position_info()==True):
    print('X: =%d '%(myGesture.get_x_position()),' Y: =%d '%(myGesture.get_y_position()),'  Z: =%d '%(myGesture.get_z_position()))

if __name__ == "__main__":
  setup()
  while True:
    loop()
