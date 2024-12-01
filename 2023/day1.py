import os

data = None
spelled_digits = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

def temp(char, subLine, reversed = False):
    if char.isdigit():
        return int(char, 10), subLine
    if reversed:
        subLine=char+subLine
    else:
        subLine+=char
    for number in spelled_digits:
        if subLine.startswith(number):
            return spelled_digits[number], subLine
        if subLine.endswith(number):
            return spelled_digits[number], subLine
    return None, subLine


with open(os.getcwd() + f'/inputs/day1', 'r') as f:
    data = f.readlines()

answer = 0
for line in data:
    line = line.strip()
    digit1, digit2 = None, None
    subLine1, subLine2 = '', ''
    for i in range(len(line)):
        if digit1 == None:
            digit1, subLine1 = temp(line[i], subLine1)
        if digit2 == None:
            digit2, subLine2 = temp(line[len(line)-1-i], subLine2, True)

        if digit1 and digit2:
            num = digit1*10+digit2
            answer+=num
            break

print(answer)



