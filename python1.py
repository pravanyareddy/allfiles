import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

while True:
   
    GPIO.output(12, 1)
    print 'ON'
    time.sleep(2)
    GPIO.output(12, 0)
    print 'OFF'
    time.sleep(2)
GPIO.cleanup()
