# DFRobot_MGC3130

- [中文版](./README_CN.md)

The DFRobot 3D gesture sensor is an interactive sensor that integrates 3D gesture recognition and motion tracking. This sensor can be used to detect clockwise/counterclockwise rotation and movement directions. It is based on Microchip patent GestIC® technology with electric near field sensing technology, including 3D gesture input sensing system and advanced 3D signal processing unit. And its effective detection range is 0-10cm.



![](./resources/images/SEN0202.jpg)


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

The library provides three samples: gesture recognition, touch recognition and proximity position monitoring

Gesture recognition: left --> right, right --> left, up --> down, down --> up

Touch recognition: single-click, double-click or touch the up, down, left, right or center key

Proximity position recognition: position data in the X, Y and Z axes

## Installation

There are two ways to use the library:
1. Open the Arduino IDE, search for "DFRobot_MGC3130" in Tools --> Manager Libraries on the status bar, and install the library.
2. First download the library file, paste it into the \Arduino\libraries directory, then open the examples folder and run the demo in that folder.

## Methods

```C++
  /**
   * @fn begin
   * @brief initialization function
   * @return bool,returns the initialization status
   * @retval true Initialization succeeded
   * @retval fasle Initialization  failed
   */
  bool begin(void);

  /**
   * @fn reset
   * @brief reset the sensor
   */
  void reset(void);

  /**
   * @fn sensorDataRecv
   * @brief get the sensor data
   */
  void sensorDataRecv(void);

  /**
   * @fn enableGestures
   * @brief enable gesture recognition function
   * @return Result of enabling gesture recognition
   * @retval -1  setup fails
   * @retval  0  setup succeeds
   */
  int8_t enableGestures(void);

  /**
   * @fn disableGestures
   * @brief turn off gesture recognition function
   * @return Result of disabling gesture recognition
   * @retval -1  setup fails
   * @retval  0  setup succeeds
   */
  int8_t disableGestures(void);

  /**
   * @fn disableAirWheel
   * @brief turn off AirWheel function
   * @return Result of disabling AirWheel function
   * @retval -1  setup fails
   * @retval  0  setup succeeds
   */
  int8_t disableAirWheel(void);

  /**
   * @fn enableAirWheel
   * @brief enable AirWheel function
   * @return Result of enabling AirWheel function
   * @retval -1  setup fails
   * @retval  0  setup succeeds
   */
  int8_t enableAirWheel(void);

  /**
   * @fn disableApproachDetection
   * @brief turn off proximity detection function
   * @return Result of disabling proximity detection function
   * @retval -1  setup fails
   * @retval  0  setup succeeds
   */
  int8_t disableApproachDetection(void);

  /**
   * @fn enableApproachDetection
   * @brief enable proximity detection function
   * @return Result of enabling proximity detection function
   * @retval -1  setup fails
   * @retval  0  setup succeeds
   */
  int8_t enableApproachDetection(void);

  /**
   * @fn disableTouchDetection
   * @brief turn off touch detection function
   * @return Result of disabling touch detection function
   * @retval -1  setup fails
   * @retval  0  setup succeeds
   */
  int8_t disableTouchDetection(void);

  /**
   * @fn enableTouchDetection
   * @brief enable touch detection function
   * @return Result of enabling touch detection function
   * @retval -1  setup fails
   * @retval  0  setup succeeds
   */
  int8_t enableTouchDetection(void);

  /**
   * @fn getPositionX
   * @brief get the X-axis position
   * @return X-axis position
   */
  uint16_t getPositionX(void);

  /**
   * @fn getPositionY
   * @brief get the Y-axis position
   * @return Y-axis position
   */
  uint16_t getPositionY(void);

  /**
   * @fn getPositionZ
   * @brief get the Z-axis position
   * @return Z-axis position
   */
  uint16_t getPositionZ(void);

  /**
   * @fn getTouchInfo
   * @brief get touch information
   * @return touch information
   * @retval eDoubleTapCenter  Double Tap Center electrode
   * @retval eDoubleTapRight   Double Tap Right electrode
   * @retval eDoubleTapUp      Double Tap Up electrode
   * @retval eDoubleTapLeft    Double Tap Left electrode
   * @retval eDoubleTapDown    Double Tap Down electrode
   * @retval eTapCenter        Tap Center electrode
   * @retval eTapRight         Tap Right electrode
   * @retval eTapUp            Tap Up electrode
   * @retval eTapLeft          Tap Left electrode
   * @retval eTapDown          Tap Down electrode
   * @retval eTouchCenter      Touch Center electrode
   * @retval eTouchRight       Touch Right electrode
   * @retval eTouchUp          Touch Up electrode
   * @retval eTouchLeft        Touch Left electrode
   * @retval eTouchDown        Touch Down electrode
   */
  uint16_t getTouchInfo(void);

  /**
   * @fn getGestureInfo
   * @brief get gesture information
   * @return gesture information
   * @retval eFilckR                   Flick Left to Right
   * @retval eFilckL                   Flick Right to Left
   * @retval eFilckU                   Flick Down to Up
   * @retval eFilckD                   Flick Up to Down
   * @retval eCircleClockwise          Circle clockwise (only active if AirWheel disabled)
   * @retval eCircleCounterclockwise   Circle counterclockwise (only active if AirWheel disabled)
   */
  uint8_t getGestureInfo(void);

  /**
   * @fn havePositionInfo
   * @brief monitor position information
   * @return Results of monitoring position information
   * @retval true  position information exists
   * @retval false There is no position information
   */
  bool havePositionInfo(void);
```

## Compatibility

| Board         | Work Well | Work Wrong | Untested | Remarks |
| ------------- | :-------: | :--------: | :------: | ------- |
| Arduino uno   |     √     |            |          |         |
| Mega2560      |     √     |            |          |         |
| Leonardo      |     √     |            |          |         |
| ESP32         |     √     |            |          |         |
| micro:bit     |     √     |            |          |         |
| FireBeetle M0 |     √     |            |          |         |


## History

- 2021/10/13 - Version 1.0.0 released.


## Credits

Written by yangfeng(feng.yang@dfrobot.com), 2021. (Welcome to our [website](https://www.dfrobot.com/))

