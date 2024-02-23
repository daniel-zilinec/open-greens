from machine import Pin, PWM
import time

ON = 1
OFF = 0

print("OpenGreens v0.2 - KitchenGreens")
mg.light(1)
mg.pump(ON);		# Pump relay disconnects fan power supply
mg.fan(50);