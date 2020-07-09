#! /usr/bin/python3

n = float(input("Enter a number:"))
def near_thousand(n):
    if abs(1000-n) <= 100 or abs(2000-n) <= 100:
        result = True
    else:
        result = False
    return result

print(near_thousand(n))

