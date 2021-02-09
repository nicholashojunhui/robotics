// This code demonstrate the usefulness of Serial Communications
int pin = 1;

void setup() {
  // put your setup code here, to run once:
  
// This code helps to kickstart your Serial Monitor
 Serial.begin(9600); }

void loop() {
  // put your main code here, to run repeatedly:

// print on Serial Monitor your messages and the outputs
// typing Serial.println() function keeps the messages neater and easier to read
// Type "" in the function to type just a message; without "", the software will 
// detect it as an output to be displayed
  Serial.println("Welcome all to Robotics Systems Workshop 1!!!");
  Serial.println("All messages and output will be uploaded to the Serial Monitor");
  Serial.print("The pin output is: ");
  Serial.println(pin);
  Serial.println("");

 //Setting Delay Time (in ms; here we set to 10 seconds delay per loop)
 delay(10000); }
