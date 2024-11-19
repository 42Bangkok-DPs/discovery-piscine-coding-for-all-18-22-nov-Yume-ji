#!/usr/bin/env python3
print("Enter a number less than 25")
n = int(input())

if n > 25:
        print("Error")

else:
        for numbers in range(n, 26):
                print("Inside the loop, my variable is " + str(numbers))