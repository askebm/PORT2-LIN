#!/bin/bash

#socat tcp-listen:8080,reuseaddr,fork exec:'echo' $INPUT
read INPUT

case "$INPUT" in
    "start")
        python3 /home/pi/PORT2/0-wallfollower.py 1> /dev/null 2> /dev/null
        ;;
    "stop")
        killall python3 1> /dev/null 2> /dev/null
        ;;
    "getdist")
        #python3 /home/pi/getdist.py 2> /dev/null
	cat /tmp/DISTANCE 2> /dev/null
        ;;
    "getmotors")
	#python3 /home/pi/getmotor.py 1>/tmp/getmotorsDATA 2> /dev/null
	cat /tmp/MOTORS 2> /dev/null
        ;; 
esac
