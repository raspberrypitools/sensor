# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO

BODY_GPIO = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(BODY_GPIO, GPIO.IN)

def body_detect():
    signal = GPIO.input(BODY_GPIO)
    if signal == 1:
        print "DETECT BODY!"
    else:
        print "NO BODY!"

if __name__ == "__main__":
    count = 0
    while True:
        body_detect()
        time.sleep(2)
        count += 1
        #if count == 20:
        #    break
    GPIO.cleanup()
