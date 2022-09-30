#!/usr/bin/python3

from math import log10

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

print(f"\n{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} % {b} = {a % b}")
print(f"The base 10 logarithm of {a} = {log10(a)}")
print(f"{a} ^ {b} = {a ** b}")
