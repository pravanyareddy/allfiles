import RPi.GPIO as GPIO
import getpass
import time


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
   	
def digit():
        digitPressed = "A"
        while digitPressed == "A":
              digitPressed = kp.getKey()
        return digitPressed
	digitPressed = "B"
	while digitPressed == "B":
	      digitPressed = kp.getKey()
	return digitPressed
          
if __name__ == '__main__':

  try:
     main()
  except KeyBoardInterrupt:
  pass

GPIO.cleanup()

