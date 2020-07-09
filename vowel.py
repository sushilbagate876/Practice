#! /usr/bin/python3

vowel = ['a','e','i','o','u']

n = input("Enter alphabet:")
n = n.lower()
if n in vowel:
    print("Alphabet is a vowel.")
else:
    print("Alphabet is not a vowel.")
