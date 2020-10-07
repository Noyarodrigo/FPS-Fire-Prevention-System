#include <ESP8266WiFi.h>          //https://github.com/esp8266/Arduino
//#include <ArduinoJson.h>
//needed for library
#include <DNSServer.h>
#include <ESP8266WebServer.h>
#include <WiFiManager.h>         //ht tps://github.com/tzapu/WiFiManager

String data_from_arduino;
String pylogger = "192.168.1.35";
String thingspeak = "api.thingspeak.com";
int port = 80;
String msg = "";
String apiKey = "AGO3Y6O5OF03OMSB";
int i = 0;
WiFiManager wifiManager;
WiFiClient client;

void setup() {
  // put your setup code here, to run once:
  
  Serial.begin(9600);

  //WiFiManager
  //Local intialization. Once its business is done, there is no need to keep it around
 
  //reset saved settings
  //wifiManager.resetSettings();

  //set custom ip for portal
  //wifiManager.setAPStaticIPConfig(IPAddress(10,0,1,1), IPAddress(10,0,1,1), IPAddress(255,255,255,0));

  //fetches ssid and pass from eeprom and tries to connect
  //if it does not connect it starts an access point with the specified name
  //here  "AutoConnectAP"
  //and goes into a blocking loop awaiting configuration
  wifiManager.autoConnect("Sensor-gas-01");
  //or use this for auto generated name ESP + ChipID
  //wifiManager.autoConnect();
 
  //if you get here you have connected to the WiFi
  //Serial.println("connected...yeey :)");
  //WiFiClient client;
}

void loop() {
  delay(2000);
  data_from_arduino = "";
  //if (Serial.available()>0) {
  while (Serial.available()) {
    data_from_arduino = Serial.readStringUntil(';');
  }
  Serial.flush();
  if (client.connect(thingspeak,port)){
   client.print("POST /update HTTP/1.1\n");
   client.print("Host: api.thingspeak.com\n");
   client.print("Connection: close\n");
   client.print("X-THINGSPEAKAPIKEY: "+apiKey+"\n");
   client.print("Content-Type: application/x-www-form-urlencoded\n");
   client.print("Content-Length: ");
   client.print(data_from_arduino.length());
   client.print("\n\n");
   client.print(data_from_arduino);
  }
  client.stop();

   if (client.connect(pylogger, port)){
   client.print(data_from_arduino);
  }
  client.stop();
}
