#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Create your objects here.
ev3 = EV3Brick()
MotorL = Motor(Port.B)
MotorR = Motor(Port.C)
Driver = DriveBase(MotorL, MotorR, wheel_diameter = 55, axle_track = 104)

def look():
    global Driver
    degrees_turned = 0
    while degrees_turned < 175:
# Write your program here.
