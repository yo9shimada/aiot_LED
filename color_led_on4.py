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
 
while True:
    for r in range(100):
        pwmRed.ChangeDutyCycle(r)
        pwmGreen.ChangeDutyCycle(0)
        pwmBlue.ChangeDutyCycle(100 - r)
        time.sleep(0.02)        
    for b in range(100):
        pwmRed.ChangeDutyCycle(100 - b)
        pwmGreen.ChangeDutyCycle(b)
        pwmBlue.ChangeDutyCycle(0)
        time.sleep(0.02)
    for g in range(100):
        pwmRed.ChangeDutyCycle(0)
        pwmGreen.ChangeDutyCycle(100 - g)
        pwmBlue.ChangeDutyCycle(g)
        time.sleep(0.02)