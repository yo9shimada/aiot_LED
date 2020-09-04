#! /usr/bin/env python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        print( GPIO.input(9) )
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
