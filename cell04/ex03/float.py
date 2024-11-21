#!/usr/bin/env python3
n = input("Give me a number: ")

try:
    number = float(n)
    if number.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")

except ValueError:
    print("This isn't a number.")