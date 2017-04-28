import RPi.GPIO as GPIO
import random
import getpass
GPIO.setmode(GPIO.BOARD)
y= random.randint(1000,2000)
print y
z = getpass.getpass("enter otp:").lower()
for i in range(0,1):
            print "****"

OTP=int(z)
if(y == OTP ):
	
        print "open...."

else:
        print "invalid otp"

MATRIX =[[1,2,3,'A'],[4,5,6,'B'],[7,8,9,'C'],['*',0,'#','D']]
k=0
row=[7,11,13,15]
col=[12,16,18,22]
for j in range(4):
		GPIO.setup(col[j],GPIO.OUT)
		GPIO.output(col[j],1)
for i in range(4):
		GPIO.setup(row[i],GPIO.IN,pull_up_down=GPIO.PUD_UP)
h=""
while(k<=3):

	for j in range(4):
		GPIO.output(col[j],0)
		for i in range(4):
			if GPIO.input(row[i])==0:
				k+=1
				MATRIX[i][j]

				NEW_ARRAY = map(list,MATRIX)
				MATRIX[i][j]
				h= h + str(NEW_ARRAY[i][j])
				print h
				while(GPIO.input(row[i])==0):
					pass
						
		GPIO.output(col[j],1)


compareKey = int(h)
comp=cmp(OTP,compareKey)
if(comp==0):
	print'otp  match'
else:
	print"does not match"

