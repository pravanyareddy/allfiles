import RPi.GPIO as GPIO
import getpass
import time

def main():

  key_init()

  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BOARD)
def key_init(): 

  # Initialise display
  key_byte(0x01,VK_LBUTTON) # Move Left
  key_byte(0x02,VK_RBUTTON) # Move Right
  key_byte(0x0C,VK_CLEAR)   # Clear all
  key_byte(0x2E,VK_DELETE)  # Delete
  key_byte(0x2F,VK_HELP)    # Help
  key_byte(0x0D,VK_RETURN)  # Enter


MATRIX = [[1,2,3,"A"],[4,5,6,"B"],[7,8,9,"C"],["*",0,"#","D"]]
k=0
ROW = [7,11,13,15]
COL = [12,16,18,22]

 
for j in range(4):
         GPIO.setup(COL[j], GPIO.OUT)
         GPIO.output(COL[j],1)

for i in range(4):
    
         GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

h=""
while(k<=3):
      for j in range(4):
		GPIO.output(COL[j],0)
           	for i in range(4):		        
                      if GPIO.input(ROW[i]) == 0:
			  k+=1	
                          MATRIX[i][j]
			  NEW_ARRAY = map(list,MATRIX)
			  MATRIX[i][j]
			  h= h + str(NEW_ARRAY[i][j])
			  print h
   			if (GPIO.input(MATRIX[i][j]) == "A"):
			    key_byte(0x01,VK_LBUTTON) 

                        if GPIO.input(MATRIX[i][j]) == "B":
 			    key_byte(0x02,VK_RBUTTON)            

		        if GPIO.input(MATRIX[i][j]) == "C":
                            key_byte(0x0C,VK_CLEAR)

                        if GPIO.input(MATRIX[i][j]) == "D":
  			    key_byte(0x2E,VK_DELETE)
			  
                        if GPIO.input(MATRIX[i][j]) == "*":
  			    key_byte(0x2F,VK_HELP)

                        if GPIO.input(MATRIX[i][j]) == "#":
			    key_byte(0x0D,VK_ENTER)
               
if __name__ == '__main__':

  try:
     main()
  except KeyBoardInterrupt:
  pass

GPIO.cleanup()

