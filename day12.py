from packages import parser
from packages import parser
from packages import utils
import re
import time
import sys

time_start = time.time()
DELTAS = ( (0,1), (1,0), (0,-1), (-1,0) )
visited = {}
def getInput():
    data = parser.readData('2024_day12.txt')

    return [list(row.strip()) for row in data]

def find_perimeter(garden_position):
    i, j = garden_position
    perimeter = 4
    for delta in DELTAS:
        neighbour_i, neighbour_j = i+delta[0],j+delta[1]
        if not (0<=neighbour_i<len(map) and 0<=neighbour_j<len(map[0])):
            continue
        if map[neighbour_i][neighbour_j] == map[i][j]:
            perimeter -=1
    return perimeter

def find_corners(garden_position):
    i, j = garden_position
    corners = 0
    for _ in range(4):
        neighbours = 0
        delta1, delta2 = DELTAS[_-1], DELTAS[_]
        neighbour1_i, neighbour1_j = i+delta1[0],j+delta1[1]
        neighbour2_i, neighbour2_j = i+delta2[0],j+delta2[1]
        if not (0<=neighbour1_i<len(map) and 0<=neighbour1_j<len(map[0])):
            neighbour1 = None
        else:
            neighbour1 = map[neighbour1_i][neighbour1_j]
        if not (0<=neighbour2_i<len(map) and 0<=neighbour2_j<len(map[0])):
            neighbour2 = None
        else:
            neighbour2 = map[neighbour2_i][neighbour2_j]

        if neighbour2 == map[i][j]:
            neighbours +=1
        if neighbour1 == map[i][j]:
            neighbours +=1
        if neighbours == 0: # no neighbours at corner - 1 corner
            corners+=1
            continue
        if neighbours == 1: # strictly one neighbour - it's not a corner
            continue
        if neighbours == 2: # it may be an internal corner
            if delta1[0] == 0:
                diagonal_neighbour = map[i+delta2[0]][j+delta1[1]]
            else:
                diagonal_neighbour = map[i+delta1[0]][j+delta2[1]]
            if diagonal_neighbour == map[i][j]:
                continue
            corners+=1

    return corners

def discover(position, garden, found):
    visited[position] = True
    i, j = position
    for delta in DELTAS:
        neighbour_i, neighbour_j = i+delta[0],j+delta[1]
        if not (0<=neighbour_i<len(map) and 0<=neighbour_j<len(map[0])):
            continue
        if (neighbour_i, neighbour_j) in found:
            continue
        if map[neighbour_i][neighbour_j] == garden:
            found[(neighbour_i, neighbour_j)] = True
            found = discover((neighbour_i, neighbour_j), garden, found)
    return found

regions = []
map = getInput()


for i in range(len(map)):
    for j in range(len(map[0])):
        if (i,j) in visited:
            continue
        found = discover((i, j), map[i][j], {(i,j):True})
        regions.append((map[i][j],list(found.keys())))

answer1 = 0
answer2 = 0
for garden, region in regions:
    perimeter = 0
    corners = 0
    area = 0
    for position in region:
        area+=1
        perimeter += find_perimeter(position)
        corners += find_corners(position)
    answer1 += perimeter*area
    answer2 += corners*area

print(answer1)
print(answer2)


