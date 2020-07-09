#! /usr/bin/python3

string = input("Input string:")

n = int(input("Input n:"))

def n_copies(string,n):
    result =""
    for i in range(n):
        if len(string)>=2 :
            result = result + string[:2]
        else:
            result = result + string
    return result

print(n_copies(string,n))
