#include <Arduino.h>
#include <IBusBM.h>

// https://platformio.org/lib/show/6248/IBusBM/examples
IBusBM IBus; // IBus object

//serialInput is all 1000 to 2000i
double serialToPower(int serialInput) {
  return serialInput / 500.0 - 3;
}

double forwardMovement(int serialInput) {
  double power = serialToPower(serialInput);
  //left_motor.setPower(power);
  //right_motor.setPower(power);
  return power;
}

double rotation(int serialInput) {
  double rotation_power = serialToPower(serialInput);
  //left_motor.setPower(-power);
  //right_motor.setPower(power);
  return rotation_power;
}

double depth(int serialInput) { //goes from 0 to 10 ft
  double depth = (serialInput - 2000) / -100.0;
  return depth;
}

void setup() {
  Serial.begin(115200);   // remove comment from this line if you change the Serial port in the next line

  IBus.begin(Serial);    // iBUS connected to Serial0 - change to Serial1 or Serial2 port when required

  Serial.println("Start IBus2PWM");
}

void loop() {
  // for(uint8_t i = 0; i < 10; ++i) {
  //   Serial.print(IBus.readChannel(i));
  //   Serial.print("\t");
  // }
  // Serial.println();

  Serial.print("Rotation: ");
  Serial.print(rotation(IBus.readChannel(0)));
  Serial.print('\t');

  Serial.print("Forwards: ");
  Serial.print(forwardMovement(IBus.readChannel(1)));
  Serial.print('\t');

  Serial.print("Depth: ");
  Serial.print(depth(IBus.readChannel(2)));
  Serial.println();
  delay(200);
}
