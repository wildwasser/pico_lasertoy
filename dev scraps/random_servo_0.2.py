from machine import Pin
from machine import PWM
import time

delay = 0.5

led = Pin(25, Pin.OUT)
led.value(1)

laser = Pin(0, Pin.OUT)
laser.value(1)

pwm = PWM(Pin(15))
pwm.freq(50)
pwm.duty_ns(1507000)

class Servo(PWM):
    _min = 814000
    _mid = 1507000
    _max = 2200000
    def __init__(self,_pin)
        _pwm = PWM(Pin(_pin))
        _pwm.freq(50)
        _pwm.duty_ns(_mid)
    def pwm_set(self,_pwm)
        _pwm.duty_ns(_pwm)

################################################################

class myPWM(PWM):
    def __init__(self, pin: Pin):
        super().__init__(pin)
    def duty(self,d):
        super().duty_u16(65535*d//1000)

In this case the percentage is specified multiplied by 10. For example, to set a 50% duty cycle you would use:

pwm16 = myPWM(Pin(16))
pwm16.freq(50)
pwm16.duty(500)


################################




servo1 = Servo(15)

range = [814000,1507000,2200000,1507000]

while True:
    for pos in range:
        servo1.pwm_set(pos)
        led.toggle()
        time.sleep(delay)
