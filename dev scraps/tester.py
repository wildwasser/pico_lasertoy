from machine import Pin, PWM
import time
delay = 1

led = Pin(25, Pin.OUT)
led.value(1)

pwm = PWM(Pin(22))
pwm.freq(50)
pwm.duty_ns(1507000)
mid = 1507000
min = 340000
max = 2647000
pos = 320000

while True:
        pwm.duty_ns(pos)
