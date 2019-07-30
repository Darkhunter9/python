from math import floor
import numpy as np
from copy import deepcopy

def g_key(grid, path):
    row = len(grid)
    column = len(grid[0])

    # special case
    if path == row*column:
        temp = 0
        for i in grid:
            temp += sum(i)
        return temp

    # dfs
    def route(s, x, y, step, record):
        if step > path-1 or max(row-1-x, column-1-y) > path-1-step:
            return []
        else:
            if x == row-1 and y == column-1:
                if step == path-1:
                    return [s]
                else:
                    return []
            else:
                temp_list = []
                for (dx,dy) in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                    if x+dx >= 0 and x+dx < row and y+dy >=0 and y+dy < column and (not record[(x+dx,y+dy)]):
                        temp_record = deepcopy(record)
                        temp_record[(x+dx,y+dy)] = 1
                        temp_list += route(s+grid[x+dx][y+dy], x+dx, y+dy, step+1, temp_record)

                return temp_list

    record = np.zeros((row, column), dtype=int)
    record[(0,0)] = 1
    temp = route(grid[0][0], 0, 0, 0, record)
    return max(temp)

if __name__ == '__main__':
    print("Example:")
    print(g_key([[1, 6, 7, 2, 4],
                 [0, 4, 9, 5, 3],
                 [7, 2, 5, 1, 4],
                 [3, 3, 2, 2, 9],
                 [2, 6, 1, 4, 0]], 9))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert g_key([[1, 6, 7, 2, 4],
                  [0, 4, 9, 5, 3],
                  [7, 2, 5, 1, 4],
                  [3, 3, 2, 2, 9],
                  [2, 6, 1, 4, 0]], 9) == 46

    assert g_key([[2, 5, 4, 1, 8],
                  [0, 4, 9, 5, 3],
                  [7, 2, 5, 1, 4],
                  [3, 3, 2, 2, 9],
                  [2, 6, 1, 4, 1]], 6) == 27

    assert g_key([[1, 2, 3, 4, 5],
                  [2, 3, 4, 5, 1],
                  [3, 4, 5, 1, 2],
                  [4, 5, 1, 2, 3],
                  [5, 1, 2, 3, 4]], 25) == 75

    assert g_key([[1, 6],
                  [5, 1]], 2) == 2

    print("Coding complete? Click 'Check' to earn cool rewards!")
