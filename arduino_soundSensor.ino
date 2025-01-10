//globals
int analogPin = A0;

int analogVal;
int digitalVal;

int baseline = 512;
int LED  = 3; 

void setup() {
  // setup for serial data flow
  Serial.begin(9600);
  pinMode(analogPin, INPUT);
  pinMode(LED, OUTPUT);

}

void loop() {
  analogVal = analogRead(analogPin);

  //print val to serial
  Serial.println(analogVal);

  if ( analogVal > 51 ) {
    digitalWrite(LED, HIGH);
  }
  else {
    digitalWrite(LED, LOW);
  }

  //delay(100);
}
