from packages import parser
from packages import iterator
import re
import time
import re
time_start = time.time()
import sys

def getInput():
    data = parser.readData('2024_day9.txt')
    return list(map(int,data[0].strip()))


data = getInput()
print(data)
checksum = 0

def what_value_at(i, number):
    if i%2 == 0:
        return [i//2 for _ in range(number)]
    else:
        return [None for _ in range(number)]
j = 0

# part 1
new_data = []
right_pointer = len(data)+1 if len(data) %2 else len(data)
stack = []
exit = False
for i, number in enumerate(data):
    if right_pointer<i or exit:
        break
    if i%2 == 0:
        if right_pointer==i:
            for _, item in enumerate(stack):
                checksum += (i//2) * (j+_)
                new_data.append(i//2)
#                 print((int(i/2), (j+_)), end = ' ')
            exit = True
            break
        for _ in range(number):
            checksum += (i//2) * (j+_)
            new_data.append(i//2)
#             print((int(i/2), (j+_)), end = ' ')
    else:
        for _ in range(min(number,right_pointer-i)):

            while len(stack)<1 :
                right_pointer -=2
                stack = what_value_at(right_pointer, data[right_pointer])

            current = stack.pop()
            checksum += current * (j+_)
            new_data.append(current)
#             print((current,(j+_)), end = ' ')
    j += number


#part 2


defragmented = []
right_pointer = len(data)+1 if len(data) %2 else len(data)
stack = []
exit = False
for i, number in enumerate(data):
    if i%2 == 0:
        for _ in range(number):
            defragmented.append(i//2)

    else:
        for _ in range(number):

            while len(stack)<1 :
                right_pointer -=2
                stack = what_value_at(right_pointer, data[right_pointer])
            current = stack.pop()
            defragmented.append(None)
    j += number


map = {}
cur_index = 0
current_count = 0
for i, id in enumerate(defragmented):
    if id != None:
        current_count = 0
    else:
        current_count +=1

    if current_count == 1:
        cur_index = i

    if current_count>0:
        map[cur_index] = current_count
#     print(cur_index,(i,id), map)
#     input("waiting")
#     print(cur_index,map)
# print(map)

replace=lambda a,b,s:a[:s]+b+a[s+len(b):]

right = len(data)+1-2 if len(data) %2 else len(data) -2
right_pointer = len(defragmented)
print(defragmented)
print(map)
while right>0:
    current_file = what_value_at(right, data[right])
    place_to_search = len(current_file)
    right_pointer = right_pointer-place_to_search

    if right % 2 == 0:
#         print(current_file, map, right_pointer)
        for i, length in dict(sorted(map.items())).items():
            if length>=place_to_search and i<right_pointer:
#                 pr    int('found',i, length, place_to_search+1)
                defragmented[i:i+place_to_search] = current_file
                defragmented[right_pointer:right_pointer+place_to_search] = place_to_search*[None]
                map.pop(i)
                map[i+place_to_search] = length-place_to_search
                break
#         print(defragmented)
    right-=1

# print(new_data)
# print(defragmented)



#final part 1
# print()
# print(checksum)
# # print(new_data)
# checksum = 0
# for i, id in enumerate(new_data):
#     checksum += i*id
#
# print(checksum)

#final part 2
print()
print(checksum)
# print(new_data)
checksum = 0
for i, id in enumerate(defragmented):
    if id is None:
        continue
    checksum += i*id
print(checksum)
