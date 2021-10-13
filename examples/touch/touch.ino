/*!
 * @file touch.ino
 * @brief detect the touch status of 5 electric fields (up, down, left, right, center), which can be: touch, single click and double click
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
   *  initialization function, return true if initialization succeeds, false if initialization fails
   */
  while(!myGesture.begin()){
    Serial.println("begin error! Please check whether the connection is correct");
    delay(100);
  };
  Serial.println("begin success!!!");

  /**
   *  enable touch detection function, returning -1 means the setup fails, and 0 means the setup succeeds
   */
  while(myGesture.enableTouchDetection()!=0){
    delay(100);
  }

  Serial.println("config success!!!");
}
void loop()
{
  /**
   * @brief get the sensor data
   */
  myGesture.sensorDataRecv();

  /**
   *  get touch information
   *  touch information:
   *         eDoubleTapCenter/eDoubleTapRight/eDoubleTapUp/eDoubleTapLeft/eDoubleTapDown/eTapCenter/
   *         eTapRight/eTapUp/eTapLeft/eTapDown/eTouchCenter/eTouchRight/eTouchUp/eTouchLeft/eTouchDown
   */
  uint16_t info = myGesture.getTouchInfo();
  if(info & myGesture.eDoubleTapCenter){
    Serial.println("Double Tap Center electrode");
  } 
  if(info & myGesture.eDoubleTapRight){
    Serial.println("Double Tap Right electrode");
  } 
  if(info & myGesture.eDoubleTapUp){
    Serial.println("Double Tap Up electrode");
  } 
  if(info & myGesture.eDoubleTapLeft){
    Serial.println("Double Tap Left electrode");
  } 
  if(info & myGesture.eDoubleTapDown){
    Serial.println("Double Tap Down electrode");
  } 
  if(info & myGesture.eTapCenter){
    Serial.println("Tap Center electrode");
  } 
  if(info & myGesture.eTapRight){
    Serial.println("Tap Right electrode");
  } 
  if(info & myGesture.eTapUp){
    Serial.println("Tap Up electrode");
  } 
  if(info & myGesture.eTapLeft){
    Serial.println("Tap Left electrode");
  } 
  if(info & myGesture.eTapDown){
    Serial.println("Tap Down electrode");
  } 
  if(info & myGesture.eTouchCenter){
    Serial.println("Touch Center electrode");
  } 
  if(info & myGesture.eTouchRight){
    Serial.println("Touch Right electrode");
  } 
  if(info & myGesture.eTouchUp){
    Serial.println("Touch Up electrode");
  } 
  if(info & myGesture.eTouchLeft){
    Serial.println("Touch Left electrode");
  } 
  if(info & myGesture.eTouchDown){
    Serial.println("Touch Down electrode");
  }
}
