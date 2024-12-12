from packages import parser
from packages import parser
from packages import utils
import re
import time
import sys

time_start = time.time()
sys.setrecursionlimit(2000)

def getInput():
    data = parser.readData('2024_day11.txt')
    return re.findall(r'\d+', data[0])

data = getInput()

BLINKS = 998
total = 0

@utils.memoize
def blink(stone, level):
    if level == 0:
        return 1
    if stone == '0':
        return blink('1', level-1)
    if len(stone) % 2 == 0:
        left = str(int(stone[0:len(stone)//2]))
        right = str(int(stone[len(stone)//2:]))
        return blink(left, level-1) + blink(right, level-1)

    multiplied = int(stone)*2024
    return blink(str(multiplied), level-1)


for stone in data:
    total+= blink(stone, BLINKS)

print(total)
print((time.time() - time_start)*1000)
print(utils.getStats())