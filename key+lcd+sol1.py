import RPi.GPIO as GPIO
import time
import random
import getpass
import MFRC522
import signal
from datetime import datetime
continue_reading = True
GPIO_CLEANED_UP  = False
GPIO.setmode(GPIO.BOARD)

def card():
    signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
    MIFAREReader = MFRC522.MFRC522()
    approved_list=("136412199","13645228")
# Welcome message
    print "Welcome to the MFRC522 data read example"
    print "Press Ctrl-C to stop."
    while continue_reading:

    # Scan for cards    
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
        if status == MIFAREReader.MI_OK:
            print "Card detected"
           # return 1
#            lcd_string("Card Detected",LCD_LINE_1)


    # Get the UID of the card
        (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
        if status == MIFAREReader.MI_OK:

        # Print UID
        #print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+",$
            tot_uid =  str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])
            print (tot_uid)
            if (tot_uid in approved_list):
                print ("Approved")
 #               return 1
 #               lcd_string("Card Approved",LCD_LINE_2)
                callKeypadDisplay()
                display=""
                display=callKeypadDisplay()
                if(display==0):
                     turn_sol()
                else:
                     pass
                # exit(1)
            else:
                print ("Not Approved")
  #              lcd_string("Not Approved",LCD_LINE_2)



# Define GPIO to LCD mapping
LCD_RS = 7
LCD_E  = 8
LCD_D4 = 40
LCD_D5 =  GNU nano 2.2.6                                                             File: rfid1_lcd1.py                                                                                                                        M$

     if(comp==0):
          result =  "OTP Matched"
     else:
        result = "Did Not Match"

 #    lcd_string(result,LCD_LINE_2)
     time.sleep(5)
     return result
def turn_sol():
      GPIO.setmode(GPIO.BOARD)
      GPIO.setup(38, GPIO.OUT)
      x=0
      while(x==0):
          GPIO.output(38,0)
          print'on'
          time.sleep(3)
         print'off'
  #        lcd_string(result,LCD_LINE_2)
          GPIO.output(38, 1)
          x+=1
   #       return

def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    if(GPIO_CLEANED_UP==False):
                pass



if __name__ == '__main__':

  try:
    main()

  except KeyboardInterrupt:

    pass
  finally:
#    pass
    lcd_byte(0x01,LCD_CMD)

    GPIO.cleanup()

