#!/usr/bin/python3

import time as tm

import ev3dev.ev3 as e3

motor = e3.LargeMotor ('outA')
button = e3.TouchSensor ('in1')

startTime = 0

while True:
    currentTime = tm.time ()
    
    if button.value ():    
        startTime = currentTime
        
    if currentTime - startTime < 3:  
        e3.Leds.set_color (e3.Leds.LEFT, e3.Leds.RED)
        motor.run_direct (duty_cycle_sp = 100)
    else:
        e3.Leds.set_color (e3.Leds.LEFT, e3.Leds.GREEN)
        motor.reset ()
        
    tm.sleep (0.1)