import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT)
while(True):
	GPIO.output(18,0)
	print "ON"
	time.sleep(3)
	GPIO.output(18,1)
	print "OFF"
	time.sleep(3)
GPIO.cleanup()



























































	
































































