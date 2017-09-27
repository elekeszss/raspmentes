import RPi.GPIO as GPIO
from time import sleep

sleepTime = 1
ledPin = 13
def callLED():
    # Setup the LED
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    # Turn it on, sleep for a bit, then turn it off.
    GPIO.output(ledPin, GPIO.HIGH)
    sleep(sleepTime)
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.cleanup()

callLED()