from gpiozero import LED, Button
from signal import pause

led = LED(22)
button = Button(13)

button.when_pressed = led.on
button.when_released = led.off

pause()
