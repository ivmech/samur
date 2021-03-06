# Samur MainBoard Python Module

REQUIREMENTS
--------

* RPi.GPIO
* smbus2
* Python 2.7 to 3.6.

INSTALL
--------

If you like to install from PiP, you can do it like so:

```bash
pip install samur
```

If you like to clone from source, you can do it like so:

```bash
git clone https://github.com/ivmech/samur.git
```

If you have downloaded the source code:

```bash
    cd samur
    sudo python setup.py install
```

RUNNING TESTS
--------

```python
import samur
MB = samur.Mainboard()
MB.digitalWrite("K1", 1)    # K1 named relay output High
MB.digitalWrite("K1", 0)    # K1 named relay output Low
print MB.digitalReadAll()   # reading all inputs

print MB.analogRead("A1")   # reading analog value
MB.analogWrite("S1", 500)   # analog output
```

Features
--------

* [x] MainBoard
* [x] Output Support
* [x] Input Support
* [x] DigitalModule Support
* [X] AnalogModule Support
* [x] I2C Expansion Support

Authors
-------

Ivmech Mechatronics Ltd.
