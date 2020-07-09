#! /usr/bin/python3

def concatenate_list_data(list):
    
    string = ""
    for i in list:
        string = string + str(i)
    return string

print(concatenate_list_data([1,5,12,2]))
