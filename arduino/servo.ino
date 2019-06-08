#include <Servo.h>      // Thư viện điều khiển servo

#include <DHT.h> // Gọi thư viện DHT22
 
//Constants
#define DHTPIN 2     // what pin we're connected to
#define DHTTYPE DHT22   // DHT22

DHT dht(DHTPIN, DHTTYPE); // Initialize DHT sensor for normal 16mhz Arduino

//Variables
float hum;  //Stores humidity value
float temp; //Stores temperature value
 
// Khai báo đối tượng myservo dùng để điều khiển servo
Servo myservo;          
 
int bientro = A0;       // Khai báo chân analog đọc biến trở điều khiển servo
int servoPin = 9;       // Khai báo chân điều khiển servo
 
void setup ()
{
    // Cài đặt chức năng điều khiển servo cho chân servoPin
    myservo.attach(servoPin); 
    
    //Initialize serial port
  Serial.begin(9600);

  //Serial.println("DHT22 sensor testing");
  
  //Initialize the DHT sensor
  dht.begin();  
  
  int servoPos = 0;
  myservo.write(servoPos);
  delay(5000);
}

int value  = 0;
void loop ()
{
    float converted = 0.00;
    
    //Read data and store it to variables hum and temp
    hum = dht.readHumidity();
    temp= dht.readTemperature();
    Serial.println("{\"temp\": \"" + String(temp) + "\", \"hum\": \"" + String(hum) + "\"}");
    int servoPos = 0;
    if(Serial.available() > 0) {
      String cmd = Serial.readString();
      Serial.println(cmd);
      if(cmd == "CMD:OPENCMD:OPEN" || cmd == "CMD:OPEN") {
          servoPos = 90;
          myservo.write(servoPos);
      }
      
      if(cmd == "CMD:CLOSECMD:CLOSE" || cmd == "CMD:CLOSE") {
          servoPos = 0;
            myservo.write(servoPos);
      }
    }
    delay(200);
    //servoPos = 90;
    //myservo.write(servoPos);
          
    //delay(2000);
    //servoPos = 0;
    //myservo.write(servoPos);
    //delay(2000);
    
}
