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

servo1 = Servo(Pin(15))

while True:
        servo1.move()
        led.toggle()
        time.sleep(delay)
