#!/usr/bin/python3
import math

l1 = math.radians(float(input("Enter the value of longitude at point 1: ")))
g1= math.radians(float(input("Enter the value of latitude at point 1: ")))

l2 = math.radians(float(input("Enter the value of longitude at point 2: ")))
g2 = math.radians(float(input("Enter the value of latitude at point 2: ")))

distance = 6371.01 * math.acos(math.sin(l1) * math.sin(l2) + math.cos(l1) * math.cos(l2) * math.cos(g1 - g2))

print(f"\nThe distance between the points = {distance:.2f}km")
