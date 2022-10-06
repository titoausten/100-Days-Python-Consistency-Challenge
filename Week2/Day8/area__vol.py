#!/usr/bin/python3

from math import pi

#read radius from user
radius= r = int(input("Enter radius in metres: "))

area_of_circle = a = pi * (r ** 2)
volume_of_sphere = v = (4 * pi * (r ** 3)) / 3

print(f"\nThe area of a circle = {a:.2f} metres square. \nThe volume of a sphere = {v:.2f} cubic metres.")
