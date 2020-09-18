#include "DHT.h"
#define DHTTYPE DHT11
String msg;
int sensePin = A0;  //This is the Arduino Pin that will read the sensor output
int sensorInput;    //The variable we will use to store the sensor input
double temp;        //The variable we will use to store temperature in degrees. 

const int DHTPin = 48;
DHT dht(DHTPin, DHTTYPE);
 
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  dht.begin();
}
void loop() {
  delay(2000);
  msg = "";
  // put your main code here, to run repeatedly: 
  sensorInput = analogRead(A0);    //read the analog sensor and store it
  temp = (double)sensorInput / 1024;       //find percentage of input reading
  temp = temp * 5;                 //multiply by 5V to get voltage
  temp = temp - 0.5;               //Subtract the offset 
  temp = temp * 100;               //Convert to degrees 
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  msg = "atmp=" + String(temp) + "&hum=" + String(h) + "&tmp" + String(t) + "\n";
  Serial.print(msg);
  Serial.flush();
}
