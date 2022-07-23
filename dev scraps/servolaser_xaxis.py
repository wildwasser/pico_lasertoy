from machine import Pin, PWM
import utime
led = Pin(25, Pin.OUT)
laser = Pin(0, Pin.OUT)
pwm = PWM(Pin(15))
pwm.freq(50)
led.value(0)
laser.value(1)

#MID = 1500000
#MIN = 900000
#MAX = 2200000

MIN = 1300000
MID = 1500000
MAX = 1700000
timer = 1
pwm.duty_ns(MID)

while True:
    pwm.duty_ns(MIN)
    led.value(1)
    utime.sleep(timer)
    
    pwm.duty_ns(MID)
    led.value(0)
    utime.sleep(timer)

    pwm.duty_ns(MAX)
    led.value(1)
    utime.sleep(timer)
    
    pwm.duty_ns(MID)
    led.value(0)
    utime.sleep(timer)
    