import RPi.GPIO as GPIO
import time
import random
import getpass
from datetime import datetime
# Define GPIO to LCD mapping
LCD_RS = 7
LCD_E  = 8
LCD_D4 = 29
LCD_D5 = 31
LCD_D6 = 32
LCD_D7 = 33

# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

def main():
  # Main program block
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BOARD)       # Use BCM GPIO numbers
  GPIO.setup(LCD_E, GPIO.OUT)  # E
  GPIO.setup(LCD_RS, GPIO.OUT) # RS
  GPIO.setup(LCD_D4, GPIO.OUT) # DB4
  GPIO.setup(LCD_D5, GPIO.OUT) # DB5
  GPIO.setup(LCD_D6, GPIO.OUT) # DB6
  GPIO.setup(LCD_D7, GPIO.OUT) # DB7

  # Initialise display
  lcd_init()
  s=0
  while (s==0):

    # Send some test
     lcd_string("   CYKUL Dock   ",LCD_LINE_1)
     lcd_string("    WELCOME    ",LCD_LINE_2)

     time.sleep(3) 
    # 3 second dela
    # Send some text
     lcd_string("SCAN SMART CARD",LCD_LINE_1)
     lcd_string(" ",LCD_LINE_2)
    # lcd_string("....",LCD_LINE_2)
     time.sleep(3) # 3 second delay
    # callKeypad()
    # output = ""
    # i = datetime.now()
    # output = i.strftime("%d/%m/%Y %H:%M:%S")
    # lcd_string(output,LCD_LINE_1)

    # time.sleep(3)
     s+=1
     messageCatched = ""

     messageCatched =  callKeypadDisplay()
     messageCatched =  callSolenoid()

    # callKeypadDisplay()

def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display

  time.sleep(E_DELAY)

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character lcd_init()

  #        False for command

  GPIO.output(LCD_RS, mode) # RS

  # High bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)

  # Toggle 'Enable' pin
  lcd_toggle_enable()

  # Low bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)

  # Toggle 'Enable' pin
  lcd_toggle_enable()

def lcd_toggle_enable():
  # Toggle enable
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)

def lcd_string(message,line):
  # Send string to display

  message = message.ljust(LCD_WIDTH," ")

  lcd_byte(line, LCD_CMD)

  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)



## Keypad Interface Started

def callKeypadDisplay():
     GPIO.setwarnings(False)
     GPIO.setmode(GPIO.BOARD)
     y= random.randint(1000,2000)
     #z = getpass.getpass("enter otp:").lower()
     enteredOTP = "OTP:" + str(y)
     lcd_string(enteredOTP,LCD_LINE_1)
     MATRIX =[[1,2,3,'A'],[4,5,6,'B'],[7,8,9,'C'],['*',0,'#','D']]
     k=0
     row=[38,11,13,15]
     col=[12,16,18,22]
     for j in range(4):
          GPIO.setup(col[j],GPIO.OUT)
          GPIO.output(col[j],1)
     for i in range(4):
          GPIO.setup(row[i],GPIO.IN,pull_up_down=GPIO.PUD_UP)
     h=""
     #enteredOTP = "Enter OTP:"
     while(k<=3):

          for j in range(4):
	       GPIO.output(col[j],0)
	       for i in range(4):
	            if GPIO.input(row[i])==0:
		         #enteredOTP = "Enter OTP:"
                         k+=1
			 MATRIX[i][j]
			 NEW_ARRAY = map(list,MATRIX)
			 MATRIX[i][j]
			 h= h + str(NEW_ARRAY[i][j])
			 
			 # lcd_byte(0x33,LCD_CMD)
                         #enteredOTP += h 
			 lcd_string(h,LCD_LINE_2)
			 while(GPIO.input(row[i])==0):
			      pass
						
	       GPIO.output(col[j],1)


     #enteredOTP += h 
     #lcd_string(enteredOTP,LCD_LINE_1)
     compareKey = int(h)
     comp=cmp(y,compareKey)
     result = ""
     if(comp==0):
          result =  "OTP Matched"
     else:
	result = "Did Not Match"

     lcd_string(result,LCD_LINE_2)
     time.sleep(5)
def callSolenoid():
     GPIO.setwarnings(False)
     GPIO.setmode(GPIO.BOARD)
     GPIO.setup(35,GPIO.OUT)

     while(True):
                compareKey = int(h)
                comp=cmp(y,compareKey)
                result = ""
                if (comp==0):
			GPIO.output(35,1)
                        print "ON"
                        time.sleep(8)
			GPIO.output(35,0)
			print "OFF"

                else:
                        GPIO.output(35,0)

      
     return result

      

if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd_byte(0x01, LCD_CMD)
    GPIO.cleanup()


