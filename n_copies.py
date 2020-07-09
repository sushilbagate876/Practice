#! /usr/bin/python3

string = input("Input string:")

n = int(input("Input n:"))

def n_copies(str,n):
    result =""
    for i in range(n):
        result = result + string
    return result

print(n_copies(string,n))
