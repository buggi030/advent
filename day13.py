from packages import parser
from packages import matrix
import re
import time

time_start = time.time()

def getInput():
    data = parser.readData('2024_day13.txt')
    equations = []
    for i in range(0, len(data),4):
        stepsA = list(map(int,re.findall(r'\d+',data[i])))
        stepsB = list(map(int,re.findall(r'\d+',data[i+1])))
        result = list(map(int,re.findall(r'\d+',data[i+2])))
        result2 = [r + 10000000000000 for r in result]
        equations.append((result, [[stepsA[0],stepsB[0]], [stepsA[1], stepsB[1]]], result2))
    return equations

equations = getInput()
print(equations)


def replaced_matrix(matrix, new_column, index):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[i])):
            if j == index:
                new_matrix[i].append(new_column[i])
            else:
                new_matrix[i].append(matrix[i][j])
    return new_matrix
PRICE_A = 3
PRICE_B = 1
answer1 = 0
for equation in equations:
    determinant = matrix.determinant(equation[1])
    print(equation[1], determinant)
    replaced1 = replaced_matrix(equation[1],equation[2], 0 )
    determinant1 = matrix.determinant(replaced1)
    print(replaced1, determinant1)

    replaced2 = replaced_matrix(equation[1],equation[2], 1 )
    determinant2 = matrix.determinant(replaced2)
    a = determinant1/determinant
    b = determinant2/determinant
    if a.is_integer() and b.is_integer():
        print(a,b)
        answer1 += int(a)*PRICE_A + int(b)*PRICE_B
    print('_____')
print(answer1)