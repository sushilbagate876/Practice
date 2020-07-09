#! /usr/bin/python3

str = input("Input String:")
def string(str):
    if len(str)>=2 and str[:2]=="Is":
        return str
    else:
        return "Is"+str

print(string(str))


