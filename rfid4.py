import RPi.GPIO as GPIO
import MFRC522
import signal
import time

continue_reading = True
GPIO_CLEANED_UP = False


def end_read(signal,frame):
    global continue_reading
    global GPIO_CLEANED_UP
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    if (GPIO_CLEANED_UP == False):
        GPIO.cleanup()
signal.signal(signal.SIGINT, end_read)

def Blink(numTimes, speed):
    global GPIO_CLEANED_UP
    
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(11, GPIO.OUT) 
    
    for i in range(0,numTimes): 
        GPIO.output(11, True) 
        time.sleep(speed) 
        GPIO.output(11, False) 
        time.sleep(speed) 
    print ("Done") 
    GPIO.cleanup()
    GPIO_CLEANED_UP = True

def Brighten_Up (numTimes, wait):
    global GPIO_CLEANED_UP
    DC_Expo = 1
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(11, GPIO.OUT) 
    
    my_pwm = GPIO.PWM(11, 50)
    my_pwm.start(7)
    
    for i in range(0,numTimes): 
       
        my_pwm.ChangeDutyCycle(2**DC_Expo) 
        DC_Expo=DC_Expo+1
        time.sleep(wait) 
        
    print ("Done") 
    my_pwm.stop()
    GPIO.cleanup()
    GPIO_CLEANED_UP = True

def Turn_Lever():
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(11, GPIO.OUT)

    my_pwm = GPIO.PWM(11, 50)
    my_pwm.start(7)

    desiredPosition = input("Where do you want the servo? 0-10 :")
    my_pwm.ChangeDutyCycle(2)
    time.sleep(3)
    my_pwm.ChangeDutyCycle(3)

    my_pwm.stop()
    GPIO.cleanup()

MIFAREReader = MFRC522.MFRC522()


approved_list = ("136412199", "136424450")

print ("Welcome to the MFRC522 data read example")
print ("Press Ctrl-C to stop.")
print ("Will Start Reading Now:")

while continue_reading:
     
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

   
    if status == MIFAREReader.MI_OK:
        print ("Card detected")
    
    
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

   
    if status == MIFAREReader.MI_OK:
        
       
        tot_uid =  str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])
        print (tot_uid)
        if (tot_uid in approved_list):
            print ("Approved")
            
            Turn_Lever()
        else:
            print ("Not Approved")


