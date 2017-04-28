import RPi.GPIO as GPIO
import time
import MFRC522
import signal
import getpass
continue_reading = True
GPIO_CLEANED_UP = False
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def end_read(signal,frame):
    global continue_reading
    global GPIO_CLEANED_UP
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    if (GPIO_CLEANED_UP == False):
        GPIO.cleanup()
signal.signal(signal.SIGINT, end_read)
