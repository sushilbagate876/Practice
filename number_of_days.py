#! /usr/bin/python3

from datetime import date

f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
d = l_date - f_date

print(d.days)

