#!/usr/bin/env python3
print("Enter the first number:")
first_number = int(input())

print("Enter the second number: ")
second_number = int(input())

third_number = first_number * second_number
print(str(first_number) + " x " + str(second_number) + " = " + str(third_number))

if third_number > 0:
    print("The result is positive.")
elif third_number < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")