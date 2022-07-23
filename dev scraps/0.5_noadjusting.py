from machine import Pin, PWM
import time, random
led = Pin(25, Pin.OUT)
led.value(1)

def delay(n):
    if n == 0:
        time.sleep(0.55)
    else:
        time.sleep(n)

def hodl():
    hodl_min = 1
    hodl_max = 3
    hodl_time = random.randint(hodl_min,hodl_max)
    delay(hodl_time)

class Servo(PWM):
    def __init__(self, pin: Pin):
        super().__init__(pin)
        self.MIN = 814000
        self.MAX = 2200000
        self.STEP = (self.MAX - self.MIN)/100
        self.pos_perc_min = 40
        self.pos_perc_max = 60
        super().freq(50)
        super().duty_ns(int((50 * self.STEP)+self.MIN))
        delay(0)
    def rand(self,):
        super().duty_ns(int((random.randint(self.pos_perc_min, self.pos_perc_max) * self.STEP)+self.MIN))
    def min(self,):
        super().duty_ns(int((self.pos_perc_min * self.STEP)+self.MIN))
    def max(self,):
        super().duty_ns(int((self.pos_perc_max * self.STEP)+self.MIN))
    def go(self,pos):
        super().duty_ns(int((pos * self.STEP)+self.MIN))
        delay(0)

class Laser(Pin):
    def __init__(self, pin: Pin):
        super().__init__(pin)
        super().value(1)
    def rand(self,):
        i = random.randint(0,100)
        if i >= 5:
            super().value(1)
        else:
            super().value(0)

servo1 = Servo(Pin(15))
#servo1.pos_perc_min = 40
#servo1.pos_perc_max = 60
servo2 = Servo(Pin(16))
#servo2.pos_perc_min = 40
#servo2.pos_perc_max = 60
laser  = Laser(0)

while True:
    for i in range(2):
        servo1.min()
        servo2.min()
        led.toggle()
        delay(0)
        servo1.min()
        servo2.max()
        led.toggle()
        delay(0)
        servo1.max()
        servo2.max()
        led.toggle()
        delay(0)
        servo1.max()
        servo2.min()
        led.toggle()
        delay(0)
        servo1.min()
        servo2.min()
        led.toggle()
        delay(1.5)
    servo1.go(50)
    servo2.go(50)
    delay(0)
    for i in range(20):
        servo1.rand()
        servo2.rand()
        laser.rand()
        hodl()
        led.toggle()
    laser.value(1)
    servo1.go(50)
    servo2.go(50)
