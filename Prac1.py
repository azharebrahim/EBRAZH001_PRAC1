"""
Name: Azhar Ebrahim
Student number: EBRAZH001
Prac: 1
Date: July

"""
import RPi.GPIO as GPIO
from time import sleep

print "3-Bit Binary Counter"

GPIO.setwarnings(0)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(33, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(7,  GPIO.OUT)

GPIO.setup(16, GPIO.IN, pull_up_down= GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down= GPIO.PUD_UP)
