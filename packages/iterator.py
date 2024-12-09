
def draw(map, extra):
    for i, row in enumerate(map):
        for j, position in enumerate(row):
            if (i,j) in extra:
                print('*', end='')
            else:
                print(map[i][j], end='')
        print("")