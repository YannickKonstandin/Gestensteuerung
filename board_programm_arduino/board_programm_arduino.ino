// vor upload - in Suchleiste Edit configurations (JSON) - rechts unten am Bildschirm on Linux auf Arduino umstellen

const int trigger1 = 2; //Trigger pin of 1st Sesnor

const int echo1 = 3; //Echo pin of 1st Sesnor

float list_measurements[3];

long time_taken;

float dist,distL, dist_old, total, dist_;

bool state = 0;

void setup() {

Serial.begin(9600); 

  

pinMode(trigger1, OUTPUT); 

pinMode(echo1, INPUT); 

}


/*###Function to calculate distance###*/

void calculate_distance(int trigger, int echo){
    list_measurements[0,0,0];
    for(int i=0;i<3;i++){
      
    digitalWrite(trigger, LOW);
    
    delayMicroseconds(2);
    
    digitalWrite(trigger, HIGH);
    
    delayMicroseconds(10);
    
    digitalWrite(trigger, LOW);
    
    
    time_taken = pulseIn(echo, HIGH);
    
    dist_= time_taken*0.034/2;
    list_measurements[i] = dist_;
    total = list_measurements[0]+list_measurements[1]+list_measurements[2];
    delay(20);
    }
    
    dist = total/3;
    //Serial.println(dist);
}


void loop() { //infinite loopy

calculate_distance(trigger1,echo1);

if (dist< 40){

  calculate_distance(trigger1,echo1);
  }
  if (dist< 40){
      if (dist<10){
        Serial.println ("Vdown");
        delay (10);
      }
      if (dist>20){ 
        Serial.println ("Vup");
        delay (10);
      }

    }
  delay(20);

}
