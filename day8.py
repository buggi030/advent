from packages import parser
from packages import iterator
import re
import time
import re
time_start = time.time()

def getInput():
    data = parser.readData('2024_day8.txt')
    map = [list(row.strip()) for row in data]

    return map

def equation(point1, point2, j3):
    i1,j1 = point1
    i2,j2 = point2

    return (j3-j1)*(i2-i1)/(j2-j1) + i1

map = getInput()

antennas = {}
for i, row in enumerate(map):
    for j, antenna in enumerate(row):
        if re.match(r'[a-z]+|[A-Z]+|[0-9]+',antenna):
            if antenna not in antennas:
                antennas[antenna] = []
            antennas[antenna].append((i,j))

antinodes1 = {}
for antenna, points in antennas.items():
#     print(antenna,points)
    for _, point1 in enumerate(points):
        if _ !=len(points)-1:
            for point2 in points[_+1:]:
                delta = abs(point1[1]-point2[1])
                min_j = min(point1[1],point2[1])
                max_j = max(point1[1],point2[1])
                left_i = equation(point1,point2, min_j - delta)
                if left_i.is_integer() and -1<left_i<len(map) and -1<min_j - delta<len(map[0]):
                    antinodes1[(int(left_i), min_j - delta)] = True
                right_i = equation(point1,point2, max_j + delta)
                if right_i.is_integer() and -1<right_i<len(map) and -1<max_j + delta<len(map[0]):
                    antinodes1[(int(right_i), max_j + delta)] = True


# iterator.draw(map,antinodes1)
time_end = time.time()
print('part 1 took ', (time_end - time_start)*1000)


# antinodes2 = []
antinodes2 = {}
for antenna, points in antennas.items():
#     print(antenna,points)
    for _, point1 in enumerate(points):
        if _ !=len(points)-1:
            for point2 in points[_+1:]:
                delta = 1
                cur_j = max(point1[1],point2[1])
                while cur_j - delta >-1:
                    left_i = equation(point1,point2, cur_j - delta)
                    if left_i.is_integer() and -1<left_i<len(map) and -1<cur_j - delta<len(map[0]):
#                         antinodes2.append((int(left_i), cur_j - delta))
                        antinodes2[(int(left_i), cur_j - delta)] = True
                    cur_j = cur_j - delta

                cur_j = min(point1[1],point2[1])
                while cur_j + delta < len(map[0]):
                    right_i = equation(point1,point2, cur_j + delta)
                    if right_i.is_integer() and -1<right_i<len(map) and -1<cur_j + delta<len(map[0]):
#                         antinodes2.append((int(right_i), cur_j + delta))
                        antinodes2[(int(right_i), cur_j + delta)] = True
                    cur_j = cur_j + delta

iterator.draw(map,antinodes2)
print(len(antinodes2))
print('part 2 took ', (time.time() - time_end)*1000)