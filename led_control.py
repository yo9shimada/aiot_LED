import tkinter as tk
import RPi.GPIO as GPIO
#GPIO.setwarnings(False)
# メインウィンドウ
root = tk.Tk()
root.title("RGB LED Control")
root.geometry("300x200+100+100")
 
LED = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
pwmLED = GPIO.PWM(LED, 500)
pwmLED.start(0)
 
def updateLED(duty):
    pwmLED.ChangeDutyCycle(float(duty))
 
s = tk.Scale(root, label = 'LED', orient = 'h',
           from_ = 0, to = 100, command = updateLED)
 
# ウィジェットの配置
s.pack(fill = 'both')
 
# メインループ
root.mainloop()
print("GPIO cleanup")
GPIO.cleanup()