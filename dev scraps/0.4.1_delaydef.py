from machine import Pin, PWM
import time, random
led = Pin(25, Pin.OUT)
led.value(1)
delay_move = 0.55
#laser = Pin(0, Pin.OUT)
#laser.value(1)

class Servo(PWM):
    def __init__(self, pin: Pin):
        super().__init__(pin)
        self.MIN = 814000
        self.MID = 1507000
        self.MAX = 2200000
        self.STEP = (self.MAX - self.MIN)/100
        self.pos_perc_min = 0
        self.pos_perc_max = 100
        super().freq(50)
        super().duty_ns(self.MID)
        time.sleep(delay_move)
    def rand(self,):
        super().duty_ns(int(((random.randint(self.pos_perc_min, self.pos_perc_max)) * self.STEP)+self.MIN))
        time.sleep(delay_move)
    def min(self,):
        super().duty_ns(int((self.pos_perc_min * self.STEP)+self.MIN))
        time.sleep(delay_move)
    def max(self,):
        super().duty_ns(int((self.pos_perc_max * self.STEP)+self.MIN))
        time.sleep(delay_move)
    def go(self,pos):
        super().duty_ns(int((pos * self.STEP)+self.MIN))
        time.sleep(delay_move)

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

hodl_min = 1
hodl_max = 2

def hodl():
    time.sleep(random.randint(hodl_min,hodl_max))

servo1 = Servo(Pin(15))
laser = Laser(0)

while True:
    laser.value(1)
    servo1.go(50)
    for i in range(5):
        servo1.min()
        led.toggle()
        servo1.max()
        led.toggle()
    for i in range(5):
        servo1.go(49)
        hodl()
        servo1.go(51)
        laser.toggle()
        led.toggle()
