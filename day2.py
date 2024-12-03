from packages import parser

def getInput():
    reports = []
    data = parser.readData('2024_day2.txt')
    for d in data:
        reports.append(list(map(int,d.split())))
    return reports


def valid(report):
    invalid = False
    order = None
    previous = report[0]
    for i in range(1, len(report)):
        diff = report[i] - previous
        if order is None:
            order = 'asc' if diff > 0 else 'desc'
        if diff == 0:
            invalid = True
            break
        if order == 'desc' and (diff >0 or diff <-3):
            invalid = True
            break
        if order == 'asc' and (diff <1 or diff > 3):
            invalid = True
            break
        previous = report[i]
    return not invalid

reports = getInput()
answer1 = 0
# Task 1
# for report in reports:
#     if valid(report):
#         answer1 +=1

answer2 = 0
for report in reports:
    print(report)
    if valid(report):
        answer2 +=1
        continue
    for i in range(len(report)):
        candidate = report[:i] + report[i+1:]
        if valid(candidate):
            answer2 +=1
            break



print(answer2)