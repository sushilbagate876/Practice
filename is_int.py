#! /usr/bin/python3

def add_number(a,b):
    if not (isinstance(a,int) and isinstance(b,int)):
        raise TypeError("Inputs must be intergers.")
    return a+b

print(add_number(10,20))
