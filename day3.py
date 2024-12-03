from packages import parser
import re

def getInput():
    data = parser.readData('2024_day3.txt')
    return data

data = getInput()

print(data)
answer = 0
answer2 = 0
instruction = r'^mul\(\d{1,3},\d{1,3}\)'
command = r"^don't\(\)|do\(\)"
# ref = re.compile('mul\(\d{1,3},\d{1,3}\)')
enabled = True
start = 0
for d in data:
    for start in range(len(d)):
        command_match = re.match(command, d[start:])
        instruction_match = re.match(instruction, d[start:])
        if not command_match and not instruction_match:
            continue
        if instruction_match and enabled:
            a, b = re.findall(r'\d{1,3}', instruction_match.group())
            answer2 += int(a)*int(b)
            print(answer2)
        if command_match:
            enabled = 0 if command_match.group() == "don't()" else 1
            print(enabled)

#         print(command_match)
#         print(instruction_match)

#         re.findall(r'mul\(\d{1,3},\d{1,3}\)', d)
#     commands = list(re.finditer(r"don't\(\)|do\(\)", d))
#     command, commands = commands[0], commands[1:]
#
# #     for command in re.finditer(r"don't\(\)|do\(\)", d):
#     print(command.span(), command.group())
#     instructions = re.search(r'mul\(\d{1,3},\d{1,3}\)', d[start: end])
#     print(instructions)

    # Task 1
    for item in re.findall(r'mul\(\d{1,3},\d{1,3}\)', d):
        a, b = re.findall(r'\d{1,3}', item)
        answer += int(a)*int(b)
print('____')
print(answer)
print(answer2)
