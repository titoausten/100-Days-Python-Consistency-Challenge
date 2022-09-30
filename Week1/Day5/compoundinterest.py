#!/usr/bin/python3

interest_rate = 0.04

amount_deposit = float(input("Enter amount deposited: $"))
interest = interest_rate * amount_deposit

for year in range(1,4):
    total_amount = amount_deposit + interest
    amount_deposit = total_amount
    print(f"The total amount of savings for year {year} is ${total_amount:.2f}")
    
print("\nThat's the details of the savings account for 3 years")
    
