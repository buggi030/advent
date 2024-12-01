import os
import re
import pprint
import functools

def generateSeeds(seeds):
    for i in range(0,len(seeds),2):
        print()
        print('NEW INTERVAL:',seeds[i], seeds[i]+seeds[i+1])
        for _ in range(seeds[i], seeds[i]+seeds[i+1]):
            yield _

class Solution:
    def __init__(self, data):
        self.answerOne = 0
        self.answerTwo = 0
        self.answersTwo = {}
        self.data = data
        self.seeds = []
        self.maps = []

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

    def runTwo(self):
        self.seeds = [int(value,10) for value in re.findall('\d+', self.data[0])]
        print(self.seeds)
        map = []
        for line in self.data[1:]:
            if len(line)<2 and len(map):
                self.maps.append(map)
                map = []
                continue
            parsed = re.findall('\d+', line)
            if not len(parsed):
                continue
            numbers = [int(value,10) for value in re.findall('\d+', line)]
            map.append(numbers)
        if len(map):
            self.maps.append(map)
        self.locations=[]
        min_location = None
        for seed in generateSeeds(self.seeds):
            mapped_seed = seed
            print(mapped_seed, end=' - ')
            for bunch in self.maps:
                seed_changed = False
                v=False
                for map in bunch:
#                     v and print('VVV1: ',seed,seed_changed,map)
                    if not seed_changed and map[1]<=mapped_seed<map[1]+map[2]:
                        mapped_seed = map[0]+(mapped_seed-map[1])
                        seed_changed = True
#                         v and print('VVV1.1: ',mapped_seed,seed_changed)
#                     else:
#                         mapped_seed = seed
#                         v and print('VVV1.2: ',mapped_seed,seed_changed)
#                     mapped_seeds.append(mapped_seed)
#                     v and print('VVV2: ',mapped_seed,seed_changed)
#                     v and print('VVV3: ',mapped_seeds,seed_changed)
#                     self.seeds.append(mapped_seeds)
                    print(mapped_seed,map,seed_changed)
            if not min_location:
                min_location = mapped_seed
            else:
                min_location = min(min_location,mapped_seed)
        print()
        return min_location

    def parseMapIntervals(self, map):
        return ((map[1],map[1]+map[2]-1),(map[0],map[0]+map[2]-1))

    def parseSeedsIntervals(self):
        values = [int(value,10) for value in re.findall('\d+', self.data[0])]
        seedsIntervals = []
        for i in range(0,len(values),2):
            seedsIntervals.append((values[i],values[i]+values[i+1]-1))
        return seedsIntervals

    def intersectIntervals(self, seeds, map):
        print(seeds)
        if type(seeds[0]) is tuple:
            print('rec')
            newIntervals = []
            for value in seeds:
                newIntervals.append(self.intersectIntervals(value,map))
            return newIntervals
        sourceMin = map[1]
        sourceMax = map[1]+map[2]-1
        print(seeds, map, (sourceMin,sourceMax))

        if seeds[0]<=sourceMax and seeds[1]>=sourceMin:
            intersection = (max(seeds[0], sourceMin), min(seeds[1], sourceMax))
            destinationIntersection = (intersection[0]+map[0]-map[1], intersection[1]+map[0]-map[1])
            if intersection==seeds:
                print('full intersect:',intersection==seeds, intersection,destinationIntersection)
                return destinationIntersection
            print('partial intersect:',intersection==seeds, intersection,destinationIntersection)
            if seeds[0]<intersection[0] and seeds[1]>intersection[1]:
#             intersection is completely inside seeds seedsInterval. we get 3 new intervals from it
                newIntervals = ((seeds[0],intersection[0]-1), destinationIntersection, (intersection[1]+1,seeds[1]))
            elif intersection[0]==seeds[0]:
                newIntervals = (destinationIntersection, (intersection[1]+1,seeds[1]))
            elif intersection[1]==seeds[1]:
                newIntervals = ((seeds[0], intersection[0]-1), destinationIntersection)
            else:
                raise Exception('Unknown case')
            print(newIntervals)
            return newIntervals

        print('no intersect')
        return seeds



    def runTwoIntervals(self):
        self.seedsIntervals = self.parseSeedsIntervals()
#         print(self.seedsIntervals)
        map = []
        for line in self.data[1:]:
            if len(line)<2 and len(map):
                self.maps.append(map)
                map = []
                continue
            parsed = re.findall('\d+', line)
            if not len(parsed):
                continue
            numbers = [int(value,10) for value in re.findall('\d+', line)]
#             map.append(self.parseMapIntervals(numbers))
            map.append(numbers)
        if len(map):
            self.maps.append(map)

        for seedsInterval in self.seedsIntervals:
            currentIntervals = seedsInterval
            for bunch in self.maps:
                for map in bunch:
                    cur = self.intersectIntervals(currentIntervals, map)
                    if currentIntervals != cur:
                        currentIntervals= cur
                        break
            print('RESULT:',seedsInterval, currentIntervals)
#         print(self.maps)

    def run(self):
        self.seeds = [[int(value,10) for value in re.findall('\d+', self.data[0])]]
        print(self.seeds)
        map = []
        for line in self.data[1:]:
            if len(line)<2 and len(map):
                self.maps.append(map)
                map = []
                continue
            parsed = re.findall('\d+', line)
            if not len(parsed):
                continue
            numbers = [int(value,10) for value in re.findall('\d+', line)]
            map.append(numbers)
        if len(map):
            self.maps.append(map)

        for bunch in self.maps:
            seed_changed = [False for _ in self.seeds[-1]]
            print()
            v=False
#             v= self.seeds[-1] ==[81,53,57,52]
            for map in bunch:
                mapped_seeds = []
                for ind, seed in enumerate(self.seeds[-1]):
                    v and print('VVV1: ',seed,seeds_changed[ind],map)
#                     if seeds_changed[ind]:
#                         continue
                    if not seeds_changed[ind] and map[1]<=seed<map[1]+map[2]:
                        mapped_seed = map[0]+(seed-map[1])
                        seeds_changed[ind] = True
                        v and print('VVV1.1: ',mapped_seed,seeds_changed[ind])
                    else:
                        mapped_seed = seed
                        v and print('VVV1.2: ',mapped_seed,seeds_changed[ind])
                    mapped_seeds.append(mapped_seed)
                    v and print('VVV2: ',mapped_seed,seeds_changed[ind])
                v and print('VVV3: ',mapped_seeds,seeds_changed[ind])
                self.seeds.append(mapped_seeds)
                print(mapped_seeds,map,seeds_changed)
        return min(self.seeds[-1])
#         print(self.seeds)


with open(os.getcwd() + f'/inputs/day5-test', 'r') as f:
    data = f.readlines()

solution = Solution(data)
# print(solution.run())
# print(solution.runTwo())
print(solution.runTwoIntervals())
