from machine import Pin, PWM
import time, random
delay = 1
led = Pin(25, Pin.OUT)
led.value(1)
laser = Pin(0, Pin.OUT)
laser.value(1)

switch = Pin(16, Pin.IN)

class Servo(PWM):
    def __init__(self, pin: Pin):
        super().__init__(pin)
        self.MIN = 814000
        self.MID = 1507000
        self.MAX = 2200000
        self.STEP = (self.MAX - self.MIN)/100
        self.pos_perc_min = 40
        self.pos_perc_max = 60
        super().freq(50)
        super().duty_ns(self.MID)
    def rand(self,):
        super().duty_ns(int(((random.randint(self.pos_perc_min, self.pos_perc_max)) * self.STEP)+self.MIN))
    def min(self,):
        super().duty_ns(int((self.pos_perc_min * self.STEP)+self.MIN))
    def max(self,):
        super().duty_ns(int((self.pos_perc_max * self.STEP)+self.MIN))


servo1 = Servo(Pin(15))

while True:
    led.value(1)
    time.sleep(2)
    for i in range(5):
        servo1.rand()
        time.sleep(1)
    time.sleep(2)
    led.value(0)
    for i in range(5):
        servo1.min()
        time.sleep(1)
        servo1.max()
        time.sleep(1)
