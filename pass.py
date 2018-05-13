#!/usr/bin/python
'''
A very simple password generator. Works with user input for the password length, as well as
the number of numeric characters in the password (though the user does not know it ;P).
Generates a password containing letters, special characters, numbers.
For more secure passwords choose length > 20 characters.
For now, assumes correct user input.
Can be either ran from command line with or without full argument list, or from a script, with full argument list. Example:
>> python3 pass.py     (not all arguments)
>> python3 pass.py 1 2 (all arguments)
'''
import sys
import secrets

forbiddenCharacters = [" ","\""," \'"]
upperLength = 0
rang = 0

def reduceToOneDigit(num):
    if(len(str(num))) < 2:
        return num
    digits = [int(digit) for digit in str(num)]
    print (digits)
    finNum = sum(digits)
    finNum = reduceToOneDigit(finNum)
    return finNum

def isForbidden(character):
    if character in forbiddenCharacters:
        return True
    return False

if not sys.argv[1:]: #No input arguments other than the script name
    upperLength = int(input("Set the upper limit for password; the lower is 9 characters:"))
    rang = int(input("Give any number:"))
else:
    upperLength = int(sys.argv[1])
    rang = int(sys.argv[2])


passlets = []
passnums = []

for i in range(0,upperLength):
    judger = secrets.randbelow(rang)
    if judger%2 == 0:  #This character will be alpha
        passnum = secrets.choice(range(32,122)) #Generate an ascii character
        while(isForbidden(chr(passnum))):
                passnum = secrets.choice(range(32,122))
        passnums.append(passnum)
        passlets.append(chr(passnums[i]))
    else:  #This character will be numeric
        if judger > rang:
            passnums.append(secrets.choice(range(rang,judger)))
        else:
            passnums.append(secrets.choice(range(judger,rang)))
        passlets.append(str(reduceToOneDigit(passnums[i])))


#print (passnums)
#print (passlets)
password = ''.join(passlets)
print (password)
