import os
import re
import pprint
import functools

class Solution:
    def __init__(self, data):
        self.answerOne = 0
        self.answersOne = {}
        self.answerTwo = 0
        self.data = data
        self.gears = {}

    def isIntervalValid(self, baseI, startJ, endJ):
        indices = [(baseI, _) for _ in range(startJ, endJ+1)]
        data = self.data
        for curI in range(baseI-1, baseI+2):
            for curJ in range(startJ-1,endJ+2):
                if (curI,curJ) in indices:
                    continue
                if 0<=curI<len(data) and 0<=curJ<len(data[0]):
                    if data[curI][curJ]!='.'  and not data[curI][curJ].isdigit() and data[curI][curJ]!="\n":
                        return (curI,curJ) if data[curI][curJ]=='*' else None, True
        return None, False

    def parseRow(self, row, index):
        valid = False
        self.answersOne[index] = []
        currentDigits = ''
        currentIndexes = []
        for j, char in enumerate(row):
            if char.isdigit():
                currentDigits+=char
                currentIndexes.append(j)
            elif len(currentIndexes):
                gear, isIntervalValid = self.isIntervalValid(index, min(currentIndexes), max(currentIndexes))
                if isIntervalValid:
                    num = int(currentDigits,10)
                    self.answerOne+=num
                    self.answersOne[index].append(num)
                    if gear:
                        if gear not in self.gears:
                            self.gears[gear] = []
                        self.gears[gear].append(num)
                currentDigits = ''
                currentIndexes = []

    def findAnswerTwo(self):
        result = 0
        for key in self.gears:
            if len(self.gears[key])>1:
                print(self.gears[key], functools.reduce(lambda a, b: a*b, self.gears[key]))
                result+=functools.reduce(lambda a, b: a*b, self.gears[key])
        print(result)

    def runOne(self):
        for index, line in enumerate(self.data):
            numbers = self.parseRow(line, index)
        print(self.answerOne)
        print(self.findAnswerTwo())
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