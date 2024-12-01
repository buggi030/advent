import parser
import functools

instructionsMap = {'R':1, 'L':0}

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

def lcm(a,b):
    return a*b //gcd(a,b)

def parseInstructions(line):
    result = []
    for char in line.strip():
        result.append(instructionsMap[char])
    return result

def parseLine(line):
    return line[0:3], [line[7:10],line[12:15]]

def allAtFinish(currents):
    for cur in currents:
        if cur[-1]!='Z':
            return False
    return True

def isFinishOne(item):
    return item=='ZZZ'

def isFinishTwo(item):
    return item[-1]=='Z'

def one(start,instructions,map, verbose):
    step=0
    instructionNumber=0
    finished = False
    current = start
    while not isFinishTwo(current):
        instructionNumber=step%len(instructions)
        instruction = instructions[instructionNumber]
        current =  map[current][instruction]
        verbose and print(instructionNumber, current)
        step+=1
    return step

def run(filename, verbose):
    data = parser.readData(filename)
    instructions = parseInstructions(data[0])
    countInstructions = len(instructions)
    map = {}
    starts = []
    for line in data[2:]:
        key , l = parseLine(line)
        if key[-1]=='A':
            starts.append(key)
        map[key]=l
    verbose and print(instructions, map, starts)
    instructionNumber=0
    finished = False

    answer1 = 0
    answers = []
    for start in starts:
        answers.append(one(start,instructions,map,verbose))
    answer2 = functools.reduce(lambda a, b: lcm(a,b), answers)
    return answer1, answer2

print(run('day8',False))