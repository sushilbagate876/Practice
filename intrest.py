#!/usr/bin/python3

def f(amt,rate,years):
    amount = amt * (1+ (rate*0.01))**years
    return amount

print(f(10000,3.5,7))
