from packages import parser
import re
import time

time_start = time.time()

def getInput():
    data = parser.readData('2024_day7.txt')
    for i, row in enumerate(data):
        numbers = list(map(int, re.findall(r'\d+', row)))
        yield numbers[0], numbers[1:]


def check(desired_result, result, operands, operations, part2 = False):
    if len(operands) == 0:
        if desired_result == result:
            return operations
        return None

    if result >=desired_result:
        return None

    operand = operands[0]

    # try addition
    path = check(desired_result, result + operand, operands[1:] if len(operands)>1 else [], ['+'] + operations, part2 )
    if path:
        return path

    # try multiplication
    path = check(desired_result, result * operand, operands[1:] if len(operands)>1 else [], ['*'] + operations, part2 )
    if path:
        return path

    if part2:
        # try concatenation
        path = check(desired_result, int(str(result) + str(operand)), operands[1:] if len(operands)>1 else [], ['||'] + operations, part2 )

    return path

answer1 = 0
for result, operands in getInput():
    path = check(result, operands[0], operands[1:], [])
    if path:
        answer1 +=result

answer2 = 0
for result, operands in getInput():
    path = check(result, operands[0], operands[1:], [], True)
    if path:
        answer2 +=result

time_end = time.time()

print(answer1)

print(answer2)
print('took ', (time_end - time_start)*1000)

