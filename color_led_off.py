import RPi.GPIO as GPIO
import time
 
#GPIO.cleanup()
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)    # Red
GPIO.setup(23, GPIO.OUT)    # Blue
GPIO.setup(24, GPIO.OUT)    # Green
 
pwmRed = GPIO.PWM(18,500)
pwmRed.start(0)
 
pwmBlue =GPIO.PWM(23,500)
pwmBlue.start(0)
 
pwmGreen = GPIO.PWM(24,500)
pwmGreen.start(0)
 
GPIO.cleanup()