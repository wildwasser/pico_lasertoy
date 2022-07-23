from machine import Pin, PWM
import time, random
delay = 1
led = Pin(25, Pin.OUT)
led.value(1)
laser = Pin(0, Pin.OUT)
laser.value(1)

class Servo(PWM):
    def __init__(self, pin: Pin):
        super().__init__(pin)
        self.ns_MIN = 814000
        self.ns_MID = 1507000
        self.ns_MAX = 2200000
        self.ns_STEP = (self.ns_MAX - self.ns_MIN) /100
        self.perc_min = 40
        self.perc_max = 60
        super().freq(50)
        super().duty_ns(self.ns_MID)
    def random(self,):
        super().duty_ns(int(((random.randint(self.perc_min, self.perc_max)) * self.ns_STEP)+self.ns_MIN))
    def min(self,):
        super().duty_ns(int((self.perc_min * self.ns_STEP)+self.ns_MIN))
    def max(self,):
        super().duty_ns(int((self.perc_max * self.ns_STEP)+self.ns_MIN))

servo1 = Servo(Pin(15))

while True:
    for i in range(5):
        servo1.random()
        time.sleep(delay)
        led.toggle()
    for i in range(2):
        servo1.min()
        time.sleep(0.5)
        servo1.max()
        time.sleep(0.5)
    if servo1.perc_max <=90 and servo1.perc_min >= 10:
        servo1.perc_max += 10
        servo1.perc_min -= 10
    else:
        servo1.perc_max = 60
        servo1.perc_min = 40
