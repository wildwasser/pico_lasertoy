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
    def move(self,):
        pos_perc = random.randint(self.pos_perc_min, self.pos_perc_max)
        pos_ns = int((pos_perc * self.STEP)+self.MIN)
        super().duty_ns(pos_ns)
        print(pos_perc)
        print(pos_ns)
    def move_limits(self,):
        for i in range(2):
            time.sleep(0.5)
            pos_ns = int((self.pos_perc_min * self.STEP)+self.MIN)
            super().duty_ns(pos_ns)
            time.sleep(0.5)
            pos_ns = int((self.pos_perc_max * self.STEP)+self.MIN)
            super().duty_ns(pos_ns)
    def calc_pos(self,pos):
        if pos == 0:
            pos_perc = random.randint(self.pos_perc_min, self.pos_perc_max)
            pos_ns = int((pos_perc * self.STEP)+self.MIN)
            super().duty_ns(pos_ns)
        else:
            pos_ns = int((pos * self.STEP)+self.MIN)
            super().duty_ns(pos_ns)


servo1 = Servo(Pin(15))

while True:
    for i in range(5):
        servo1.calc_pos(i)
        time.sleep(0.5)
    for i in range (5):
        servo1.calc_pos(0)
        time.sleep(1)
