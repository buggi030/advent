import parser

galaxy = '#'
def getItem(map,indices):
    return map[indices[0]][indices[1]]

def scanRows(map):
    rowsToDouble = []
    for i, row in enumerate(map):
        if galaxy not in row:
            rowsToDouble.append(i)
    return rowsToDouble

def scanColumns(map):
    columnsToDouble = []
    for j in range(len(map[0])):
        foundGalaxy = False
        for i in range(len(map)):
            if map[i][j] == galaxy:
                foundGalaxy = True
                break
        if not foundGalaxy:
            columnsToDouble.append(j)
    return columnsToDouble

def run(filename, verbose):
    answer1, answer2 = 0,0
    data = parser.readData(filename)
    map = [[char for char in line.strip()  ] for line in data]
    r,c = scanRows(map), scanColumns(map)
    print(r,c)
    return answer1, answer2


answer1, answer2 = run('day11-test',True)
print(f'Answer1: {answer1}')
print(f'Answer2: {answer2}')
