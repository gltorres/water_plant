#!/usr/bin/python

import RPi.GPIO as GPIO
import time

#this is the plant closer to the RPI
sensor_1 = 17
need_water_1 = 27
#this is the plant further from the RPI
sensor_2 = 18
need_water_2 = 22
#red led
warning = 23


def led_on_off(plant, sensor):

    if GPIO.input(sensor):
        GPIO.output(plant, GPIO.HIGH)
    else:
        GPIO.output(plant, GPIO.LOW)
#        GPIO.output(warning, GPIO.HIGH)

#    if GPIO.input(sensor_1) == 1 and GPIO.input(sensor_2) == 1:
#        GPIO.output(warning, GPIO.LOW)


def water_plant(plant):
    #TODO
    pass

def notification(sensor):
    if sensor == sensor_1:
        led_on_off(need_water_1, sensor)
    elif sensor == sensor_2:
        led_on_off(need_water_2, sensor)
    else:
        pass

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(need_water_1, GPIO.OUT)
GPIO.setup(need_water_2, GPIO.OUT)
#GPIO.setup(warning, GPIO.OUT)
GPIO.setup(sensor_1, GPIO.IN)
GPIO.setup(sensor_2, GPIO.IN)

GPIO.output(need_water_1, GPIO.LOW)
GPIO.output(need_water_2, GPIO.LOW)
#GPIO.output(warning, GPIO.LOW)

print GPIO.input(sensor_1)
print GPIO.input(sensor_2)
if GPIO.input(sensor_1) == 1:
    GPIO.output(need_water_1, GPIO.HIGH)
if GPIO.input(sensor_2) == 1:
    GPIO.output(need_water_2, GPIO.HIGH)



GPIO.add_event_detect( sensor_1, GPIO.BOTH, bouncetime=300)
GPIO.add_event_detect( sensor_2, GPIO.BOTH, bouncetime=300)

GPIO.add_event_callback(sensor_1,notification)
GPIO.add_event_callback(sensor_2,notification)

while True:
	time.sleep(0.1)

