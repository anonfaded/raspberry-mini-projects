# Official guide: >>> https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico

# Manually set switch to zero and one to turn on and off the LED.
from machine import Pin

# blue led light
led = Pin(25, Pin.OUT)

# 1 = on, 0 = off
led.value(0)





# Toggle the light with the run button clicks
from machine import Pin
led = Pin(25, Pin.OUT)

led.toggle()






# Blink the led light with different frequencies
from machine import Pin, Timer
led = Pin(25, Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()

timer.init(freq=10, mode=Timer.PERIODIC, callback=blink)
