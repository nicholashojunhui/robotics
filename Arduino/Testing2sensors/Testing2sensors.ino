//Include DHT library
#include "DHT.h"

// Rmb to change your DHT port to the correct one:
#define DHTPIN 4
#define DHTTYPE DHT11   // Grove DHT sensors are DHT 11

DHT dht(DHTPIN, DHTTYPE);

//Defining Global Variables
// Rmb to change your Light port to the correct one:
int Light = A2;

void setup() {


// active the Serial Monitor
 Serial.begin(9600);

dht.begin();

}

void loop() {
  // define the DHT sensor readings as TempVal and HumidVal
float TempVal= dht.readTemperature();
float HumidVal= dht.readHumidity();

// define the light sensor readings as BrightnessVal
int BrightnessVal= analogRead(Light);

 // print on Serial Monitor the outputs of the DHT sensors
  Serial.print("Temperature: ");
  Serial.println(TempVal);

  Serial.print("Humidity: ");
  Serial.println(HumidVal);

   // print on Serial Monitor the outputs of the light sensors
  Serial.print("Brightness: ");
  Serial.println(BrightnessVal);

 //delay loop by 1 second; you can delete this if you want more responsive reading
  delay(100);
}
