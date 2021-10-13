/*!
 * @file gesture.ino
 * @brief gesture recognition, it can be up-->down,down-->up,left-->right,right-->left,Circle clockwise,Circle counterclockwise.
 * @n Hardware Connections:
 * @n HOST Pin    SENSOR PIN        Function
 * @n  GND          GND              Ground
 * @n  3.3V-5V      VCC              Power
 * @n  SCL          SCL              I2C Clock
 * @n  SDA          SDA              I2C Data
 * @n  DPin         D                Transfer Status Line
 * @n  MCLRPin      MCLR             reset
 * @copyright Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
 * @license The MIT License (MIT)
 * @author [yangfeng]<feng.yang@dfrobot.com>
 * @version V1.0
 * @date 2021-09-18
 * @url  https://github.com/DFRobot/DFRobot_MGC3130
 */
#include <DFRobot_MGC3130.h>

//the following pins are recommended, can be customized by the users (pins with input and output functions are required)
#if defined(ESP32) || defined(ESP8266)
  uint8_t DPin= D9;
  uint8_t MCLRPin= D3;
#elif defined(ARDUINO_SAM_ZERO)
  uint8_t DPin= 6;
  uint8_t MCLRPin= 7;
#else
  uint8_t DPin= 8;
  uint8_t MCLRPin= 9;
#endif

DFRobot_MGC3130 myGesture(DPin,MCLRPin);

void setup()
{

  Serial.begin(115200);
  /**
   *  initialization function,return true if initialization succeeds, and false if initialization fails
   */
  while(!myGesture.begin()){
    Serial.println("begin error! Please check whether the connection is correct");
    delay(100);
  };
  Serial.println("begin success!!!");

  /**
   *  turn off AirWheel function,returning -1 means the setup fails, and 0 means the setup succeeds
   */
  while(myGesture.disableAirWheel()!=0){
    delay(100);
  }
  /**
   *  enable gesture recognition function, returning -1 means the setup fails, and 0 means the setup succeeds
   */
  while(myGesture.enableGestures()!=0){
    delay(100);
  }

  Serial.println("config success!!!");
}


void loop()
{
  /**
   *  get the sensor data
   */
  myGesture.sensorDataRecv();

  /**
   *  get gesture information, gesture information:eFilckR/eFilckL/eFilckU/eFilckD/eCircleClockwise/eCircleCounterclockwise
   */
  switch(myGesture.getGestureInfo()){
    case myGesture.eFilckR:
      Serial.println("Flick Left to Right");
      break;
    case myGesture.eFilckL:
      Serial.println("Flick Right to Left");
      break;
    case myGesture.eFilckU:
      Serial.println("Flick Down to Up");
      break;
    case myGesture.eFilckD:
      Serial.println("Flick Up to Down");
      break;
    case myGesture.eCircleClockwise:
      Serial.println("Circle clockwise");
      break;
    case myGesture.eCircleCounterclockwise:
      Serial.println("Circle counterclockwise");
      break;
    default:
      break;
  }
}
