"""
gpiozero makes some things very easy, but 
it helps to have a bit more control.  here's
the same example with the button and led
using the lower-level RPi module.
"""

import RPi.GPIO as GPIO
from signal import pause

# BCM lets us reference pins by GPIO number.
GPIO.setmode(GPIO.BCM)

# Set the two pins
button = 13
led = 22
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Pulls up to 3.3v when closed, so 0v is "on"
GPIO.setup(led, GPIO.OUT)

def callback(pin):
    if GPIO.input(button):
        GPIO.output(led, 0)
    else:
        print("pressed!")
        GPIO.output(led, 1)


GPIO.add_event_detect(button, GPIO.BOTH, callback)

pause()
