from machine import Pin
import time

led = Pin(25, Pin.OUT)
led.value(1)

switch = Pin(28, Pin.IN)

def waiting(howlong):
    led.value(0)
    for i in range(howlong):
        time.sleep(1)
        print(f"Waiting... {i} seconds")

while True:
    if switch.value() == 1:
        waiting(10)
    else:
        led.value(1)
