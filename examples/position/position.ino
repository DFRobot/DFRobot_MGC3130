/*!
 * @file position.ino
 * @brief position recognition, data on X, Y and Z axes (zero at southwest position of touch plate, silkscreen at Down)
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
   *  initialization function,return true if initialization succeeds, false if initialization fails
   */
  while(!myGesture.begin()){
    Serial.println("begin error! Please check whether the connection is correct");
    delay(100);
  };
  Serial.println("begin success!!!");

  /**
   *  enable proximity detection function, returning -1 means the setup fails, and 0 means the setup succeeds
   */
  while (myGesture.enableApproachDetection() != 0){
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
   *  monitor position information ,returning true means position information existed and false means not
   */
  if(myGesture.havePositionInfo()){
    Serial.print("X: ");
    Serial.print(myGesture.getPositionX());
    Serial.print("   Y: ");
    Serial.print(myGesture.getPositionY());
    Serial.print("   Z: ");
    Serial.println(myGesture.getPositionZ());
  }
}
