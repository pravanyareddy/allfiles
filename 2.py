import getpass
import datetime
import csv
import RPi.GPIO as GPIO

full_date = str(datetime.datetime.now())
short_date = full_date[5:10]
print(short_date)
while True:
    while True:
        try:
            ID = getpass.getpass(prompt = 'Please swipe your ID card. ')
            if GPIO.path.exists('.\attendance.csv'):
                  student_number = open('.\attendance.csv', 'a')
                  student_number.write(ID[1:10] + '\n')
                  print(' ')
            else:
                  student_number = open('.\attendance.csv', 'w')
                  student_number.write(ID[1:10] + '\n')
                  print(' ')
