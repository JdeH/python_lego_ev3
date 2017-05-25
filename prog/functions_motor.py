#!/usr/bin/python3

import time as tm

import ev3dev.ev3 as e3

def tell (message):
    print (message)
    e3.Sound.speak (message)

tell ('The program was started')
tm.sleep (2)

e3.Leds.all_off ()
e3.Leds.set_color (e3.Leds.LEFT, e3.Leds.GREEN)
        
motor = e3.LargeMotor ('outA')
button = e3.TouchSensor ('in1')

startTime = 0
isActive = False

while True:
    currentTime = tm.time ()
    
    if button.value ():    
        startTime = currentTime
    
    wasActive = isActive
    isActive = currentTime - startTime < 10
       
    if isActive and not wasActive:
        tell ('The motor was started')
        e3.Leds.set_color (e3.Leds.LEFT, e3.Leds.RED)
        motor.run_direct (duty_cycle_sp = 100)
        
    if not isActive and wasActive:
        tell ('The motor was stopped')
        e3.Leds.set_color (e3.Leds.LEFT, e3.Leds.GREEN)
        motor.reset ()
        
    tm.sleep (0.1)
    
