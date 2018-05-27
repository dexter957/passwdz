#!/usr/bin/python


'''
Made specifically to invoke pass.py, for checking purposes
>>python3 invokePass.py > oufile & (put in the backgroud bc it takes some time)
'''

import subprocess
import secrets

below =70
limitDown=10
limitUp=50

for i in range(0,1000):
    #Choose a random number for length; we assume that a typical user does not use a passwordlonger than 50 characters
    passLength = str(secrets.choice(range(limitDown,limitUp)))
    #Assume the user gives sth close the length they have already decided
    randNum = str(secrets.randbelow(below))
    #If you get a negative random number, augment your limit
    while int(randNum) <= 0:
        below +=1
        randNum = str(secrets.randbelow(below))
    subprocess.call(["python3","pass.py",passLength,randNum])
