from machine import Pin, PWM #raspberry pi pico specific modules
import time, random
led = Pin(25, Pin.OUT)
laser = Pin(17, Pin.OUT)
led.value(1)


################################################################
while True: #while loop is where the code runs in a nonstop loop on the pico
    laser.value(1)
    led.value(1)
    time.sleep(2)
    laser.value(0)
    led.value(0)
    time.sleep(2)
