void get_db_data_to_wifi () {}
void send_db_data_to_wifi () {}

void set_wifi_at () {
  if (Serial.available()){
    ESP01.write(Serial.read()); 
  } 
  if (ESP01.available()) { 
    Serial.write(ESP01.read()); 
  }
}
