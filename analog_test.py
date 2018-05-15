import os
import sys
import select
import RPi.GPIO as GPIO
from time import sleep

import samur

MB = samur.Mainboard()

if __name__ == "__main__":
    try:
        while 1:
            

    except KeyboardInterrupt:
        print "\rCtrl-C - Quit."
        GPIO.cleanup()
