#!/usr/bin/python3

small_containers = int(input("Enter number of containers (1 litre or less): "))
big_containers = int(input("Enter number of containers (greater than 1 litre): "))

refund = (small_containers * 0.10) + (big_containers * 0.25)

print(f"\nYou will be refunded ${refund:.2f} for your containers.")
