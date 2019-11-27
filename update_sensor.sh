#!/bin/bash

while sleep 1; do
	VAR=$(python3 /home/pi/PORT2/getdist.py)
	echo $VAR > /tmp/DISTANCE
	VAR=$(python3 /home/pi/PORT2/getmotor.py)
	echo $VAR > /tmp/MOTORS
done
