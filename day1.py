from packages import parser


def getInput():
    left, right = {}, {}
    data = parser.readData('2024_day1.txt')
    for i, d in enumerate(data):
        l, r = d.split()
        if int(l) not in left:
            left[int(l)] = []
        if int(r) not in right:
            right[int(r)] = []
        left[int(l)].append(i)
        right[int(r)].append(i)
    return left, right



left, right = getInput()
left, right = dict(sorted(left.items())), dict(sorted(right.items(), reverse=True))

print(left)
print(right)
t_distance = 0
similarity = 0
##### Task 1
# r_number, r_keys = right.popitem()
# for l_number, l_keys in left.items():
#     _ = 0
#     while _ < len(l_keys):
#         if len(r_keys) == 0:
#             r_number, r_keys = right.popitem()
#         r_key, r_keys = r_keys[0], r_keys[1:]
#         l_key = l_keys[_]
#         t_distance += abs(r_number - l_number)
#         _ +=1
# print(t_distance)

##### Task 2
for l_number, l_keys in left.items():
    if l_number in right:
        print(l_number, right[l_number])
        similarity += l_number * len(right[l_number]) * len(l_keys)
print(similarity)
