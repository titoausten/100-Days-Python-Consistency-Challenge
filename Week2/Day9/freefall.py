#!/usr/bin/python3
#Free fall
from math import sqrt

initial_speed = vi = 0
gravity = a = 9.8

#height from which the object is dropped in meters(m).
height = d = float(input("Enter height: "))

final_speed = vf = sqrt((vi ** 2) + (2 * a * d))

print(f"\nThe final velocity = {vf:.2f} meters per second square.")
