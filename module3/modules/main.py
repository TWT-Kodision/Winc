# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line
import this
import time
import math
from datetime import datetime
import sys
from greety import supergreeting

def wait(seconds):
    seconds_start= time.time()
    while (time.time() < (seconds_start + seconds)):
        print()

def my_sin(float):
    sine = math.sin(float)
    return sine

def iso_now():
    now = datetime.now()
    date_time = now.strftime('%Y-%m-%dT%H:%M')
    return date_time

def platform():
    return sys.platform

def supergreeting_wrapper(name):
    return supergreeting(name)

print(supergreeting_wrapper('test'))

