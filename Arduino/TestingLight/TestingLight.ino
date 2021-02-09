//Defining Global Variables
// Rmb to change your Light port to the correct one:
int Light = A2;

void setup() {


// active the Serial Monitor
 Serial.begin(9600);

}

void loop() {
  // define the light sensor readings as BrightnessVal
int BrightnessVal= analogRead(Light);

 // print on Serial Monitor the outputs of the light sensors
  Serial.print("Brightness: ");
  Serial.println(BrightnessVal);

 //delay loop by 1 second; you can delete this if you want more responsive reading
  delay(1000);
}
