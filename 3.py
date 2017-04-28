import RPi.GPIO as GPIO
import spi
import signal
class MFRC522:
     
serNum = []
   

def __init__(self, dev='/dev/spidev0.0', spd=1000000):
     spi.openSPI(device=dev,speed=spd)
     GPIO.setmode(GPIO.BOARD)
     GPIO.setup(22, GPIO.OUT)

def MFRC522_Reset(self):
     self.Write_MFRC522(self.CommandReg, self.PCD_RESETPHASE)
   
def Write_MFRC522(self, addr, val):
     spi.transfer(((addr<<1)&0x7E,val))
   
def Read_MFRC522(self, addr):
     val = spi.transfer((((addr<<1)&0x7E) | 0x80,0))
     return val[1]


def end_read(signal,frame):
             print "Authentication error"
 
         # Make sure to stop scanning for cards

        continue_reading = False

