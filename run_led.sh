#!/bin/bash

GPIO=22

# Initialize GPIO22 for output.  You'll
# get a warning if the GPIO is already in use.
echo $GPIO > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio$GPIO/direction


# Flip it on and off every second
while true; do
    echo 0 > /sys/class/gpio/gpio$GPIO/value
    sleep 1s # s, m, h, or d
    echo 1 > /sys/class/gpio/gpio$GPIO/value
    sleep 1s # s, m, h, or d
done

echo "Goodbye."