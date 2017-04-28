import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)  # channel=12 frequency=50Hz
p.start(0)
try:
    while 1:
        for dc in range(0, 12, 5):
            p.ChangeDutyCycle(dc)
            print 'ON'
	    time.sleep(1)
        for dc in range(8, -1, -5):
            p.ChangeDutyCycle(dc)
	    print 'OFF'
            time.sleep(1)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
