from machine import Pin
from machine import PWM
import time

delay = 0.5

led = Pin(25, Pin.OUT)
led.value(1)

laser = Pin(0, Pin.OUT)
laser.value(1)

class Laser:
    def __init__(self,pin)
        pwm = Pin(pin, Pin.OUT)
    def set(self,)
        self.pwm.duty_ns(_pwm)

