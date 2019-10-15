char untilChar = '\!';
String serialInput = "";
void setup() {
  Serial.begin(38400);
  Serial.setTimeout(25);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB
  }
}

void loop() {
  // print the string when a newline arrives:
  if (serialInput != "") {
    Serial.println(serialInput);
    serialInput = "";
  }
}

/*
  SerialEvent occurs whenever a new data comes in the hardware serial RX. This
  routine is run between each time loop() runs, so using delay inside loop can
  delay response. Multiple bytes of data may be available.
*/
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    serialInput = Serial.readStringUntil(untilChar);
  }
}
