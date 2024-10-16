void setup() {
  Serial.begin(115200);
  pinMode(12, OUTPUT);
}

int previousTime = 0;
void loop() {
  digitalWrite(12, HIGH);
  Serial.write("Hello world");
  digitalWrite(12, LOW);
}