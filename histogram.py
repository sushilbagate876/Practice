#! /usr/bin/python3

def histogram(items):
    for n in items:
        result = ""
        times = n
        while times>0:
            result = result + "*"
            times = times - 1
        print(result)

histogram([2,3,6,5])
