import time, random
from machine import Pin, Timer
led = Pin(25, Pin.OUT)
laser = Pin(0, Pin.OUT)
led.value(0)
laser.value(0)
s = 100

while True:
    led.value(1)
    laser.value(1)
    time.sleep_ms(s)
    led.value(0)
    laser.value(0)
    time.sleep_ms(s)      # sleep for 500 milliseconds
    s = random.randint(100, 1000)
