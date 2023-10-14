int playe = 7;
int data;

void setup()
{ 
  Serial.begin(115200);
  //pinMode(rec, INPUT);
  pinMode(playe, OUTPUT);
}

void loop() {
  while (Serial.available()) {
    data = Serial.read();
  }
  
  if (data == '1') {
    digitalWrite(playe, HIGH);
    delay(10000);
    digitalWrite(playe, LOW);
  }
  else if (data == '0') {
    digitalWrite(playe, LOW);
  }
}
