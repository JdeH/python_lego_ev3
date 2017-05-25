#!/usr/bin/python3

import ev3dev.ev3 as ev3

import time

motor = ev3.LargeMotor ('outA')
button = ev3.TouchSensor ('in1')

while True:
    if button.value ():
        ev3.Leds.set_color (ev3.Leds.LEFT, ev3.Leds.GREEN)
        motor.run_direct (duty_cycle_sp = 100)
    else:
        ev3.Leds.all_off ()
        motor.reset ()
        
    time.sleep (0.1)
