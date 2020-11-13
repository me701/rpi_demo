from w1thermsensor import W1ThermSensor
import time 

sensor = W1ThermSensor()

while True:
    C = sensor.get_temperature()
    F = 9*C/5.0 + 32.0
    t = time.asctime( time.localtime(time.time()) )
    print("{} and T={:.2f} °F".format(t, F))
    time.sleep(2.0)