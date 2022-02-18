

#include <dht.h>
dht DHT;
int DHT_pin = 13;
float get_temperature();
float get_humidity();
// 안의 함수가 read11 (dht11) 로 되어있을 수 있습니다. (read21)


#include <SoftwareSerial.h> 
SoftwareSerial ESP01(2, 3); 
void get_db_data_to_wifi();


#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);
void update_lcd_msg (int x, int y, String msg);
void update_lcd_clear ();


int led_relay_pin = 12;
void update_led (int flag);


int fan_right_speed_pin = 11;
int fan_right_direction1_pin = 10;
int fan_right_direction2_pin = 9;
int fan_left_direction1_pin = 8;
int fan_left_direction2_pin = 7;
int fan_left_speed_pin = 6;
void update_dc_fan (char motorSelect, int dir, int spd);

// motorSelect : 'r'(오른쪽) 'l'(왼쪽)
// dir : 1(정회전) 0(정지)
// spd : 모터 속도 (pwm)(driver에는 점퍼)



void setup() {
  set_wifi();
  set_output_part();
} 


void loop() { 
}


void update_input () {}
void update_output() {}
void update_comm_wifi () {}




void set_wifi () {
  // set wifi
  // wifi mode        : AT+CWMODE=1
  // search wifi      : AT+CWLAP
  // change wifi baud : AT+UART_DEF=9600,8,1,0,0
  // wifi connect     : AT+CWJAP="SSID","PASSWORD"
  // wifi disconnect  : AT+CWQAP 
  Serial.begin(9600);  //arduino uno baud 9600
  ESP01.begin(9600);   //wifi baud        9600
  ESP01.setTimeout(5000); 
  ESP01.println("AT+CWMODE=1\r\n");
  delay(1000);
  ESP01.println("AT+CWJAP=\"iptime_krc\",\"a16881252\"\r\n");
  delay(1000);
}


void set_output_part () {
  // set lcd
  lcd.init();
  lcd.backlight();
  update_lcd_msg(0,0,"hello!!");
  update_lcd_msg(0,1,"smart farm");
  delay(2000);
  update_lcd_clear();

  pinMode(led_relay_pin,OUTPUT); update_led(0);
  pinMode(fan_right_direction1_pin,OUTPUT);
  pinMode(fan_right_direction2_pin,OUTPUT);
  pinMode(fan_right_speed_pin,OUTPUT);
  pinMode(fan_left_direction1_pin,OUTPUT);
  pinMode(fan_left_direction2_pin,OUTPUT);
  pinMode(fan_left_speed_pin,OUTPUT);
}
