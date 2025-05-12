#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from umath import sin, cos

# Create your objects here.
ev3 = EV3Brick()
MotorL = Motor(Port.B)
MotorR = Motor(Port.C)
Driver = DriveBase(MotorL, MotorR, wheel_diameter = 55, axle_track = 104)
Eyes = UltrasonicSensor(Port.1)

def look():
    global Driver, degrees_turned
    positions = []
    degrees_turned = 0 #Records the amount of degrees turned
    while degrees_turned < 175:
        if Eyes.distance() < 30:
            Farness = Eyes.distance()
            Horizontal = sin((degrees_turned - 90) * Farness)
            Vertical = cos((degrees_turned - 90) * Farness)
            Driver.turn(5)
            degrees_turned += 5
        else:
            Driver.turn(1)
            degrees_turned += 1



# Write your program here.
