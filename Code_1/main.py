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
# Motors: Ports B and C
# Ultrasonic sensor: Port 2
# Colour sensor: Port 1

ev3 = EV3Brick()
MotorL = Motor(Port.B)
MotorR = Motor(Port.C)
Driver = DriveBase(MotorL, MotorR, wheel_diameter = 55, axle_track = 104)
Eyes = UltrasonicSensor(Port.S2)
ColourCheck = ColorSensor(Port.S1)

Farness = 0

def look():
    '''Turns and looks for objects'''
    global Driver, degrees_turned, Eyes
    positions = []
    degrees_turned = 0 #Records the amount of degrees turned
    while degrees_turned < 175:
        Farness = Eyes.distance()
        if Farness < 30:
            Farness = Eyes.distance()
            Horizontal = sin((degrees_turned - 90) * Farness) #Finds the vertical and horizontal distance of the boxes
            Vertical = cos((degrees_turned - 90) * Farness)
            Driver.turn(5)
            degrees_turned += 5
            positions.append([Horizontal, Vertical])
        else:
            Driver.turn(1)
            degrees_turned += 1
    Driver.turn((180 - degrees_turned))
    return positions



# Write your program here.
previousVertical = 0
while True:
    for i in look():
        Driver.forward((i[1] - previousVertical))
        '''Turns to look at the object'''
        if i[0] < 0:
            Driver.turn(-90)
        elif i[0] > 0:
            Driver.turn(90)
        
        if ColourCheck.color() == Color.RED or Color.YELLOW:
            '''The robot moves the box back to the start'''
            Driver.forward(i[0])
            Driver.forward(10)
            Driver.turn((90 * (i[0] ** 0)))
            Driver.forward(i[1] + 30)
            Driver.forward(-30)
            Driver.turn((90 * (i[0] ** 0)))
            Driver.forward(i[0] + 10)
            previousVertical = 0
        else:
            '''The robot just moves on to the next box'''
            Driver.turn((-90 * (i[0] ** 0)))
            previousVertical = i[1]

    