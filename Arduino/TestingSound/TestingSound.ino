//Defining Global Variables
// Rmb to change your Sound port to the correct one:
int Sound = A2;

void setup() {


// active the Serial Monitor
 Serial.begin(9600);

}

void loop() {
  // define the Sound sensor readings as SoundVal
int SoundVal= analogRead(Sound);

 // print on Serial Monitor the outputs of the sound sensors
  Serial.print("Sound Volume Level: ");
  Serial.println(SoundVal);

 //delay loop by 1 second; you can delete this if you want more responsive reading
  delay(1000);
}
