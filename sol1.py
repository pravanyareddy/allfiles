import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
for i in range(2):
	GPIO.output(18,GPIO.HIGH)
	GPIO.output(24,GPIO.HIGH)
	GPIO.output(11,GPIO.HIGH)
	print 'push..'
	time.sleep(3)
	GPIO.output(18,GPIO.LOW)
	GPIO.output(24,GPIO.low)
	GPIO.output(11,GPIO.LOW)
	print'pull'

