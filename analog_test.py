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
            print [MB.analogRead(_) for _ in MB.AINPUTS]
            MB.analogWrite("S1", 500)
            MB.analogWrite("S2", 500)
            MB.analogWrite("S3", 0)
            MB.analogWrite("S4", 0)
            pass

    except KeyboardInterrupt:
        print "\rCtrl-C - Quit."
        GPIO.cleanup()
