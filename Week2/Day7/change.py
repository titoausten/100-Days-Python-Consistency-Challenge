#!/usr/bin/python3

#Self Checkout Program
cents_to_toonie = ct = 200
cents_to_loonie = cl = 100
cents_to_quarter = cq = cl / 4
cents_to_dime = cd = cl / 10
cents_to_nickel = cn = cl / 20

#Number of cents by User
num_cents = nc = int(input("Enter the number of cents: "))

print("The change is:")
print(f"{nc // ct} toonies,")
nc = nc % ct
print(f"{nc // cl} loonies,")
nc = nc % cl
print(f"{nc // cq} quarters,")
nc = nc % cq
print(f"{nc // cd} dimes,")
nc = nc % cd
print(f"{nc // cn} nickels,")
nc = nc % cn
print(f"{nc} pennies.")
