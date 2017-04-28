import signal
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(SDA, GPIO.IN)

def read_rfid ():
   ser = serial.Serial ("/dev/ttyAMAO")
   ser.baudrate = 9600
   data = ser.read(12)
   ser.close()
   return data

id = read_rfid ()
print id
