import os
import re
import pprint
import functools

game_max = {'red':12, 'green':13, 'blue':14}
answer = 0

class Solution:
    def __init__(self, data):
        self.answerOne = 0
        self.answerTwo = 0
        self.answersTwo = {}
        self.data = data

    def parseRow(self, row):
        separator1Index = row.find(':')
        separator2Index = row.find('|')
        winRow = row[separator1Index+1:separator2Index].strip()
        givenRow = row[separator2Index+1:].strip()
        win = re.findall('\d+',winRow)
        given = re.findall('\d+',givenRow)
        return win, given

    def findWin(self, input):
        win,given = input
        return [value for value in given if value in win]

    def findAnswerTwo(self):
        for key in self.answersTwo:
            self.answerTwo+=self.answersTwo[key]

    def run(self):
        for index, line in enumerate(self.data):
            if index not in self.answersTwo:
                self.answersTwo[index]=0
            self.answersTwo[index]+=1
            found = self.findWin(self.parseRow(line))
            for _ in range(self.answersTwo[index]):
                for cardIndex in range(index+1,index+1+len(found)):
                    if cardIndex not in self.answersTwo:
                        self.answersTwo[cardIndex]=0
                    self.answersTwo[cardIndex]+=1
            points = 2**(len(found)-1) if len(found) else 0
            self.answerOne+=points
        self.findAnswerTwo()
        return self.answerOne, self.answerTwo


with open(os.getcwd() + f'/inputs/day4', 'r') as f:
    data = f.readlines()

solution = Solution(data)
print(solution.run())
