#!/usr/bin/env python3

x = 0
while x < 11:
    print(f"Table de {x}:", end=" ")
    y = 0
    while y < 11:
        print(f"{x*y}", end=" ")
        y += 1
    print()
    x += 1