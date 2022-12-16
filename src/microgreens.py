from machine import Pin, PWM
import time

ON = 1
OFF = 0

class Microgreens:

    def __init__(self):
        # fan_pin = Pin(4, Pin.OUT)
        self.pump_pin = Pin(2, Pin.OUT)
        self.light_pin = Pin(0, Pin.OUT)
        self.fan_pwm = PWM(Pin(4))
        self.fan_pwm.freq(25000)
        self.pump(OFF)
        self.lingth(0)
        self.fan(0)
        
    def pump(self, value):
        if value == ON:
            self.pump_pin.value(0)
        else:
            self.pump_pin.value(1)
            
    def light(self, value):
        if value == ON:
            self.light_pin.value(0)
        else:
            self.light_pin.value(1)
            
    def fan(self, percentage):
        value = (percentage * 1023) / 100
        if value > 1023:
            value = 1023
        self.fan_pwm.duty(int(value))


    def pump_time(self, duration):
        self.pump(ON)
        time.sleep(duration)
        self.pump(OFF)
