#! /usr/bin/python3

from math import pi

radius = float(input("Enter radius of the sphere:"))

volume = (4*pi*radius*radius*radius)/3

print("Volume of thr sphere with radius {} is : {}".format(radius,volume))
