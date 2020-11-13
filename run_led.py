from gpiozero import LED
from time import sleep

GPIO = 22
led = LED(GPIO)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
