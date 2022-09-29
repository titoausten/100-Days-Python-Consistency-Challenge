#!/usr/bin/python3

widget_weight = 75
gizmo_weight = 112

num_widgets = int(input("Enter number of widgets ordered: "))
num_gizmos = int(input("Enter number of gizmos ordered: "))

total_weightw = widget_weight * num_widgets
total_weightg = gizmo_weight * num_gizmos
total_weight_kg = (total_weightw + total_weightg) / 1000

print(f"\nThe total weight of the order is {total_weight_kg:.2f}kg")
