import os
import re

game_max = {'red':12, 'green':13, 'blue':14}
answer = 0

class Solution:
    def __init__(self, data):
        self.answerOne = 0
        self.answerTwo = 0
        self.max = {'red':12, 'green':13, 'blue':14}
        self.data = data

    def parseIndex(self, row):
        pattern = r"[0-9]+"
        separatorIndex = row.find(':')
        index = re.findall(pattern, row[:separatorIndex])[0]
        return row[separatorIndex+1:].strip(), index

    def parseGame(self, string):
        game = {}
        for item in  string.split(','):
            key = re.search('[a-z]+',item)[0]
            value = re.search('[0-9]+',item)[0]
            game[key] = int(value, 10)

        return game


    def isGameValid(self, game):
        for key in game:
            if game[key]>self.max[key]:
                return False
        return True

    def findFewestAmounts(self, games):
        fewest = {'blue':0, 'green':0, 'red':0}
        for game in games:
            for key in game:
                fewest[key] = max(fewest[key], game[key])
        return fewest


    def isGamesValid(self, games):
        valid = True
        for game in games:
            valid = valid & self.isGameValid(game)
            if not valid:
                break
        return valid

    def parseRow(self, row):
        row, index = self.parseIndex(row)
        games = []
        for item in row.split(';'):
            game = self.parseGame(item)
            games.append(game)
        return int(index,10), games


    def runOne(self):
        for line in self.data:
            index, row_games = self.parseRow(line)
            if self.isGamesValid(row_games):
                self.answerOne += index
        return self.answerOne

    def findAnswerTwo(self, fewest):
        result = 1
        for key in fewest:
            result *=fewest[key]
        return result


    def runTwo(self):
        for line in self.data:
            index, row_games = self.parseRow(line)
            fewest = self.findFewestAmounts(row_games)
            self.answerTwo += self.findAnswerTwo(fewest)
        return self.answerTwo


with open(os.getcwd() + f'/inputs/day2', 'r') as f:
    data = f.readlines()

solution = Solution(data)
# print(solution.runOne())
print(solution.runTwo())