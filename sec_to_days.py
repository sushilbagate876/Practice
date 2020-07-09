#!/usr/bin/python3

def sec_to_days(sec):

    days = sec//(86400)
    hrs = (sec%(86400))//3600
    mins = ((sec%(86400))%3600)//60
    secs = ((sec%(86400))%3600)%60
    return days, hrs, mins, secs

print('time in sec is',sec_to_days(91836))

