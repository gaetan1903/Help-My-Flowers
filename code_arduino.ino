const int analogInPinh = A0;  

const int analogInPinl = A3;  

int sensorValue = 0;
int lumValue = 0;  

void setup() {
  Serial.begin(9600);
  pinMode(A3, INPUT);
  pinMode(A0, INPUT);
}

void loop() {
  sensorValue = analogRead(analogInPinh);
  lumValue = analogRead(analogInPinl);

  Serial.print(sensorValue);
  Serial.print("_");
  Serial.println(lumValue);

  delay(2000);
}