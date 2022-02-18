float temp;
float humi;

float get_temperature () {
  DHT.read21(DHT_pin);
  return DHT.humidity;
}
float get_humidity () {
  DHT.read21(DHT_pin);
  return DHT.temperature;
}
void get_gas () {}
