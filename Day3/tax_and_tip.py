#!/usr/bin/python3

tax_rate = 0.04
tip_rate = 0.18

cost = float(input("Enter the cost of the meal: $"))

tax = cost * tax_rate
tip = cost * tip_rate
grand_total = cost + tax + tip

print(f"\nThe tax for the meal is ${tax:.2f},\n\
the tip for the meal is ${tip:.2f} and\n\
the grand total of the meal is ${grand_total:.2f}.")
