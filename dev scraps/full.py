from machine import Pin, PWM #raspberry pi pico specific modules
import time, random
led = Pin(25, Pin.OUT)
led.value(1)

def delay(n): #basic function to call delays, setting the input to 0 calls the minimum delay needed to move a servo 100%
    if n == 0:
        time.sleep(0.55)
    else:
        time.sleep(n)

def hodl(): #this function defines a randomised delay to  help with random movement creation
    hodl_min = 2
    hodl_max = 5
    hodl_time = random.randint(hodl_min,hodl_max)
    delay(hodl_time)

class Laser(Pin):
    def __init__(self, pin: Pin): #sets up the pin defnition for the laser
        super().__init__(pin)
        super().value(1)
    def rand(self,): #sets up a random state for the laser
        i = random.randint(0,100)
        if i >= 5: #setting this value defines the %chance of the laser switching off
            super().value(1)
        else:
            super().value(0)

laser  = Laser(17)

class Servo(PWM): #a class within a class with another class, to define the servos
    def __init__(self, pin: Pin, mode, imin, imax):
        super().__init__(pin)
        if mode == 1: #big servo
            self.MIN = 814000 #range of ns PWM signal
            self.MAX = 2200000
        elif mode == 2: #little black servo
            self.MIN = 340000 #range of ns PWM signal
            self.MAX = 2647000
        elif mode == 3:
            self.MIN = 814000 #range of ns PWM signal
            self.MAX = 2200000
        self.STEP = (self.MAX - self.MIN)/100
        self.pmin = imin #percentage range of allowed movement, will be updated afterwards if needed
        self.pmax = imax
        super().freq(50)
        super().duty_ns(int((50 * self.STEP)+self.MIN))
        delay(1)
    def rand(self,): #defines a random move for the servo, within the defined range
        super().duty_ns(int((random.randint(self.pmin, self.pmax) * self.STEP)+self.MIN))
    def min(self,): #move servo to minimum value
        super().duty_ns(int((self.pmin * self.STEP)+self.MIN))
    def max(self,): #move servo to maximum value
        super().duty_ns(int((self.pmax * self.STEP)+self.MIN))
    def go(self,pos): #move servo to a defined %position
        super().duty_ns(int((pos * self.STEP)+self.MIN))
        delay(0)
    def park(self,): #stop the servo twitching when it's not doing anything
        super().duty_ns(0)

servo1 = Servo(Pin(28), 1, 40, 60)
servo1.park()
servo2 = Servo(Pin(27), 2, 45, 60)
servo2.park()
laser.value(0)

switch = Pin(22, Pin.IN)
run_time_min  = 5   #how many minutes it should run
run_time_s = int(60.0 * run_time_min)
################################################################
while True: #while loop is where the code runs in a nonstop loop on the pico
    if switch.value() == 1:
        deadline = time.time() + run_time_s #sets up a timer after touching the switch
        while time.time() - deadline < 0:
            servo1.rand()
            servo2.rand()
            laser.rand()
            hodl()
            led.toggle()
    else:
        laser.value(0)
        led.value(1)
        servo1.park()
        servo2.park()
        delay(0.25)
