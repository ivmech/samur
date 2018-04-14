import os
import sys
import select
import RPi.GPIO as GPIO
import smbus2
from time import sleep

from devices import ShiftRegister
from devices import Multiplexer
from devices import DigitalModule

class Mainboard:

    def __init__(self):
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        dataPinP = 18   #pin 14 on the 74HC595
        latchPinP = 17  #pin 12 on the 74HC595
        clockPinP = 4   #pin 11 on the 74HC595

        dataPinR = 24   #pin 14 on the 74HC595
        latchPinR = 23  #pin 12 on the 74HC595
        clockPinR = 27  #pin 11 on the 74HC595

        # 74HC4067
        S0Pin = 5
        S1Pin = 6
        S2Pin = 12
        S3Pin = 13
        COMPin = 7

        # Number of Relays
        relay_num = 12

        self.relaysP = ShiftRegister(dataPinP, latchPinP, clockPinP)
        self.relaysR = ShiftRegister(dataPinR, latchPinR, clockPinR)
        self.lineInputs = Multiplexer(S0Pin, S1Pin, S2Pin, S3Pin, COMPin)
        self.digitalModules = self.scanModule()

        self.RELAYS = {}
        self.INPUTS = []

        for i in range(relay_num):
            if i<8:
                self.RELAYS["K"+str(i+1)] = (i, self.relaysP.output)
            else:
                self.RELAYS["K"+str(i+1)] = (i-8, self.relaysR.output)

        for j,m in enumerate(self.digitalModules):
            for i in range(6):
                self.RELAYS["K"+str(relay_num + j * 6 + i + 1)] = (i, m.output)

        for i in range(3):
            self.RELAYS["V"+str(i+1)] = (4+i, self.relaysR.output)

        for i in range(14):
            if i < 8:
                self.INPUTS.append("L"+str(i+1))
            else:
                self.INPUTS.append("D"+str(i+1-8))


    def digitalWrite(self, name, state):
        try:
            value = self.RELAYS[name]
            value[1](value[0], state)
        except:
            pass

    def digitalRead(self, name):
        inputs = self.lineInputs.read()
        try:
            index = self.INPUTS.index(name)
        except:
            raise
#        d = dict(zip(self.INPUTS, inputs))
        return inputs[index]

    def digitalReadAll(self):
        inputs = self.lineInputs.read()
        return inputs[:14]

    def scanModule(self):
        modules = []
        bus = smbus2.SMBus(1)
        for address in range(32,40):
            try:
                bus.read_byte(address)
                modules.append(DigitalModule(address))
            except:
                pass
        return modules

if __name__ == "__main__":
    app = Mainboard()
    while True:
        print app.digitalReadAll()
        app.digitalWrite("K1", GPIO.HIGH)
        sleep(0.1)
        app.digitalWrite("K1", GPIO.LOW)
        sleep(0.1)
