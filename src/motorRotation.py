import RPi.GPIO as GPIO
import time

control_pin = 12

def rotate():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(control_pin, GPIO.OUT)
    p = GPIO.PWM(control_pin, 50)
    p.start(2.5)
    try:
        timer = 0
        while True:
            if timer%2 == 0:
                for i in range(0, 180, 10):
                    if i % 20 == 0:
                        p.ChangeDutyCycle(1/18* (i) + 2.5)
                    else:
                        p.ChangeDutyCycle(1/18* (i-10) + 2.5)
                    time.sleep(1)
            else:
                for i in range(180, 0, -10):
                    if i % 20 == 0:
                        p.ChangeDutyCycle(1/18* (i) + 2.5)
                    else:
                        p.ChangeDutyCycle(1/18* (i-10) + 2.5)
                    time.sleep(1)
                
            timer += 1
            time.sleep(5)
            
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()
