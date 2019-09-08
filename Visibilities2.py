from typing import List, Iterable, Tuple
from itertools import product
from copy import deepcopy
import time

def visibilities(grid: List[List[int]]) -> Iterable[Tuple[int]]:
    row = len(grid)
    col = len(grid[0])
    black = []
    numbers = []
    numbers_need_check = []
    white = []
    prohibited = []
    status = []
    sure_num = {}
    available_num = {}
    fail = False

    in_grid = lambda x,y: 0<=x<row and 0<=y<col

    def around(x,y):
        for (dx,dy) in [(-1,0),(1,0),(0,-1),(0,1)]:
            if in_grid(x+dx,y+dy):
                yield (x+dx,y+dy)

    def update_num():
        nonlocal fail,white,black,prohibited,sure_num,available_num,numbers_need_check
        for (i,j) in numbers:
            for (dx,dy) in [(-1,0),(1,0),(0,-1),(0,1)]:
                (x0,y0) = (i,j)
                while (x0+dx,y0+dy) in prohibited or (x0+dx,y0+dy) in numbers:
                    x0 += dx
                    y0 += dy
                    if (x0,y0) not in sure_num[(i,j)]:
                        sure_num[(i,j)].append((x0,y0))
            for (dx,dy) in [(-1,0),(1,0),(0,-1),(0,1)]:
                (x0,y0) = (i,j)
                while in_grid(x0+dx,y0+dy) and (x0+dx,y0+dy) not in black:
                    x0 += dx
                    y0 += dy
                    if  (x0,y0) not in available_num[(i,j)]:
                        available_num[(i,j)].append((x0,y0))

    def check_finish():
        for (x,y) in black:
            if any((dx,dy) in black for (dx,dy) in around(x,y)):
                return False
        for (x,y) in prohibited:
            if all((dx,dy) in black for (dx,dy) in around(x,y)):
                return False
        for (x,y) in numbers:
            if len(sure_num[(x,y)]) != grid[x][y]:
                return False
        return True

    def obvious():
        nonlocal fail,white,black,prohibited,sure_num,available_num,numbers_need_check
        if fail:
            return

        for (x,y) in black:
            for (dx,dy) in around(x,y):
                if (dx,dy) in black:
                    fail = True
                    return
                elif (dx,dy) in white:
                    prohibited.append((dx,dy))
                    white.remove((dx,dy))
        
        for (x,y) in prohibited:
            temp = [(dx,dy) for (dx,dy) in around(x,y) if (dx,dy) not in black]
            if len(temp) == 1 and temp[0] in white:
                prohibited.append(temp[0])
                white.remove(temp[0])
            elif not len(temp):
                fail = True
                return
        
        for (x,y) in white:
            if all((dx,dy) in black for (dx,dy) in around(x,y)):
                fail = True
                return
        
        for (x,y) in numbers:
            # if (x,y) in numbers_need_check:
            if len(sure_num[(x,y)]) != len(available_num[(x,y)]):
                if len(sure_num[(x,y)]) == grid[x][y]:
                    x0 = x
                    y0 = min([dy for (dx,dy) in sure_num[(x,y)]])-1
                    y1 = max([dy for (dx,dy) in sure_num[(x,y)]])+1
                    if (x0,y0) in white:
                        black.append((x0,y0))
                        white.remove((x0,y0))
                    if (x0,y1) in white:
                        black.append((x0,y1))
                        white.remove((x0,y1))
                    y0 = y
                    x0 = min([dx for (dx,dy) in sure_num[(x,y)]])-1
                    x1 = max([dx for (dx,dy) in sure_num[(x,y)]])+1
                    if (x0,y0) in white:
                        black.append((x0,y0))
                        white.remove((x0,y0))
                    if (x1,y0) in white:
                        black.append((x1,y0))
                        white.remove((x1,y0))
                    # numbers_need_check.remove((x,y))
                    continue
                elif len(sure_num[(x,y)]) < grid[x][y]:
                    #1
                    templist = [0]*4
                    templist2 = [(-1,0),(1,0),(0,-1),(0,1)]
                    for i in range(4):
                        n = 0
                        (x0,y0) = (x,y)
                        (dx,dy) = templist2[i]
                        while in_grid(x0+dx,y0+dy) and (x0+dx,y0+dy) not in black:
                            templist[i] += 1
                            x0 += dx
                            y0 += dy

                    for i in range(4):
                        iterlist = [0,1,2,3]
                        iterlist.pop(i)
                        delta = grid[x][y] - 1 - sum([templist[j] for j in iterlist])
                        if delta > 0:
                            (x0,y0) = (x,y)
                            (dx,dy) = templist2[i]
                            for j in range(delta):
                                if not in_grid(x0+dx,y0+dy) or (x0+dx,y0+dy) in black:
                                    fail = False
                                    return
                                else:
                                    x0 += dx
                                    y0 += dy
                                    if (x0,y0) in white:
                                        prohibited.append((x0,y0))
                                        white.remove((x0,y0))
                    
                    #2
                    templist = []
                    templist2 = []
                    for (dx,dy) in [(-1,0),(1,0),(0,-1),(0,1)]:
                        n = 0
                        (x0,y0) = (x,y)
                        while (x0+dx,y0+dy) in prohibited or (x0+dx,y0+dy) in numbers:
                            x0 += dx
                            y0 += dy
                            n += 1
                        if not in_grid(x0+dx,y0+dy) or (x0+dx,y0+dy) in black:
                            templist.append(n)
                        else:
                            templist2.append((dx,dy))
                        if len(templist2) > 1:
                            templist2 = []
                            break
                    
                    if len(templist2) == 1:
                        (dx,dy) = templist2[0]
                        delta = grid[x][y] - 1 - sum(templist)
                        (x0,y0) = (x,y)
                        for i in range(delta):
                            x0 += dx
                            y0 += dy
                            if (x0,y0) in prohibited or (x0,y0) in numbers:
                                continue
                            elif (x0,y0) in black or not in_grid(x0,y0):
                                fail = True
                                return
                            else:
                                prohibited.append((x0,y0))
                                white.remove((x0,y0))
                        x0 += dx
                        y0 += dy
                        if not in_grid(x0,y0) or (x0,y0) in black:
                            pass
                        elif (x0,y0) in prohibited or (x0,y0) in numbers:
                            fail = True
                            return
                        else:
                            black.append((x0,y0))
                            white.remove((x0,y0))
                            # numbers_need_check.remove((x,y))
                            continue

                else:
                    fail = True
                    return
                
                if len(available_num[(x,y)]) == grid[x][y]:
                    for (dx,dy) in available_num[(x,y)]:
                        if (dx,dy) not in prohibited:
                            white.remove((dx,dy))
                            prohibited.append((dx,dy))
                    # numbers_need_check.remove((x,y))
                    continue

    def guess():
        nonlocal fail,white,black,prohibited,sure_num,available_num,numbers_need_check
        for (i,j) in deepcopy(white):
            if (i,j) in white and not all((x,y) in white for (x,y) in around(i,j)):
                fail = False
                status = deepcopy([white,black,prohibited,sure_num,available_num])
                black.append((i,j))
                white.remove((i,j))

                # start = time.time()
                while True:
                    status2 = deepcopy([white,black,prohibited])
                    obvious()
                    update_num()
                    if status2 == [white,black,prohibited]:
                        break
                # print('1:'+str(time.time()-start))

                if fail or any(len(available_num[(x,y)]) < grid[x][y] or len(sure_num[(x,y)]) > grid[x][y] for (x,y) in numbers):
                    [white,black,prohibited,sure_num,available_num] = deepcopy(status)
                    white.remove((i,j))
                    prohibited.append((i,j))

                    # start = time.time()
                    while True:
                        status2 = deepcopy([white,black,prohibited])
                        obvious()
                        update_num()
                        if status2 == [white,black,prohibited]:
                            break
                    # print('2:'+str(time.time()-start))
                
                else:
                    fail = False
                    [white,black,prohibited,sure_num,available_num] = deepcopy(status)
                    white.remove((i,j))
                    prohibited.append((i,j))

                    # start = time.time()
                    while True:
                        status2 = deepcopy([white,black,prohibited])
                        obvious()
                        update_num()
                        if status2 == [white,black,prohibited]:
                            break
                    # print('3:'+str(time.time()-start))

                    if fail or any(len(available_num[(x,y)]) < grid[x][y] or len(sure_num[(x,y)]) > grid[x][y] for (x,y) in numbers):
                        [white,black,prohibited,sure_num,available_num] = deepcopy(status)
                        white.remove((i,j))
                        black.append((i,j))

                        # start = time.time()
                        while True:
                            status2 = deepcopy([white,black,prohibited])
                            obvious()
                            update_num()
                            if status2 == [white,black,prohibited]:
                                break
                        # print('4:'+str(time.time()-start))
                    
                    else:
                        [white,black,prohibited,sure_num,available_num] = deepcopy(status)

    def guess2():
        nonlocal fail,white,black,prohibited,sure_num,available_num,numbers_need_check
        for (k,l) in numbers:
            if grid[k][l] <= 4:
                for (i,j) in around(k,l):
                # for (i,j) in deepcopy(white):
                    if (i,j) in white and not all((x,y) in white for (x,y) in around(i,j)):
                        fail = False
                        status = deepcopy([white,black,prohibited,sure_num,available_num])
                        black.append((i,j))
                        white.remove((i,j))

                        # start = time.time()
                        while True:
                            status2 = deepcopy([white,black,prohibited])
                            obvious()
                            update_num()
                            if status2 == [white,black,prohibited]:
                                break
                        # print('1:'+str(time.time()-start))

                        if fail or any(len(available_num[(x,y)]) < grid[x][y] or len(sure_num[(x,y)]) > grid[x][y] for (x,y) in numbers):
                            [white,black,prohibited,sure_num,available_num] = deepcopy(status)
                            white.remove((i,j))
                            prohibited.append((i,j))

                            # start = time.time()
                            while True:
                                status2 = deepcopy([white,black,prohibited])
                                obvious()
                                update_num()
                                if status2 == [white,black,prohibited]:
                                    break
                            # print('2:'+str(time.time()-start))
                        
                        else:
                            fail = False
                            [white,black,prohibited,sure_num,available_num] = deepcopy(status)
                            white.remove((i,j))
                            prohibited.append((i,j))

                            # start = time.time()
                            while True:
                                status2 = deepcopy([white,black,prohibited])
                                obvious()
                                update_num()
                                if status2 == [white,black,prohibited]:
                                    break
                            # print('3:'+str(time.time()-start))

                            if fail or any(len(available_num[(x,y)]) < grid[x][y] or len(sure_num[(x,y)]) > grid[x][y] for (x,y) in numbers):
                                [white,black,prohibited,sure_num,available_num] = deepcopy(status)
                                white.remove((i,j))
                                black.append((i,j))

                                # start = time.time()
                                while True:
                                    status2 = deepcopy([white,black,prohibited])
                                    obvious()
                                    update_num()
                                    if status2 == [white,black,prohibited]:
                                        break
                                # print('4:'+str(time.time()-start))
                            
                            else:
                                [white,black,prohibited,sure_num,available_num] = deepcopy(status)


    for i in range(row):
        for j in range(col):
            if grid[i][j]:
                numbers.append((i,j))
                sure_num[(i,j)] = [(i,j)]
                available_num[(i,j)] = [(i,j)]
            else:
                white.append((i,j))

    numbers_need_check = deepcopy(numbers)
    update_num()
    while True:
        status = deepcopy([white,black,prohibited])
        obvious()
        update_num()
        if status == [white,black,prohibited]:
            break
    
    # guess2()
    # guess2()
    while True:
        guess()
        while True:
            status = deepcopy([white,black,prohibited])
            obvious()
            update_num()
            if status == [white,black,prohibited]:
                break
        if not white:
            return black
    pass



if __name__ == '__main__':
    def checker(func, grid):
        result = func([row[:] for row in grid])
        BLACK, MOVES = -1, ((-1, 0), (1, 0), (0, -1), (0, 1))
        in_grid = lambda i, j: 0 <= i < len(grid) and 0 <= j < len(grid[0])
        for item in result:
            if not (isinstance(item, (tuple, list)) and len(item) == 2 and
                    all(isinstance(n, int) for n in item)):
                print(f"You should give tuples/lists of 2 ints, not {item}.")
                return False
            i, j = item
            if not in_grid(i, j):
                print(f"{(i, j)} is outside the grid.")
                return False
            if grid[i][j] > 0:
                print("You can't put a black box on the "
                      f"number {grid[i][j]} at {(i, j)}.")
                return False
            if grid[i][j] == BLACK:
                print(f"You can't put a black box twice at {(i, j)}.")
                return False
            for x, y in ((i + di, j + dj) for di, dj in MOVES):
                if in_grid(x, y) and grid[x][y] == BLACK: # RULE 1
                    print(f"You can't put a black box at {(x, y)} because "
                          f"there is a box at {(i, j)}, it's too close.")
                    return False
            grid[i][j] = BLACK
        from numpy import array
        from scipy.ndimage import label # Powerful tool.
        bool_array = array([[n != BLACK for n in row] for row in grid])
        num_pieces = label(bool_array)[1]
        if num_pieces > 1: # RULE 2
            print("White boxes in the grid should not be separated "
                  f"into {num_pieces} pieces by black boxes.")
            return False
        numbers = ((i, j, n) for i, row in enumerate(grid)
                             for j, n in enumerate(row) if n > 0)
        for i, j, n in numbers:
            visibility_from_n = 1
            for di, dj in MOVES:
                x, y = i + di, j + dj
                while in_grid(x, y) and grid[x][y] != BLACK:
                    visibility_from_n += 1
                    x, y = x + di, y + dj
            if visibility_from_n != n: # RULE 3
                print(f"The box at {(i, j)} should see "
                      f"{n} boxes, not {visibility_from_n}.")
                return False
        return True

    # visibilities([[0,0,9,0,0,7,0,0,0],[0,0,0,0,4,0,0,0,0],[0,9,0,0,0,7,0,0,7],[0,0,0,0,0,0,0,0,0],[0,0,0,9,0,0,10,0,0],[0,0,0,0,0,0,0,0,0],[17,0,0,0,3,0,0,14,9],[0,0,0,7,0,0,0,0,0],[0,0,0,0,0,9,0,0,0],[21,7,0,0,7,0,0,0,4],[0,0,0,0,0,0,0,0,0],[0,0,14,0,0,10,0,0,0],[0,0,0,0,0,0,0,0,0],[16,0,0,10,0,0,0,17,0],[0,0,0,0,4,0,0,0,0],[0,0,0,2,0,0,5,0,0]])
    visibilities([[0,0,0,0,0,0,0,16,0,0,0,0,12,0,0,0,0,0,0,0,5,0,0,0,10,0,0,13,0,0,0,0],[0,5,8,0,0,0,6,0,0,0,0,3,0,0,0,0,0,0,8,0,0,0,0,4,0,0,0,0,0,0,0,7],[0,0,0,0,0,0,0,11,0,0,0,0,0,8,0,11,0,5,0,0,0,0,0,0,0,0,0,0,4,0,0,0],[0,0,13,0,0,0,0,0,0,0,0,14,0,0,0,0,0,0,0,0,6,0,0,0,0,0,6,0,0,0,13,0],[0,0,0,0,0,0,0,14,0,0,0,0,0,16,0,18,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0],[7,0,7,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,16,0,0,0,0,0,8,0,0,13,0],[6,4,0,0,7,0,4,2,0,13,0,19,0,0,0,0,0,0,0,0,0,0,2,0,0,0,12,0,11,0,0,0],[0,0,0,0,0,0,0,0,5,0,0,0,0,0,11,0,0,0,0,10,13,0,0,0,5,0,5,0,0,0,0,0],[5,0,0,0,0,0,0,0,0,0,0,20,0,0,0,20,0,0,0,0,18,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,15,0,0,0,0,11,0,0,0,18,0,0,0,0,0,0,0,0,0,0,10],[0,0,0,0,0,13,0,7,0,0,0,10,13,0,0,0,0,12,0,0,0,0,0,7,0,0,0,0,0,0,0,0],[0,0,0,10,0,13,0,0,0,16,0,0,0,0,0,0,0,0,0,0,17,0,10,0,10,13,0,6,0,0,16,8],[0,16,0,0,13,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,0,0,11,0,0,0,0,0,0,17,0,4],[0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,10,0,6,0,0,0,0,0,6,0,0,0,0,0,0,0],[0,12,0,0,0,8,0,0,0,0,0,5,0,0,0,0,0,0,0,0,17,0,0,0,0,0,0,0,0,14,0,0],[0,0,0,11,0,0,0,0,0,0,0,0,0,0,12,0,2,0,9,0,0,0,0,0,9,0,0,0,0,0,0,0],[9,0,0,0,0,0,0,0,7,0,0,0,0,5,0,0,0,0,0,0,11,0,0,0,0,9,0,0,0,12,7,0],[0,0,0,0,3,0,0,5,0,0,0,7,0,0,0,0,0,0,0,5,0,0,0,0,8,0,0,0,0,0,0,0]])
    # visibilities([[0,0,7,0,0,0,0,0,0,0,3,0,0,0,0,0,0],[7,0,0,15,0,0,0,4,0,0,0,0,3,0,4,9,0],[0,0,9,0,0,0,0,0,0,0,7,0,0,0,0,0,5],[0,0,0,13,0,0,0,0,11,0,0,0,0,3,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],[6,0,0,11,0,6,8,0,0,0,0,12,0,0,3,0,0],[0,3,0,0,0,0,0,0,0,11,9,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0],[0,0,23,0,0,0,0,0,15,0,0,0,20,0,0,0,0],[0,0,0,0,8,0,0,0,7,0,0,0,0,0,5,0,0],[0,0,13,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,19,18,0,0,0,0,0,0,0,20,0],[0,0,18,0,0,13,0,0,0,0,12,12,0,11,0,0,8],[11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,7,0,0,0,0,11,0,0,0,0,14,0,0,0],[10,0,0,0,0,0,5,0,0,0,0,0,0,0,11,0,0],[0,6,15,0,8,0,0,0,0,7,0,0,0,10,0,0,5],[0,0,0,0,0,0,5,0,0,0,0,0,0,0,8,0,0]])
    GRIDS = (
             ('5x5', [[0, 0, 4, 0, 6],
                      [0, 6, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 5, 0],
                      [6, 0, 7, 0, 0]]),

             ('5x8', [[0, 0, 0, 0, 0, 0, 4, 7],
                      [0, 0, 0, 0, 4, 0, 3, 0],
                      [0, 0, 8, 0, 0, 7, 0, 0],
                      [0, 4, 0, 6, 0, 0, 0, 0],
                      [6, 5, 0, 0, 0, 0, 0, 0]]),

             ('6x9', [[6, 0, 0, 8, 0, 0, 4, 0, 0],
                      [0, 0, 0, 9, 0, 0, 0, 0, 0],
                      [7, 3, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 7, 8],
                      [0, 0, 0, 0, 0, 2, 0, 0, 0],
                      [0, 0, 9, 0, 0, 8, 0, 0, 12]]),

             ('8x12', [[0, 0, 0, 2, 0, 0, 6, 0, 0, 0, 0, 0],
                       [0, 5, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0],
                       [0, 6, 0, 0, 0, 13, 0, 0, 0, 10, 0, 0],
                       [0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 8, 6],
                       [8, 3, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0],
                       [0, 0, 9, 0, 0, 0, 5, 0, 0, 0, 7, 0],
                       [0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 10, 0],
                       [0, 0, 0, 0, 0, 13, 0, 0, 7, 0, 0, 0]]),)

    for dim, grid in GRIDS:
        assert checker(visibilities, grid), f"You failed on the grid {dim}."

