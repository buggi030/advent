from functools import wraps

def determinant(matrix):
    if len(matrix)!= 2 or len(matrix[0])!= 2:
        raise 'not supported'

    return matrix[0][0]*matrix[1][1] - matrix[0][1] * matrix[1][0]

