from packages import parser
import re

def getInput():
    data = parser.readData('2024_day5.txt')
    i = 0
    right_rules = {}
    while i < len(data) and data[i] != '\n':
        left, right = re.findall(r'\d{1,2}', data[i])
        if right not in right_rules:
            right_rules[right] = []
        right_rules[right].append(left)
        i += 1

    sets = []
    for j in range(i+1, len(data)):
        sets.append(re.findall(r'\d{1,2}', data[j]))

    return right_rules, sets

right_rules, sets = getInput()

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def valid(set):
    valid = True
    for i in range(len(set)-2, -1,-1):
        s = set[i]
        subset = set[i+1:]
        rule = right_rules[s] if s in right_rules else []
        intersect = intersection(subset, rule)
        valid = valid and len(intersect)==0
        if not valid:
            break
    return valid

def resort(set):
    valid = True
    for i in range(len(set)-2, -1,-1):
        s = set[i]
        subset = set[i+1:]
        rule = right_rules[s] if s in right_rules else []
        intersect = intersection(subset, rule)
        if len(intersect)>0:
            print(set, i, s, rule, intersect)
            max_j = -1
            for item_to_move in intersect:
                max_j = max(max_j, set.index(item_to_move))
            set[i], set[max_j] = set[max_j], set[i]

    return set

answer1 = 0
answer2 = 0
for set in sets:
    if valid(set):
        print('valid', set)
        # Part 1
        middle = len(set) // 2
        answer1 += int(set[middle])
    else:
        while not valid(set):
            print('invalid', set)
            set = resort(set)
        print('NOW VALID', set)
        middle = len(set) // 2
        answer2 += int(set[middle])



print(answer1)
print(answer2)

