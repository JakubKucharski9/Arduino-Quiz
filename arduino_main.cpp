const int buttonPinA = 2;
const int buttonPinB = 3;
const int buttonPinC = 4;
const int buttonPinD = 5;

const int ledPinG = 12;
const int ledPinR = 13;

int stage = 0;

void setup() {
  Serial.begin(9600);
  pinMode(buttonPinA, INPUT_PULLUP);
  pinMode(buttonPinB, INPUT_PULLUP);
  pinMode(buttonPinC, INPUT_PULLUP);
  pinMode(buttonPinD, INPUT_PULLUP);
  pinMode(ledPinG, OUTPUT);
  pinMode(ledPinR, OUTPUT);
}

void loop() {
  if(stage == 0){
      if (digitalRead(buttonPinA) == LOW) {
        Serial.println("QA");
        delay(300);
        stage++;
      }
      if (digitalRead(buttonPinB) == LOW) {
        Serial.println("QB");
        delay(300);
        stage++;
      }
      if (digitalRead(buttonPinC) == LOW) {
        Serial.println("QC");
        delay(300);
        stage++;
      }
      if (digitalRead(buttonPinD) == LOW) {
        Serial.println("QD");
        delay(300);
        stage++;
      }
  }
  else if(stage == 1){
      if (digitalRead(buttonPinA) == LOW) {
        Serial.println("A");
        delay(300);
      }
      if (digitalRead(buttonPinB) == LOW) {
        Serial.println("B");
        delay(300);
      }
      if (digitalRead(buttonPinC) == LOW) {
        Serial.println("C");
        delay(300);
      }
      if (digitalRead(buttonPinD) == LOW) {
        Serial.println("D");
        delay(300);
      }

      if (Serial.available() > 0) {
        char result = Serial.read();
        if (result == '1') {
          digitalWrite(ledPinG, HIGH);
          delay(500);
          digitalWrite(ledPinG, LOW);
          stage--;
        } else if (result == '0') {
          digitalWrite(ledPinR, HIGH);
          delay(500);
          digitalWrite(ledPinR, LOW);
          stage--;
        }
      }
  }
}
