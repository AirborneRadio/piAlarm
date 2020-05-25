import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(0)
GPIO.setmode(GPIO.BCM)
buzzer=9
GPIO.setup(buzzer,GPIO.OUT)

p = GPIO.PWM(buzzer, 6000)
p.start(1)
input('press enter to stop')
p.stop()
GPIO.cleanup()