import fileinput
'''
Analyzes the output of passAnalyzer.py.
Processes each password, creating a tuple about it as:(length, lower case letters %, upper case letters %, digits %).
Can be called either with a filename as a command line argument, or using input piping
>>python3 passAnalyzer.py outfile
>>python3 passAnalyzer.py < outfile
>>python3 passAnalyzer.py < outfile > analyzerOutput
'''

#----------------------------------- Functions  -----------------------------------------------
def numOfUpperCaseLetters(word):
    return sum(1 for l in word if l.isupper() and not l.isdigit())

def numOfLowerCaseLetters(word):
    return sum(1 for l in word if not l.isupper() and not l.isdigit())

def numOfDigits(word):
    return sum(1 for d in word if d.isdigit())

def statisticize(word):
    low = numOfLowerCaseLetters(word)
    upp = numOfUpperCaseLetters(word)
    nums = numOfDigits(word)
    length = len(word)
    statistics.append((length,round(low/length,3),round(upp/length,3),round(nums/length,3)))

#----------------------------------------   Script   -----------------------------------------------

statistics = []

for line in fileinput.input():
    statisticize(line)
print(statistics)
