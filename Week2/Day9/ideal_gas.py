#!/usr/bin/python3
#ideal gas constant
r = 8.314

#Reads input from user
pressure = p = float(input("Enter pressure in Pascal: "))
volume = v = float(input("Enter volume in liters: "))
temperature = t = float(input("Enter temperature in degrees Celsius: "))
#Temperature in Kelvin
t += 273.15

#Amount of gas in moles
n = (p * v) / (r * t)

print(f"\nThe amount of gas is {n:.2f} moles.")
