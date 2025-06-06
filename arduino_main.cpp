const int buttonPinA = 2;
const int buttonPinB = 3;
const int buttonPinC = 4;
const int buttonPinD = 5;

const int ledPinG = 12;
const int ledPinR = 13;

int stage = 0;

void setup() {
  Serial.begin(9600);
  pinMode(buttonPinA, INPUT);
  pinMode(buttonPinB, INPUT);
  pinMode(buttonPinC, INPUT);
  pinMode(buttonPinD, INPUT);
  pinMode(ledPinG, OUTPUT);
  pinMode(ledPinR, OUTPUT);
}

void loop() {
  if(stage == 0){
      if (digitalRead(buttonPinA) == HIGH) {
        Serial.println("QA");
        delay(300);
        stage++;
      }
      if (digitalRead(buttonPinB) == HIGH) {
        Serial.println("QB");
        delay(300);
        stage++;
      }
      if (digitalRead(buttonPinC) == HIGH) {
        Serial.println("QC");
        delay(300);
        stage++;
      }
      if (digitalRead(buttonPinD) == HIGH) {
        Serial.println("QD");
        delay(300);
        stage++;
      }
  }
  else if(stage == 1){
      if (digitalRead(buttonPinA) == HIGH) {
        Serial.println("A");
        delay(300);
      }
      if (digitalRead(buttonPinB) == HIGH) {
        Serial.println("B");
        delay(300);
      }
      if (digitalRead(buttonPinC) == HIGH) {
        Serial.println("C");
        delay(300);
      }
      if (digitalRead(buttonPinD) == HIGH) {
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
