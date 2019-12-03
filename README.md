# Portfolio 2

This portfolio 2 for the Linux for Embedded Systems course at SDU contains 
the code necessary for a robot that can follow a wall autonomously as reliably and quickly as possible. 
The robot accepts start and stop commands via an ad-hoc wireless network. It also support requests for sensor and control parameters.
The assignment is solved by using the Pi Zero and CamJam EduKit 3.

## Getting Started

To get the project: https://github.com/askebm/PORT2-LIN.git

### Prerequisites

For properly using the project the following are required.
 * Python3
 * socat

## Running the program

Set up the pi such that its running main_pi_zero.sh. Thus socat can be run on
host and send commands like "start", "stop", "getdist" and "getmotors" 
