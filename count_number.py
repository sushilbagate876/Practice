#! /usr/bin/python3

list = input("Enter numbers:")
n = input("Enter number:")

def count_number(n):
    count = 0
    for num in list:
        if num ==n:
            count = count+1
    return count

print(count_number(n))
