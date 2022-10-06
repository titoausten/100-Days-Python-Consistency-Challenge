#!/usr/bin/python3

#Reads input from user in feet
measurement = ms = int(input("Enter measurement in feet: "))

inches = inc = ms * 12
yards= yd = ms * 3
miles = mi = ms / 5280

print(f"\nThe measurement of {ms}ft in inches, yards and miles = \n{inc}inches, \n{yd:.2f}yards and \n{mi:.4f}miles respectively.")
