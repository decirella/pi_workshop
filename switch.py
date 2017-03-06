import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

# GPIO pin 6 used for push button switch
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO pin 7 used for LED
GPIO.setup(7, GPIO.OUT)


# the while loop continuisly reads the pi status the switch is wired to
while True:
    input_state = GPIO.input(6)
    if input_state == False:
        print('Button Pressed') # output to terminal
        GPIO.output(7,GPIO.HIGH) # LED brightly lit for 1 second
        time.sleep(o.21) 
        GPIO.output(7,GPIO.LOW)
        time.sleep(0.2)
