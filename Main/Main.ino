/*
  Name:		Sketch1.ino
  Created:	3/13/2016 6:43:19 PM
  Author:	hejtmy
*/
#include <Keyboard.h>
#define numberOfButtons 4

String serialInput;
int timeout = 25;
bool connected = false;
bool photoresistorUse = false;
//speed for the delay factor
int speed = 20;

//pin setup
int pulsePin = 13;
int photoresistorPin = 0;

char* buttonColours[numberOfButtons] = {"RED","BLUE","YELLOW","GREEN"};
int buttonPins[numberOfButtons] = {7, 6, 5, 4};
//ascii chars representing
char buttonKeys[numberOfButtons] = {'a','d','j','l'};

int photoresistorThreshold = 500;

char untilChar = '\!';

// the setup function runs once when you press reset or power the board
void setup() {
  Keyboard.begin();
  Serial.begin(9600);
  Serial.setTimeout(timeout);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB
  }
  //initialise buttons
  for(int i = 0; i < numberOfButtons;i++){
    pinMode(buttonPins[i], INPUT_PULLUP);
  }
}

// the loop function runs over and over again until power down or reset
void loop() {
  serialInput = Serial.readStringUntil(untilChar);
  if (serialInput != "") {
    if (serialInput == "WHO") {
      lettingKnow();
    }
    if (connected) {
      ListenForOrders();
    }
  }
  if (connected){
    if (photoresistorUse) {
      PhotoresistorAction();
    }
    ButtonsAction();
  }
}

void lettingKnow() {
  float time = millis();
  while (true) {
    serialInput = Serial.readStringUntil(untilChar);
    if (serialInput == "DONE") {
      connected = true;
      break;
    }
    Serial.println("ARDUINO");
    if (millis() - time > 1000) {
      break;
    }
    delay(speed);
  }
}

void ListenForOrders() {
  if (serialInput != "") {
    if (serialInput == "RESTART") {
      connected = false;
      Serial.println("DONE");
    }
    if (serialInput == "SENDPULSE") {
      Serial.println("DONE");
    }
    if (serialInput == "PULSE+") {
      digitalWrite(13, HIGH);
      Serial.println("DONE");
    }
    if (serialInput == "PULSE-") {
      digitalWrite(13, LOW);
      Serial.println("DONE");
    }
    if (serialInput == "BLINK") {
      digitalWrite(13, HIGH);
      delay(100);
      digitalWrite(13, LOW);
      Serial.println("DONE");
    }
    if (serialInput == "PHOTO+") {
      photoresistorUse = true;
      Serial.println("DONE");
    }
    if (serialInput == "PHOTO-") {
      photoresistorUse = false;
      Serial.println("DONE");
    }
  }
  delay(speed);
}
void PhotoresistorAction(){
  if(digitalRead(7) == LOW){
    Serial.println(analogRead(photoresistorPin));
    static bool alreadyReacted = false;
    if (analogRead(photoresistorPin) > photoresistorThreshold) {
        if(!alreadyReacted){
          alreadyReacted = true;
          //do sth
        }
    } else {
      alreadyReacted = false;
    }
  }
  
}
void ButtonsAction(){
  for(int i=0; i < numberOfButtons; i++){
    if(digitalRead(buttonPins[i]) == LOW){
      Keyboard.write(buttonKeys[i]);
      Serial.println(buttonColours[i]);
    }
  }
}

