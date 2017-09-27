import RPi.GPIO as GPIO
from time import sleep

sleepTime = 1
ledPin = [13,11]
def relayon1():
    # Setup the LED
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    # Turn it on, sleep for a bit, then turn it off.
    GPIO.output(11, True)
    
def relayoff1():
    # Setup the LED
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    # Turn it on, sleep for a bit, then turn it off.
    GPIO.output(11, False)
    GPIO.cleanup(11)
    

def relayon2():
    # Setup the LED
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13, GPIO.OUT)
    # Turn it on, sleep for a bit, then turn it off.
    GPIO.output(13, True)
    
def relayoff2():
    # Setup the LED
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13, GPIO.OUT)
    # Turn it on, sleep for a bit, then turn it off.
    GPIO.output(13, False)
    GPIO.cleanup(13)