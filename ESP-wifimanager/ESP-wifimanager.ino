#include <ESP8266WiFi.h>          //https://github.com/esp8266/Arduino

//needed for library
#include <DNSServer.h>
#include <ESP8266WebServer.h>
#include <WiFiManager.h>         //https://github.com/tzapu/WiFiManager

String data_from_arduino;
String host = "192.168.1.35";
int port = 80;
String url = "";
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

  if (WiFi.status()!=WL_CONNECTED)
  {
      Serial.println("failed to connect, finishing setup anyway");
  } 
  else
  {
    Serial.print("local ip: ");
    Serial.println(WiFi.localIP());
  }
  //if you get here you have connected to the WiFi
  //Serial.println("connected...yeey :)");
  //WiFiClient client;
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(1000);
  //data_from_arduino = "";
  //url = "";
  if (Serial.available()>0) {
    data_from_arduino = Serial.readStringUntil('\n');
    }
  url = "/?"+ data_from_arduino;
  if (client.connect(host,port)){
  client.print(String("GET ") + url + " HTTP/1.1\r\n" + "Host: " + host + "\r\n" + "Connection: close\r\n\r\n");
  }
  client.stop();
}
