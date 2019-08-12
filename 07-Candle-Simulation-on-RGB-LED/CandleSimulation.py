from random import randint
import unicornhat as unicorn
import math
import random
import time

intensity = 0.75
unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
width,height=unicorn.get_shape()

def rand_flicker_sleep():
    time.sleep(random.randint(3,10) / 100.0)

while True:
    x = randint(0, (width-1))
    y = randint(0, (height-1))
    r = randint(75, 100)
    g = randint(33, 44)
    b = 0
    r_intensity = math.pow(intensity + 0.1, 0.75)
    unicorn.brightness(r_intensity)
    unicorn.set_pixel(x, y, r, g, b)
    unicorn.show()
    rand_flicker_sleep()
