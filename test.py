import os
import sys
import select
import RPi.GPIO as GPIO
from time import sleep

import samur

MB = samur.Mainboard()

relay_delay = 0.1

if __name__ == "__main__":
    try:
        while 1:
            for i in range(15):
                MB.relays.output(i, GPIO.HIGH)
                sleep(relay_delay)

            for i in range(15):
                MB.relays.output(i, GPIO.LOW)
                sleep(relay_delay)

#            sleep(0.1)
#            MB.digitalWrite("K1", GPIO.LOW)
            sleep(relay_delay)

    except KeyboardInterrupt:
        print "\rCtrl-C - Quit."
        for i in range(15):
            MB.relays.output(i, GPIO.LOW)
        GPIO.cleanup()
