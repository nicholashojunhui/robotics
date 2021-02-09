// The aims for this program is to: 
// (a) obtain pin output as 13 and 
// (b) configure pin2 output to start from 1 and be increasing by 1 per second 

//Defining Global Variables pin and pin2
int pin = 13;
int pin2 = 0;

void setup() {
// put your setup code here, to run once:
  // This code helps to kickstart your Serial Monitor
 Serial.begin(9600); }

void loop() {
// put your main code here, to run repeatedly:
  //To increase pin2 output by 1 per loop

  pin2 = pin2 + 1;

 // print on Serial Monitor the outputs
  Serial.println("pin: ");
  Serial.println(pin);
   Serial.println("pin2: ");
  Serial.println(pin2);

// Delay the loop by 1 second
  delay(1000);  }
