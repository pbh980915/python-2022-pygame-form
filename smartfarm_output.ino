

void update_led (int flag) { digitalWrite(led_relay_pin, ~flag); }



void update_lcd_msg (int x, int y, String msg) {
  lcd.setCursor(x,y);
  lcd.print(msg);
}
void update_lcd_clear () {
  lcd.setCursor(0,0);
  lcd.clear();
}


void update_dc_fan (char motorSelect, int dir, int spd) {
  
  if(motorSelect == 'r') {
    if(dir == 1) {// 정회전
      digitalWrite(fan_right_direction1_pin, 1);
      digitalWrite(fan_right_direction2_pin, 0);
      analogWrite(fan_right_speed_pin, spd);
    }
    if(dir == 0) {// 정지
      digitalWrite(fan_right_direction1_pin, 1);
      digitalWrite(fan_right_direction2_pin, 1);
      analogWrite(fan_right_speed_pin, spd);
    }
  }
  if(motorSelect == 'l') {
    if(dir == 1) {// 정회전
      digitalWrite(fan_left_direction1_pin, 1);
      digitalWrite(fan_left_direction2_pin, 0);
      analogWrite(fan_left_speed_pin, spd);
    }
    if(dir == 0) {// 정지
      digitalWrite(fan_left_direction1_pin, 1);
      digitalWrite(fan_left_direction2_pin, 1);
      analogWrite(fan_left_speed_pin, spd);
    }
  }
  
}


void update_relay_ultrasonic () {}
void update_relay_heater () {}






void test_motor () {
  for(int i=100; i<255;i++) {
    update_dc_fan('r',1, i); update_dc_fan('l',1, i);
    delay(30);
  }
  for(int i=100; i<255;i++) {
    update_dc_fan('r',1, 255-i); update_dc_fan('l',1, 255-i);
    delay(30);
  }
}
