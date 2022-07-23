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
        self.MIN = 814000
        self.MID = 1507000
        self.MAX = 2200000
        self.STEP = (self.MAX - self.MIN)/100
        super().duty_ns(self.MID)
    def duty(self,pos_perc):
        pos_ns = int((pos_perc * self.STEP)+self.MIN)
        super().duty_ns(pos_ns)
        print(pos_perc)
        print(pos_ns)


servo1 = Servo(Pin(15))
servo1.freq(50)
servo1.duty(5)

range = [50,60,70,80,90,100,90,80,70,60,50,40,30,20,10,0,10,20,30,40]

while True:
    for pos in range:
        servo1.duty(pos)
        led.toggle()
        time.sleep(delay)
