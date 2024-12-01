import parser

def run(filename, verbose):
    data = parser.readData(filename)
    answer1 = 0
    answer2 = 0
    for line in data:
        nextValue = 0
        history = parser.ints(line)
        prevValue = history[0]
        verbose and print(prevValue, history, nextValue)
        currentSequence = history
        i=0
        while True:
            i+=1
            nextValue +=currentSequence[-1]
            currentSequence = newSecNumeric(currentSequence)
            if i&1:
                prevValue -=currentSequence[0]
            else:
                prevValue +=currentSequence[0]

            verbose and print(prevValue, currentSequence,nextValue)
            if len(list(filter(lambda x: x != 0, currentSequence)))==0:
                break
        verbose and print(prevValue, nextValue)
        answer1 +=nextValue
        answer2 += prevValue
    return answer1, answer2

def newSecNumeric(sec):
    return [sec[i+1]-sec[i] for i in range(len(sec)-1) ]


print(run('day9',False))