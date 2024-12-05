from packages import parser
import re

def getInput():
    data = parser.readData('2024_day4.txt')
    return data

# Part 1
word = 'XMAS'
answer1 = 0

data = getInput()
tuple1 = [(i,i) for i in range(4)]
tuple2 = [(i,i) for i in range(0,-4,-1)]
tuple3 = [(-i,i) for i in range(4)]
tuple4 = [(i,-i) for i in range(4)]
tuple5 = [(0,i) for i in range(4)]
tuple6 = [(0,i) for i in range(0,-4,-1)]
tuple7 = [(i,0) for i in range(4)]
tuple8 = [(i,0) for i in range(0,-4,-1)]

deltas = [
[(i,i) for i in range(4)],
[(i,i) for i in range(0,-4,-1)],
[(-i,i) for i in range(4)],
[(i,-i) for i in range(4)],
[(0,i) for i in range(4)],
[(0,i) for i in range(0,-4,-1)],
[(i,0) for i in range(4)],
[(i,0) for i in range(0,-4,-1)]]

for i, row in enumerate(data):
    for j, start_letter in enumerate(row.strip()):
        if start_letter == 'X':
            for delta in deltas:
                valid = True
#                 print(delta)
                for _, (di,dj) in enumerate(delta):
                    if 0<=i+di<len(data) and 0<=j+dj< len(row):
#                         print((i+di,j+dj), data[i+di][j+dj], word[_])
                        if data[i+di][j+dj] != word[_]:
#                             print('invalid')
                            valid = False
                            break
                    else:
                        valid = False
                        break

                if valid:
#                     print('valid')
                    answer1+=1
print(answer1)

# Part 2

data = getInput()
tuple1 = [(-1,-1), (1,1)]
tuple2 = [(i,i) for i in range(0,-4,-1)]
tuple3 = [(-i,i) for i in range(4)]
tuple4 = [(i,-i) for i in range(4)]
tuple5 = [(0,i) for i in range(4)]
tuple6 = [(0,i) for i in range(0,-4,-1)]
tuple7 = [(i,0) for i in range(4)]
tuple8 = [(i,0) for i in range(0,-4,-1)]

deltas = (
([(-1,-1), (0, 0),(1,1)],
[(1,-1), (0, 0),(-1,1)],
[(1,1), (0, 0),(-1,-1)],
[(-1,1), (0, 0),(1,-1)],)
)
word = 'MAS'
answer2 = 0
for i, row in enumerate(data):
    for j, start_letter in enumerate(row.strip()):
        if start_letter == 'A':
            print('candidate', (i,j))
            valid = 4
            for delta in deltas:
#                 print('delta',delta, valid)
                for _, (di,dj) in enumerate(delta):
                    if 0<=i+di<len(data) and 0<=j+dj< len(row):
                        print((i+di,j+dj), data[i+di][j+dj], word[_])
                        if data[i+di][j+dj] != word[_]:
#                             print('invalid')
                            valid -=1
                            break
                    else:
#                         print('out of range')
                        valid -=1
                        break
            print((i,j),valid)

            if valid == 2:
                print('valid', (i,j))
                answer2+=1
print(answer2)