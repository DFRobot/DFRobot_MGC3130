# DFRobot_MGC3130

- [中文版](./README_CN.md)

The DFRobot 3D gesture sensor is an interactive sensor that integrates 3D gesture recognition and motion tracking. This sensor can be used to detect clockwise/counterclockwise rotation and movement directions. It is based on Microchip patent GestIC® technology with electric near field sensing technology, including 3D gesture input sensing system and advanced 3D signal processing unit. And its effective detection range is 0-10cm.



![](../../resources/images/SEN0202.jpg)


## Product Link(https://www.dfrobot.com/product-1538.html)

    SKU：SEN0202

## Table of Contents

* [Summary](#summary)
* [Installation](#installation)
* [Methods](#methods)
* [Compatibility](#compatibility)
* [History](#history)
* [Credits](#credits)

## Summary

The library provides three samples: gesture recognition, touch recognition and proximity position detection.

Gesture recognition: left --> right, right --> left, up --> down, down --> up

Touch recognition: single-click, double-click or touch the up, down, left, right or center key

Proximity position recognition: position data in the X, Y and Z axes

## Installation

Before use, first download the library file, paste it into your Raspberry Pi's custom directory, then open the examples folder and run the demo in that folder.

## Methods

```python
  def begin(self):
    '''!
      @brief initialization function
      @return returns the initialization status
      @retval True Initialization succeeded
      @retval False Initialization succeeded
    '''

  def reset(self):
    '''!
      @brief reset the sensor
    '''

  def enable_touch_detection(self):
    '''!
      @brief enable touch detection function
      @return Result of enabling touch detection function
      @retval -1  setup fails
      @retval  0  setup succeeds
    '''

  def disable_touch_detection(self):
    '''!
      @brief turn off touch detection function
      @return Result of disabling touch detection function
      @retval -1  setup fails
      @retval  0  setup succeeds
    '''

  def enable_approach_detection(self):
    '''!
      @brief enable proximity detection function
      @return Result of enabling proximity detection function
      @retval -1  setup fails
      @retval  0  setup succeeds
    '''

  def disable_approach_detection(self):
    '''!
      @brief turn off proximity detection function
      @return Result of disabling proximity detection function
      @retval -1  setup fails
      @retval  0  setup succeeds
    '''

  def enable_air_wheel(self):
    '''!
      @brief enable AirWheel function
      @return Result of enabling AirWheel function
      @retval -1  setup fails
      @retval  0  setup succeeds
    '''

  def disable_air_wheel(self):
    '''!
      @brief turn off gesture recognition function
      @return Result of disabling AirWheel function
      @retval -1  setup fails
      @retval  0  setup succeeds
    '''

  def enable_gestures(self):
    '''!
      @brief enable gesture recognition function
      @return Result of enabling gesture recognition function
      @retval -1  setup fails
      @retval  0  setup succeeds
    '''

  def disable_gestures(self):
    '''!
      @brief turn off gesture recognition function
      @return Result of disabling gesture recognition function
      @retval -1  setup fails
      @retval  0  setup succeeds
    '''

  def get_x_position(self):
    '''!
      @brief get the X-axis position
      @return X-axis position
    '''

  def get_y_position(self):
    '''!
      @brief get the Y-axis position
      @return Y-axis position
    '''

  def get_z_position(self):
    '''!
      @brief get the Z-axis position
      @return Z-axis position
    '''

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

  def have_position_info(self):
    '''!
      @brief monitor position information
      @return Results of monitoring position information
      @retval true  position information exists
      @retval false There is no position information
    '''

  def sensor_data_recv(self):
    '''!
      @brief get the sensor data
    '''
```

## Compatibility

* RaspberryPi Version

| Board        | Work Well | Work Wrong | Untested | Remarks |
| ------------ | :-------: | :--------: | :------: | ------- |
| RaspberryPi2 |           |            |    √     |         |
| RaspberryPi3 |     √     |            |          |         |
| RaspberryPi4 |           |            |    √     |         |

* Python Version

| Python  | Work Well | Work Wrong | Untested | Remarks |
| ------- | :-------: | :--------: | :------: | ------- |
| Python2 |     √     |            |          |         |
| Python3 |     √     |            |          |         |


## History

- 2021/10/13 - Version 1.0.0 released.


## Credits

Written by yangfeng(feng.yang@dfrobot.com), 2021. (Welcome to our [website](https://www.dfrobot.com/))

