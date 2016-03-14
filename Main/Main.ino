/*
Name:		Sketch1.ino
Created:	3/13/2016 6:43:19 PM
Author:	hejtmy
*/
String serialInput;
int timeout = 25;
bool connected = false;
//speed for the delay factor
int speed = 20;
int i = 0;
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
	serialInput = Serial.readStringUntil('\n');
	if (serialInput != "") {
		if (serialInput == "WHO") {
			lettingKnow();
		}	
		if (connected) {
			ListenForOrders();
		}
	}
}

void lettingKnow() {
	float time = millis();
	while (true) {
		serialInput = Serial.readStringUntil('\n');
		if (serialInput == "DONE") {
			connected = true;
			break;
		}
		Serial.println("ARDUINO");
		if (millis() - time > 1000) { break; }
		delay(speed);
	}
}

void ListenForOrders() {
	if (serialInput != "") {
		if (serialInput == "RESTART") {
			connected = false;
		}
		if (serialInput == "SENDPULSE") {
		}
		if (serialInput == "BLINK") {
			digitalWrite(13, HIGH);
			delay(100);
			digitalWrite(13, LOW);
		}
	}
	delay(speed);
}
