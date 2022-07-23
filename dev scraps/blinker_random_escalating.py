import time, random
from machine import Pin, Timer
led = Pin(25, Pin.OUT)
laser = Pin(0,Pin.OUT)
led.value(0)