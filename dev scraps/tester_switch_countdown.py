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

deadline = time.ticks_add(time.ticks_ms(), 5000)

while True:
    if switch.value() == 1:
        deadline = time.ticks_add(time.ticks_ms(), 5000)
        while time.ticks_diff(deadline, time.ticks_ms()) > 0:
            waiting(1)

    else:
        led.value(1)

