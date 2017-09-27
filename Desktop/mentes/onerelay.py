#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# init list with pin numbers

pinList = [11,13]

# loop through pins and set mode and state to 'high'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = 5

# main loop

try:
  GPIO.output(11, GPIO.HIGH)
  print "HIGH"
  GPIO.output(13, GPIO.HIGH)
  print "HIGH"
  time.sleep(5);
  GPIO.output(11,GPIO.LOW)
  print "LOW"
  GPIO.output(13,GPIO.LOW)
  print "LOW" 

  GPIO.cleanup()
  print "Good bye!"

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()