import RPi.GPIO as GPIO
import time

control_pin = 12

def rotate():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(control_pin, GPIO.OUT)
    p = GPIO.PWM(control_pin, 50)
    p.start(2.5)
    try:
        while True:
            p.ChangeDutyCycle(10)
            time.sleep(1)
            '''
            p.ChangeDutyCycle(10)
            time.sleep(1)
            p.ChangeDutyCycle(25)
            time.sleep(1)
            '''
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()
