from machine import Pin, PWM
import time, random
delay = 1
led = Pin(25, Pin.OUT)
led.value(1)
#laser = Pin(0, Pin.OUT)
#laser.value(1)

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
    def go(self,pos):
        super().duty_ns(int((pos * self.STEP)+self.MIN))

class Laser(Pin):
    def __init__(self, pin: Pin):
        super().__init__(pin)
        super().value(1)
    def rand(self,):
        i = random.randint(1,10)
        if i >= 3:
            super().value(1)
        else:
            super().value(0)

servo1 = Servo(Pin(21))
laser = Laser(14)

while True:
    servo1.rand()
    time.sleep(delay)
    led.toggle()
    laser.rand()
