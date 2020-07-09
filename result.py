#!/usr/bin/python3

n = int(input("Enter any integer:"))
result = int("%s" % n)+int("%s%s" % (n,n) )+int("%s%s%s" % (n,n,n) )
print(result)
