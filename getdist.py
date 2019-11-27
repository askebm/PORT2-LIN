

import time
from gpiozero import CamJamKitRobot
from gpiozero import DistanceSensor

pinTrigger = 17
pinEcho = 18

sensor = DistanceSensor(echo=pinEcho, trigger=pinTrigger)

while True:
    try:
        dist = sensor.distance * 100
        print("Sensor distance: %.1f cm" % (dist) )
        break
    except:
        1+1





