#!/usr/bin/python3

#Converting U.S MPG to Canadian L/100km
us_units = int(input("Enter fuel value in MPG: "))
cad_units = 235.215 / us_units

print(f"The Canadian fuel efficiency value for the U.S value {us_units:.2f}MPG is {cad_units:.3f}L/100km")
