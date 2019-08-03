"""
Name: Azhar Ebrahim
Student number: EBRAZH001
Prac: 1
Date: July

"""
import RPi.GPIO as GPIO
from time import sleep            #import libraries

print "3-Bit Binary Counter"

GPIO.setwarnings(0)
GPIO.setmode(GPIO.BOARD)           #set to board mode

GPIO.setup(33, GPIO.OUT)           #init LED's
GPIO.setup(37, GPIO.OUT)
GPIO.setup(7,  GPIO.OUT)

GPIO.setup(16, GPIO.IN, pull_up_down= GPIO.PUD_UP)           #init push buttons
GPIO.setup(18, GPIO.IN, pull_up_down= GPIO.PUD_UP)

x=0
cnt=0
y=0

def my_callback_one(channel1):                                              #function definition
			global cnt
			x=0
			y=0

			if GPIO.event_detected(16):                          #check if butto pressed
				print "Pressed 1"
				x=1

				cnt+=1%8
				GPIO.output(33, cnt & 0x01)                     #upward counter output to LED's
				GPIO.output(37, cnt & 0x02)
				GPIO.output(7,  cnt & 0x04)
				sleep(0.1)                                      #sleep function of 0.1 seconds

def my_callback_two(chanel2):
			global cnt
			y=0
			if GPIO.event_detected(18):
				print "Pressed 2"
				y=1

				cnt-=1%8
				GPIO.output(33, cnt & 0x01)
				GPIO.output(37, cnt & 0x02)
				GPIO.output(7,  cnt & 0x04)
				sleep(0.1)

GPIO.add_event_detect(16,GPIO.RISING, callback=my_callback_one, bouncetime=50)
GPIO.add_event_detect(18,GPIO.RISING, callback=my_callback_two, bouncetime=50)

while(1):
	c=10
