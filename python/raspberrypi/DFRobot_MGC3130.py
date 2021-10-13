# -*- coding:utf-8 -*-
'''！
  @file DFRobot_MGC3130.py
  @brief DFRobot_MGC3130 class infrastructure, the implementation of basic methods
  @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license     The MIT License (MIT)
  @author     [yangfeng](feng.yang@dfrobot.com)
  @version  V1.0
  @date  2021-09-18
  @url https://github.com/DFRobot/DFRobot_MGC3130
'''
import sys
import smbus
import logging
import numpy as np
from ctypes import *
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

logger = logging.getLogger()
logger.setLevel(logging.INFO)  #display all the printed information
#logger.setLevel(logging.FATAL)#use this option if you don't want to display too many prints and just print errors
ph = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - [%(filename)s %(funcName)s]:%(lineno)d - %(levelname)s: %(message)s")
ph.setFormatter(formatter) 
logger.addHandler(ph)

DFRobot_MGC3130_IIC_ADDR = 0x42

class DFRobot_MGC3130(object):
  '''!
    @brief DFRobot_MGC3130 implements gesture recognition, touch recognition, and approach recognition.
  '''

  def __init__(self,d_pin,mclr_pin,bus = 1):
    '''!
      @brief   __init__
      @param d_pin Transfer Status Line
      @param mclr_pin reset pin
      @param bus  IIC Bus
    '''
    self.now_touch                    = 0
    self.last_touch                   = 0
    self.gesture_info                 = 0
    self.touch_info                   = 0
    self.air_wheel_info               = 0
    self.x_position                   = 0
    self.y_position                   = 0
    self.z_position                   = 0
    self.NOERROR                      = 0x0000
    self.UNKONWN_COMMAND              = 0x0001
    self.WRONG_PARAMETER_VALUE        = 0x0014
    self.UNKNOWN_PARAMETER_ID         = 0x0015
    self.WAKEUP_HAPPEND               = 0x001A
    self.NO_GESTURE                   = 0
    self.GARBAGE_MODEL                = 1
    self.FILCK_R                      = 2
    self.FILCK_L                      = 3
    self.FILCK_U                      = 4
    self.FILCK_D                      = 5
    self.CIRCLE_CLOCKWISE             = 6
    self.CIRCLE_COUNTERCLOCKWISE      = 7
    self.TOUCH_DOWN                   = 1
    self.TOUCH_LEFT                   = 2
    self.TOUCH_UP                     = 4
    self.TOUCH_RIGHT                  = 8
    self.TPUCH_CENTER                 = 16
    self.TAP_DOWN                     = 32
    self.TAP_LEFT                     = 64
    self.TAP_UP                       = 128
    self.TAP_RIGHT                    = 256
    self.TAP_CENTER                   = 512
    self.DOUBLE_TAP_DOWN              = 1024
    self.DOUBLE_TAP_LEFT              = 2048
    self.DOUBLE_TAP_UP                = 4096
    self.DOUBLE_TAP_RIGHT             = 8192
    self.DOUBLE_TAP_CENTER            = 16384
    self._ts_pin = d_pin
    self._reset_pin = mclr_pin
    self.position = False
    self.last_time_stamp = 0
    self.now_time_stamp = 0
    self.i2cbus=smbus.SMBus(bus)
    self.i2c_addr = DFRobot_MGC3130_IIC_ADDR

  def begin(self):
    '''!
      @brief initialization function
      @return bool,returns the initialization status
      @retval True Initialization succeeded
      @retval False Initialization succeeded
    '''
    ret = False
    self._ts_input()
    self.reset()
    while(self.disable_touch_detection()!=0):
      ret = True
    while(self.disable_approach_detection()!=0):
      ret = True
    while(self.disable_air_wheel()!=0):
      ret = True
    while(self.disable_gestures()!=0):
      ret = True
    while(self._enable_data_output()!=0):
      ret = True
    while(self._lock_data_output()!=0):
      ret = True
    return ret

  def reset(self):
    '''!
      @brief reset the sensor
    '''
    GPIO.setup(self._reset_pin, GPIO.OUT)
    GPIO.output(self._reset_pin, GPIO.LOW)
    time.sleep(0.25)
    GPIO.output(self._reset_pin, GPIO.HIGH)
    time.sleep(2)

  def enable_touch_detection(self):
    '''!
      @brief enable touch detection function
      @return Result of enabling touch detection function
      @retval -1  setup fails
      @retval  0  setup succeeds
    '''
    ret = -1
    buf=[0x00,0x00,0xA2,0x97,0x00,0x00,0x00,0x08,0x00,0x00,0x00,0x08,0x00,0x00,0x00]
    recv_buf=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    self._set_runtime_parameter(buf,16)
    recv_buf = self._read(16)
    if(recv_buf != 0):
      if(recv_buf[4] == 0xA2):
        ret = recv_buf[7]>>8 | recv_buf[6]
    return ret

  def disable_touch_detection(self):
    '''!
      @brief turn off touch detection function
      @return Result of disabling touch detection function
      @retval -1  setup fails
      @retval  0  setup succeeds
    '''
    ret = -1
    buf=[0x00,0x00,0xA2,0x97,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x08,0x00,0x00,0x00]
    recv_buf=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    self._set_runtime_parameter(buf,16)
    recv_buf = self._read(16)
    if(recv_buf != 0):
      if(recv_buf[4] == 0xA2):
        ret = recv_buf[7]>>8 | recv_buf[6]
    return ret

  def enable_approach_detection(self):
    '''!
      @brief enable proximity detection function
      @return Result of enabling proximity detection function
      @retval -1  setup fails
      @retval  0  setup succeeds
    '''
    ret = -1
    buf=[0x00,0x00,0xA2,0x97,0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x01,0x00,0x00,0x00]
    recv_buf=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    self._set_runtime_parameter(buf,16)
    recv_buf = self._read(16)
    if(recv_buf != 0):
      if(recv_buf[4] == 0xA2):
        ret = recv_buf[7]>>8 | recv_buf[6]
    return ret

  def disable_approach_detection(self):
    '''!
      @brief turn off proximity detection function
      @return Result of disabling proximity detection function
      @retval -1  setup fails
      @retval  0  setup succeeds
    '''
    ret = -1
    buf=[0x00,0x00,0xA2,0x97,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x01,0x00,0x00,0x00]
    recv_buf=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    self._set_runtime_parameter(buf,16)
    recv_buf = self._read(16)
    if(recv_buf != 0):
      if(recv_buf[4] == 0xA2):
        ret = recv_buf[7]>>8 | recv_buf[6]
    return ret


  def enable_air_wheel(self):
    '''!
      @brief enable AirWheel function
      @return Result of enabling AirWheel function
      @retval -1  setup fails
      @retval  0  setup succeeds
    '''
    ret = -1
    buf=[0x00,0x00,0xA2,0x90,0x00,0x00,0x00,0x20,0x00,0x00,0x00,0x20,0x00,0x00,0x00]
    recv_buf=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    self._set_runtime_parameter(buf,16)
    recv_buf = self._read(16)
    if(recv_buf != 0):
      if(recv_buf[4] == 0xA2):
        ret = recv_buf[7]>>8 | recv_buf[6]
    return ret

  def disable_air_wheel(self):
    '''!
      @brief turn off gesture recognition function
      @return Result of disabling AirWheel function
      @retval -1  setup fails
      @retval  0  setup succeeds
    '''
    ret = -1
    buf=[0x00,0x00,0xA2,0x90,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x20,0x00,0x00,0x00]
    recv_buf=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    self._set_runtime_parameter(buf,16)
    recv_buf = self._read(16)
    if(recv_buf != 0):
      if(recv_buf[4] == 0xA2):
        ret = recv_buf[7]>>8 | recv_buf[6]
    return ret


  def enable_gestures(self):
    '''!
      @brief enable gesture recognition function
      @return Result of enabling gesture recognition function
      @retval -1  setup fails
      @retval  0  setup succeeds
    '''
    ret = -1
    buf=[0x00,0x00,0xA2,0x85,0x00, 0x00,0x00, 0x7F,0x00,0x00,0x00, 0x7F,0x00,0x00,0x00]
    recv_buf=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    self._set_runtime_parameter(buf,16)
    recv_buf = self._read(16)
    if(recv_buf != 0):
      if(recv_buf[4] == 0xA2):
        ret = recv_buf[7]>>8 | recv_buf[6]
    return ret

  def disable_gestures(self):
    '''!
      @brief turn off gesture recognition function
      @return Result of disabling gesture recognition function
      @retval -1  setup fails
      @retval  0  setup succeeds
    '''
    ret = -1
    buf=[0x00,0x00,0xA2,0x85,0x00, 0x00,0x00, 0x00,0x00,0x00,0x00, 0x00,0x00,0x00,0x00]
    recv_buf=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    self._set_runtime_parameter(buf,16)
    recv_buf = self._read(16)
    if(recv_buf != 0):
      if(recv_buf[4] == 0xA2):
        ret = recv_buf[7]>>8 | recv_buf[6]
    return ret


  def get_x_position(self):
    '''!
      @brief get the X-axis position
      @return X-axis position
    '''
    return self.x_position


  def get_y_position(self):
    '''!
      @brief get the Y-axis position
      @return Y-axis position
    '''
    return self.y_position


  def get_z_position(self):
    '''!
      @brief get the Z-axis position
      @return Z-axis position
    '''
    return self.z_position

  def get_touch_info(self):
    '''!
      @brief get touch information
      @return touch information
      @retval DOUBLE_TAP_CENTER  Double Tap Center electrode
      @retval DOUBLE_TAP_RIGHT   Double Tap Right electrode
      @retval DOUBLE_TAP_UP      Double Tap Up electrode
      @retval DOUBLE_TAP_LEFT    Double Tap Left electrode
      @retval DOUBLE_TAP_DOWN    Double Tap Down electrode
      @retval TAP_CENTER        Tap Center electrode
      @retval TAP_RIGHT         Tap Right electrode
      @retval TAP_UP            Tap Up electrode
      @retval TAP_LEFT          Tap Left electrode
      @retval TAP_DOWN          Tap Down electrode
      @retval TPUCH_CENTER      Touch Center electrode
      @retval TOUCH_RIGHT       Touch Right electrode
      @retval TOUCH_UP          Touch Up electrode
      @retval TOUCH_LEFT        Touch Left electrode
      @retval TOUCH_DOWN        Touch Down electrode
    '''
    data = self.touch_info & 0xFFFF
    if(self.touch_info & 0x3E0):
      if((self.now_touch == self.last_touch) and (self.now_time_stamp == self.last_time_stamp)):
        data = self.touch_info & 0xFC1F
    if(self.touch_info & 0x7C00):
      if((self.now_touch == self.last_touch) and (self.now_time_stamp == self.last_time_stamp)):
        data = self.touch_info & 0x83FF
    self.last_touch  = self.now_touch
    self.last_time_stamp  = self.now_time_stamp
    return data

  def get_gesture_info(self):
    '''!
      @brief get gesture information
      @return gesture information
      @retval FILCK_R                   Flick Left to Right
      @retval FILCK_L                   Flick Right to Left
      @retval FILCK_U                   Flick Down to Up
      @retval FILCK_D                   Flick Up to Down
      @retval CIRCLE_CLOCKWISE          Circle clockwise (only active if AirWheel disabled)
      @retval CIRCLE_COUNTERCLOCKWISE   Circle counterclockwise (only active if AirWheel disabled)
    '''
    return self.gesture_info & 0xFF

  def have_position_info(self):
    '''!
      @brief monitor position information
      @return Results of monitoring position information
      @retval true  position information exists
      @retval false There is no position information
    '''
    return self.position


  def sensor_data_recv(self):
    '''!
      @brief get the sensor data
    '''
    self.position = False
    self.x_position = 0
    self.y_position = 0
    self.z_position = 0
    self.air_wheel_info = 0
    self.gesture_info = 0
    self.touch_info = 0
    buf=self._read(24)
    if(buf!=0):
      if((buf[3] == 0x91) and (buf[4] == 0x1E)):
        self.gesture_info = buf[8] | buf[9]<<8 | buf[10]<<16 | buf[11]<<24
        self.touch_info = buf[12] | buf[13]<<8 | buf[14]<<16 | buf[15]<<24
        self.now_time_stamp = buf[14] | buf[15]<<8
        self.now_touch = buf[12] | buf[13]<<8
        if(buf[7] & 0x02):
          self.air_wheel_info = buf[16] | buf[17]<<8
        if(buf[7] & 0x01):
          self.position = True
          self.x_position = buf[18] | buf[19]<<8
          self.y_position = buf[20] | buf[21]<<8
          self.z_position = buf[22] | buf[23]<<8
      elif(buf[4] == 0x1F):
        while(self._enable_data_output()!=0):
          ret = True
        while(self._lock_data_output()!=0):
          ret = True


  def _enable_data_output(self):
    '''!
      @brief set the output data format of the sensor
      @return Result of setting
      @retval -1  setup fails
      @retval  0  setup succeeds
    '''
    ret = -1
    buf=[0x00,0x00,0xA2,0xA0,0x00, 0x00,0x00, 0x1E,0x00,0x00,0x00, 0xFF,0xFF,0xFF,0xFF]
    recv_buf=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    self._set_runtime_parameter(buf,16)
    recv_buf = self._read(16)
    if(recv_buf != 0):
      if(recv_buf[4] == 0xA2):
        ret = recv_buf[7]>>8 | recv_buf[6]
    return ret

  def _lock_data_output(self):
    '''!
      @brief lock the output data format of the sensor
      @return Result of setting
      @retval -1  setup fails
      @retval  0  setup succeeds
    '''
    ret = -1
    buf=[0x00,0x00,0xA2,0xA1,0x00, 0x00,0x00, 0x1E,0x00,0x00,0x00, 0xFF,0xFF,0xFF,0xFF]
    recv_buf=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    self._set_runtime_parameter(buf,16)
    recv_buf = self._read(16)
    if(recv_buf != 0):
      if(recv_buf[4] == 0xA2):
        ret = recv_buf[7]>>8 | recv_buf[6]
    return ret


  def _ts_input(self):
    '''!
      @brief set the ts_pin of the master computer to the input mode(TS:transfer status line)
    '''
    GPIO.setup(self._ts_pin, GPIO.IN)


  def _ts_output(self):
    '''!
      @brief set the ts_pin of the master computer to the output mode(TS:transfer status line)
    '''
    GPIO.setup(self._ts_pin, GPIO.OUT)

  def _ts_write(self,mode):
    '''!
      @brief set the ts_pin of the master computer to the output status(TS:transfer status line)
      @param mode output status HIGH/LOW
      @n HIGH  Move the Transfer Status line higher
      @n LOW   Lower the Transfer Status line
    '''
    if(mode):
      GPIO.output(self._ts_pin, GPIO.HIGH)
    else:
      GPIO.output(self._ts_pin, GPIO.LOW)


  def _ts_read(self):
    '''!
      @brief get the status of transfer status line
      @return  return the status of transfer status line
      @retval HIGH
      @retval LOW
    '''
    return GPIO.input(self._ts_pin)


  def _set_runtime_parameter(self,buf,len):
    '''!
      @brief write the sensor IIC data
      @param pBuf write the store and buffer of the data
      @param size write the data length
      @return return the actually written length
    '''
    self.i2cbus.write_i2c_block_data(self.i2c_addr, 0x10, buf)

  def _read(self,len):
    '''!
      @brief get the sensor IIC data
      @param pBuf write the store and buffer of the data
      @param size write the data length
      @return return the actually written length, returning 0 means reading data fails
    '''
    #self._ts_input()
    if(self._ts_read() != 0):
      return 0
    self._ts_output()
    self._ts_write(0)
    data = self.i2cbus.read_i2c_block_data(self.i2c_addr, 0x00, len)
    self._ts_write(1)
    self._ts_input()
    time.sleep(0.05)
    return data

