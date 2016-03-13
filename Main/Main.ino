/*
 Name:		Sketch1.ino
 Created:	3/13/2016 6:43:19 PM
 Author:	hejtmy
*/
String serialInput;
int timeout = 25;

// the setup function runs once when you press reset or power the board
void setup() {
  Serial.begin(9600); 
  Serial.setTimeout(timeout);
    while (!Serial) {
      ; // wait for serial port to connect. Needed for native USB
    }
}

// the loop function runs over and over again until power down or reset
void loop() {
    serialInput = Serial.readString();
    if (serialInput == "WHO\n"){
      lettingKnow();
    }
    delay(1);
}

void lettingKnow(){
  while (true){
    serialInput = Serial.readString();
    if (serialInput == "DONE"){
      break;
    }
    Serial.println("ARDUINO");
    delay(1);
  }
}

