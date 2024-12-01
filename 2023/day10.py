import parser

directions = {
'F': ((0,1),(1,0)),
'7': ((1,0),(0,-1)),
'J': ((-1,0),(0,-1)),
'L': ((0,1),(-1,0)),
'|': ((1,0),(-1,0)),
'-': ((0,1),(0,-1)),
'S':((-1,0),(0,1), (1,0), (0,-1))
 }

def findStartPosition(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j]=='S':
                return (i,j)

    raise Exception('start is missing!')

def getItem(map,indices):
    return map[indices[0]][indices[1]]

def buildPath(head,tail):
    path = []
    prev = None
    for item in head:
        if item!=prev:
            path.append(item)
        prev = item

    for item in tail:
        if item!=prev:
            path.append(item)
        prev = item
    return path

def scanNeighbours(map, start, verbose = False):
    nexts = []
    for d in directions[getItem(map,start)]:
        candidateIndices = (start[0]+d[0],start[1]+d[1])
        if candidateIndices[0]>=len(map) or candidateIndices[1]>=len(map[0]) or candidateIndices[0]<0 or candidateIndices[1]<0:
            continue
        item = getItem(map,candidateIndices)
        invertedD = tuple([ -1*i for i in d])
        if item in directions:
            verbose and print(candidateIndices, item, directions[item], d, invertedD)
            try:
                direction = directions[item].index(invertedD)
                verbose and print(direction)
            except ValueError:
                if item !='S':
                    continue
            nexts.append(candidateIndices)
    if len(nexts)!=2:
        print(nexts)
        raise Exception('pipe is broken')
#     print(nexts,start)
    return nexts

def run(filename, verbose):
    data = parser.readData(filename)
    map = [[char for char in line.strip()  ] for line in data]
    start = findStartPosition(map)
    verbose and print('start:', start)
    startPaths = scanNeighbours(map,start, verbose)
    pointer1, pointer2 = startPaths
    prevPointer1, prevPointer2 = start,start
    finish = False
    step = 0
    head = [start]
    tail = []
    while not finish:
        head.append(pointer1)
        tail.append(pointer2)
        if pointer1==pointer2 or pointer1==prevPointer2 or pointer2 == prevPointer1:
            finish = True
        nextPaths1 = tuple(filter(lambda x: x!=prevPointer1, scanNeighbours(map,pointer1,verbose)))
        nextPaths2 = tuple(filter(lambda x: x!=prevPointer2, scanNeighbours(map,pointer2,verbose)))
        if len(nextPaths1)!=1 or len(nextPaths2)!=1:
            print(nextPaths1,nextPaths2)
            raise Exception('found too many junctions')
        nextPointer1 = nextPaths1[0]
        nextPointer2 = nextPaths2[0]
        verbose and print(prevPointer1, pointer1, nextPointer1,'-',prevPointer2, pointer2, nextPointer2)
        prevPointer1, prevPointer2 = pointer1,pointer2
        pointer1, pointer2 = nextPointer1, nextPointer2
        step+=1
    tail.reverse()
    path = buildPath(head,tail)

    tilesCount = 0
    for i in range(len(map)):
        currentTiles = 0
        verbose and print(map[i])
        isCounting = False
        isPrevPipe = False
        temp = 0
        for j in range(len(map[0])):
            if (i,j) in path:
                if not isCounting and temp and map[i][j]=='|':
                    isCounting = False
                    continue

                tilesCount+=currentTiles
                currentTiles=0
                isCounting = True
                isPrevPipe = True
                if map[i][j]=='|':
                    temp +=1
                else:
                    temp = 0
                continue
            if isCounting:
                temp = 0
                isPrevPipe=False
                currentTiles+=1
    return step, tilesCount


answer1, answer2 = run('day10-test',True)
print(f'Answer1: {answer1}')
print(f'Answer2: {answer2}')
