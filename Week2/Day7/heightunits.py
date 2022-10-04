#!/usr/bin/python3

#Feet & inches to centimeters converter
inch_per_feet, cm_per_inch = 12, 2.54

print("Enter your height")
feet, inches = int(input("Height in feet: ")), int(input("Height in inches: "))

height_in_cm = ((feet * inch_per_feet) + inches) * cm_per_inch

print(f"\nYour height in cm = {height_in_cm}")
