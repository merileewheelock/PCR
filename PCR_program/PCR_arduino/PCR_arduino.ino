String data;

void setup() { 
  Serial.begin(9600); //initialize serial COM at 9600 baudrate
  pinMode(LED_BUILTIN, OUTPUT); //make the LED pin (13) as output
  digitalWrite (LED_BUILTIN, LOW);
  
  Serial.println("Arduino connected!");
}
 
void loop() {
while (Serial.available()){
  data = Serial.readString();
  Serial.println(data);
};

//Serial.print(data);

if (data == "s"){
Serial.println(data);
digitalWrite (LED_BUILTIN, HIGH);
}

else if (data == "f"){
digitalWrite (LED_BUILTIN, LOW);
};

}
