#! /usr/bin/python3

filename = input("Enter filename with extension:")
filename_split = filename.split(".")
print("Output:{}".format(filename_split[1]))
