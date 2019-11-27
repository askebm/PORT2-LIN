
import time
from gpiozero import CamJamKitRobot
from gpiozero import DistanceSensor

pinTrigger = 17
pinEcho = 18

robot = CamJamKitRobot()
sensor = DistanceSensor(echo=pinEcho, trigger=pinTrigger)

delta = 15
rightLimit = delta + 2
leftLimit = delta - 2

sleeptime = 0.001


motorspeed = 0.25
motorforward = (motorspeed, motorspeed)
motorbackward = (-motorspeed, -motorspeed)
motorleft = (motorspeed, 0)
motorright = (0, motorspeed)

while True:
    try:
        dist = sensor.distance * 100
        if (dist < leftLimit):
            print(" | Motor Left: %f | Motor Right: %f | " % (motorspeed,0) )
        elif (dist < rightLimit):
            print(" | Motor Left: %f | Motor Right: %f | " % (motorspeed,motorspeed))
        else:
            print(" | Motor Left: %f | Motor Right: %f | " % (0,motorspeed))
        break
    except:
        1+1
