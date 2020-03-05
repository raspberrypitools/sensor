#!/usr/bin/env python
# by shumeipai.net
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, 1)
Prev = []

while True:
    Sig = GPIO.input(4)
    print '---------',Prev
    if len(Prev) > 99:
        Avg = 0
        for A in Prev:
            Avg = Avg + A
            Avg = Avg / 100.00
            Prev = []
            print Avg * 100
        else:
            Prev.append(Sig)
            time.sleep(0.0003)
            print '==='
