from machine import Pin
from machine import PWM
import time

delay = 0.5

led = Pin(25, Pin.OUT)
led.value(1)

laser = Pin(0, Pin.OUT)
laser.value(1)

pwm = PWM(Pin(15))
pwm.freq(50)
pwm.duty_ns(1507000)

range = [814000,1507000,2200000,1507000]

while True:
    for pos in range:
        pwm.duty_ns(pos)
        led.toggle()
        time.sleep(delay)
