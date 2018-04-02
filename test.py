import os
import sys
import select
import RPi.GPIO as GPIO
from time import sleep

import samur

MB = samur.Mainboard()

relay_delay = 0.05

if __name__ == "__main__":
    try:
        while 1:
            for i in range(15):
                if i<8:
                    MB.relaysP.output(i, GPIO.HIGH)
                else:
                    MB.relaysR.output(i-8, GPIO.HIGH)
                sleep(relay_delay)

            for i in range(15):
                if i<8:
                    MB.relaysP.output(i, GPIO.LOW)
                else:
                    MB.relaysR.output(i-8, GPIO.LOW)
                sleep(relay_delay)


#            MB.digitalWrite("K1", GPIO.HIGH)
#            sleep(0.1)
#            MB.digitalWrite("K1", GPIO.LOW)
            sleep(relay_delay)

    except KeyboardInterrupt:
        print "\rCtrl-C - Quit."
        GPIO.cleanup()
