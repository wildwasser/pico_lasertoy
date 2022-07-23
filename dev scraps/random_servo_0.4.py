from machine import Pin, PWM
import time

delay = 0.5

led = Pin(25, Pin.OUT)
led.value(1)

laser = Pin(0, Pin.OUT)
laser.value(1)


class Servo(PWM):
    def __init__(self, pin: Pin):
        super().__init__(pin)
    def duty(self,d):
        super().duty_u16(65535*d//1000)

servo1 = Servo(Pin(15))
servo1.freq(50)
servo1.duty(500)

#range = [814000,1507000,2200000,1507000]
range = [100,500,900,500]

while True:
    for pos in range:
        servo1.duty(pos)
        led.toggle()
        time.sleep(delay)
