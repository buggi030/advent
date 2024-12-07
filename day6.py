from packages import parser
import re

def getInput():
    data = parser.readData('2024_day6.txt')
    map = []
    for i, row in enumerate(data):
        map.append([])
        for j, position in enumerate(row.strip()):
            map[-1].append(position)
            if position == '^':
                start_i, start_j = i , j
    return map, (start_i, start_j)

def next_position(direction, i,j):
    match direction:
        case 'up':
            return (i - 1, j)
        case 'down':
            return (i + 1, j)
        case 'left':
            return (i, j - 1)
        case 'right':
            return (i, j + 1)


map, (i,j) = getInput()


exit = False

next_direction_map = {
'up': 'right',
'right': 'down',
'down' : 'left',
'left' : 'up',
}

answer1 = {}
answer1[(i, j)] = True
def hasExit(direction, i, j):
    exit = False
    while not exit:
        if not (0<=i<len(map) and 0<=j<len(map[0])):
            exit = True
            continue
        next_i, next_j = next_position(direction, i, j)

        if not (0<=next_i<len(map) and 0<=next_j<len(map[0])):
            exit = True
            continue

        next = map[next_i][next_j]
        if next == '#':
            direction = next_direction_map[direction]
            continue
        i, j = next_i,next_j
        answer1[(i, j)] = True

    return True

def draw(visited, impediment = (-1,-1), background = {}, found_loop = None):
    for i, row in enumerate(map):
        for j, position in enumerate(row):
            if (i,j) == found_loop:
                    print('O', end=' ')
            elif (i,j) in visited:
                if isinstance(visited[(i,j)], (bool)):
                    print('X', end=' ')
                elif len(visited[(i,j)])>1:
                    print('+', end=' ')
                elif visited[(i,j)][0] == 'up' or  visited[(i,j)][0] == 'down':
                    print('|', end=' ')
                else:
                    print('—', end=' ')
            elif (i,j) == impediment:
                    print('X', end=' ')
            elif (i,j) in background:
                print('@', end=' ')
            else:
                print(position, end=' ')
        print("")

# Part 1

direction = 'up'
hasExit(direction, i , j)
print(len(answer1))
draw(answer1)

# Part 2
answer2 = {}
# answer2_less = {}

def hasExitLoop(direction, i, j, impediment = None, given_visited = {}):
    global answer2
#     global answer2_less
    visited = {}
    visited[(i,j)] = [direction]
    exit = False
    hasLoop = False
    while not exit:
        if not (0<=i<len(map) and 0<=j<len(map[0])):
            exit = True
            continue
        next_i, next_j = next_position(direction, i, j)

        if not (0<=next_i<len(map) and 0<=next_j<len(map[0])):
            exit = True
            continue

        next = map[next_i][next_j]
        if next == '#' or (next_i, next_j) == impediment:
            direction = next_direction_map[direction]
            continue

        # imagine next item IS impediment. then we would change direction
        if not impediment and (next_i, next_j) not in visited:
            new_direction = next_direction_map[direction]
            if hasExitLoop(next_direction_map[direction], i,j, (next_i, next_j), visited):
                answer2[(next_i, next_j)] = True

#         print('paused', direction, i, j, impediment, visited)
#         draw(visited)
        if impediment and (next_i,next_j) in visited and direction in visited[(next_i,next_j)]:
            hasLoop = True
#             if -2<impediment[0]-next_i<2 and -2<impediment[1]-next_j<2:
#                 answer2_less[impediment] = (next_i,next_j)
#                 draw(visited, impediment, given_visited, (next_i,next_j))
#                 print('found loop', direction, i, j, impediment)
#                 input("Press Enter to continue...")
            break

        i, j = next_i,next_j
        if (i, j) not in visited:
            visited[(i, j)] = []
        visited[(i, j)].append(direction)

#     print('____________________________', direction, i, j, impediment)
#     draw(visited)
    return hasLoop

hasExitLoop(direction, i , j)


print(answer2)
print(len(answer2))
print((i,j) in answer2)

