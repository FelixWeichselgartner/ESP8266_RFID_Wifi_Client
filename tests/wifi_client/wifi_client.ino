#include <ESP8266WiFi.h>

String ssid = "wifi-Felix";
String password = "a9#5u1+-5";
const char* server_ip = "192.168.178.77";
const int port = 9999;

void setup() {
    Serial.begin(115200);
    WiFi.mode(WIFI_STA); // <<< Station
    WiFi.begin(ssid.c_str(), password.c_str());
    Serial.println("Connecting to AP");
    while(WiFi.status() != WL_CONNECTED){
        Serial.println(".");
        yield();
    }
    Serial.println(" connected");
}

void loop() {
    WiFiClient client;
    Serial.println("Connecting to host");
    
    if(!client.connect(server_ip, port)){
        Serial.println("...connection failed!");
        Serial.println("Retrying in 5 seconds...");
        delay(5000);
        return;
    }

    client.print("uid: 0b d0 17 1c\n");
    Serial.println("...TCP message fired!");

    while (client.connected())
    {
        if (client.available())
        {
            String line = client.readStringUntil('\n');
            Serial.println(line);
        }
    }

    delay(2000);
}
