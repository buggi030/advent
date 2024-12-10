from packages import parser
from packages import iterator
import time
time_start = time.time()

def getInput():
    data = parser.readData('2024_day10.txt')
    return [list(map(str,row.strip())) for row in data]


deltas = ((-1,0),(0,1), (1, 0), (0,-1))
routes = []

def depth_first_search(next, path):
    global routes
    path.append(next)
#     print('deeper', next)
#     input("waiting")
    start_i, start_j = next
    current = map[start_i][start_j]
    if current == '9':
        routes.append(list(path))
        path.pop()
        return

    for d_i, d_j in deltas:
        if not (0<=start_i+d_i<len(map) and 0<=start_j+d_j<len(map[0])):
            continue

        neighbour = map[start_i+d_i][start_j+d_j]
        if neighbour == '.':
            continue
        if int(neighbour) - int(current) == 1:
            depth_first_search((start_i+d_i, start_j+d_j), path)

#     routes.append(list(path))
    path.pop()

map = getInput()
print(map)

for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == '0':
            depth_first_search((i, j), [])

def draw(map, path):
    for i, row in enumerate(map):
        for j, item in enumerate(row):
#             print((i,j) in path, (i,j) , path)
            if (i,j) in path:
                print(item, end=" ")
            else:
                print('.', end=" ")
        print()

unique_routes = {}
for route in routes:
#     draw(map, route)
#     print(route[0] not in unique_routes, route[0] , unique_routes)
    if route[0] not in unique_routes:
        unique_routes[route[0]] = set()
    unique_routes[route[0]].add(route[-1])
#     print(route, unique_routes)
#     input("waiting")

answer1 = 0
for trailhead, tails in unique_routes.items():
    answer1 += len(tails)

print(answer1)
print(len(routes))