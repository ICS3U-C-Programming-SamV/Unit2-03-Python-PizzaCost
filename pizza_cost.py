#!/usr/bin/env python3
# Created By: Sam V
# Date: Sep 27th , 2026
# this program asks the user for the size of the pizza
# with the number of toppings and calculates
# the total cost of the pizza.
# Input: Get dimensions from the user

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
cost_per_unit = float(input("Enter the cost per square unit: $"))

# Calculations
area = length * width
perimeter = 2 * (length + width)
total_cost = area * cost_per_unit

# Output: Display results formatted to 2 decimal places
print(f"\n--- Results ---")
print(f"Area: {area:.2f} sq units")
print(f"Perimeter: {perimeter:.2f} units")
print(f"Total Cost: ${total_cost:.2f}")
