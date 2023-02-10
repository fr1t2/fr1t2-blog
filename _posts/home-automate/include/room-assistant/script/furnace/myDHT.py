import time
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        temperature_f = temperature * (9 / 5) + 32
        print("Temp={0:0.1f}F Humidity={1:0.1f}%".format(temperature_f, humidity))
        exit()
    else:
        time.sleep(.05);