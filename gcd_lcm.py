#! /usr/bin/python3

x = int(input("Enter first number:"))
y = int(input("Enter second number:"))

def gcd(x, y):
    for i in range(1,max(x,y)+1):
        if (x%i==0) and (y%i==0):
            gcd = i
    return gcd

def lcm(x, y):
    for i in range(1,max(x,y)+1):
        if (x%i==0) and (y%i==0):
            gcd = i
    lcm = (x*y)/gcd
    return lcm

print("GCD of numbers is: {}".format(gcd(x,y)))
print("LCM of numbers is: {}".format(lcm(x,y)))
