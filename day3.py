import os
import re
import pprint
import functools

game_max = {'red':12, 'green':13, 'blue':14}
answer = 0

class Solution:
    def __init__(self, data):
        self.answerOne = 0
        self.answersOne = {}
        self.answerTwo = 0
        self.data = data

    def isValid(self, baseI, baseJ):
        data = self.data
        for i in range(-1,2):
            for j in range(-1,2):
                curI = baseI+i
                curJ = baseJ+j
#                 print(curI,curJ,curIdata[curI][curJ])
                if 0<=curI<len(data) and 0<=curJ<len(data[baseI]) and data[curI][curJ]!='.' and not data[curI][curJ].isdigit():
#                     print(self.data[curI][curJ])
                    return True
        return False


    def parseRow(self, row, index):
        valid = False
        self.answersOne[index] = []
#         print("")
#         print(row)
        currentDigits = ''
        for j, char in enumerate(row):
            if char.isdigit():
                currentDigits+=char
#                 print('currentDigits:',currentDigits)
                valid = valid | self.isValid(index, j)
            else:
                if valid:
                    num = int(currentDigits,10)
#                     print('num:',num, end=", ")
                    self.answerOne+=num
                    self.answersOne[index].append(num)
#                     print('answer:',self.answerOne, end=";")
                    valid = False
#                 print(currentDigits)
                currentDigits = ''

    def runOne(self):
        for index, line in enumerate(self.data):
            numbers = self.parseRow(line, index)


        pprint.pprint(self.answersOne)

        print("The sum of the list elements is : ", end="")
        print(functools.reduce(lambda a, b: a+b, self.answersOne))
        return self.answerOne



    def runTwo(self):
        for line in self.data:
            index, row_games = self.parseRow(line)
            fewest = self.findFewestAmounts(row_games)
            self.answerTwo += self.findAnswerTwo(fewest)
        return self.answerTwo


with open(os.getcwd() + f'/inputs/day3', 'r') as f:
    data = f.readlines()

solution = Solution(data)
print(solution.runOne())
# print(solution.runTwo())