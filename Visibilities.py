from typing import List, Iterable, Tuple
from itertools import product
from copy import deepcopy
import time

def visibilities(grid: List[List[int]]) -> Iterable[Tuple[int]]:
    row = len(grid)
    col = len(grid[0])
    black = []
    numbers = []
    white = []
    prohibited = []
    status = []
    current_num = {}

    in_grid = lambda x,y: 0<=x<row and 0<=y<col

    def around(x,y):
        for (dx,dy) in [(-1,0),(1,0),(0,-1),(0,1)]:
            if in_grid(x+dx,y+dy):
                yield (x+dx,y+dy)
    
    def cross(x,y):
        yield (x,y)
        for (dx,dy) in [(-1,0),(1,0),(0,-1),(0,1)]:
            (x0,y0) = (x,y)
            while in_grid(x0+dx,y0+dy) and (x0+dx,y0+dy) not in black:
                x0 += dx
                y0 += dy
                yield(x0,y0)

    def check_number(x,y):
        n = 1
        for (dx,dy) in [(-1,0),(1,0),(0,-1),(0,1)]:
            (x0,y0) = (x,y)
            while in_grid(x0+dx,y0+dy) and (x0+dx,y0+dy) not in black:
                n += 1
                x0 += dx
                y0 += dy
        return n
    
    def check_number_prohibited(x,y):
        # n = 1
        # for (dx,dy) in [(-1,0),(1,0),(0,-1),(0,1)]:
        #     (x0,y0) = (x,y)
        #     while (x0+dx,y0+dy) in prohibited or (x0+dx,y0+dy) in numbers:
        #         n += 1
        #         x0 += dx
        #         y0 += dy
        # return n
        return len(current_num[(x,y)])
    
    def guess():
        nonlocal white, black, prohibited, current_num, fail
        
        while True:
            update()
            status_temp = [deepcopy([white,black,prohibited, current_num])]
            l = 0
            while l < len(white):
                (i,j) = white[l]
                if any((x,y) in numbers or (x,y) in prohibited for (x,y) in around(i,j)):
                    fail = False
                    status_temp.append(deepcopy([white,black,prohibited, current_num, i, j]))
                    black.append((i,j))
                    white.remove((i,j))
                    update()
                    if fail or not check():
                        [white, black, prohibited, current_num, x, y] = status_temp.pop(-1)
                        white.remove((x,y))
                        prohibited.append((x,y))
                        # update()
                        continue
                        # break
                    else:
                        fail = False
                        [white, black, prohibited, current_num, i, j] = deepcopy(status_temp[-1])
                        white.remove((i,j))
                        prohibited.append((i,j))
                        update()
                        if fail or not check():
                            [white, black, prohibited, current_num, i, j] = status_temp.pop(-1)
                            white.remove((i,j))
                            black.append((i,j))
                            # update()
                            continue
                            # break
                        else:
                            [white, black, prohibited, current_num, i, j] = status_temp.pop(-1)
                            l += 1
                else:
                    l += 1
            if [white,black,prohibited, current_num] == status_temp[0]:
                break
            


    def update():
        while not fail:
            for (i,j) in numbers:
                for (dx,dy) in [(-1,0),(1,0),(0,-1),(0,1)]:
                    (x0,y0) = (i,j)
                    while (x0+dx,y0+dy) in prohibited or (x0+dx,y0+dy) in numbers:
                        x0 += dx
                        y0 += dy
                        if in_grid(x0,y0) and (x0,y0) not in current_num[(i,j)]:
                            current_num[(i,j)].append((x0,y0))

            temp = deepcopy([white,black,prohibited, current_num])
            obvious()

            if temp == [white,black,prohibited, current_num]:
                break

        

    def check():
        for (x,y) in black:
            if any((dx,dy) in black for (dx,dy) in around(x,y)):
                return False
        for (x,y) in white+prohibited:
            if all((dx,dy) in black for (dx,dy) in around(x,y)):
                return False
        for (x,y) in numbers:
            if check_number(x,y) < grid[x][y] or check_number_prohibited(x,y) > grid[x][y]:
                return False
        return True
    
    def check_finish():
        for (x,y) in black:
            if any((dx,dy) in black for (dx,dy) in around(x,y)):
                return False
        for (x,y) in prohibited:
            if all((dx,dy) in black for (dx,dy) in around(x,y)):
                return False
        for (x,y) in numbers:
            if check_number(x,y) != grid[x][y]:
                return False
        return True
    
    def obvious():
        for (x,y) in black:
            for (dx,dy) in around(x,y):
                if (dx,dy) in black:
                    fail = True
                    return
                elif (dx,dy) in white:
                    prohibited.append((dx,dy))
                    white.remove((dx,dy))
        

        for (x,y) in white+prohibited:
            temp = []
            for (dx,dy) in around(x,y):
                if (dx,dy) in prohibited or (dx,dy) in numbers:
                    temp = []
                    break
                elif (dx,dy) in white:
                    temp.append((dx,dy))
            if len(temp) == 1:
                prohibited.append(temp[0])
                white.remove(temp[0])
            
        
        for (x,y) in numbers:
            if len(current_num[(x,y)]) < grid[x][y]:
                # 1
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
                # 2
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

                if len(templist2) == 0:
                    continue
                elif len(templist2) == 1:
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

            if len(current_num[(x,y)]) == grid[x][y]:
                for (dx,dy) in [(-1,0),(1,0),(0,-1),(0,1)]:
                    (x0,y0) = (x,y)
                    while (x0+dx,y0+dy) in prohibited or (x0+dx,y0+dy) in numbers:
                        x0 += dx
                        y0 += dy
                    x0 += dx
                    y0 += dy
                    if in_grid(x0,y0):
                        if (x0,y0) in prohibited or (x0+dx,y0+dy) in numbers:
                            fail = True
                            return
                        elif (x0,y0) in white:
                            black.append((x0,y0))
                            white.remove((x0,y0))

            
           
    

    start = time.time()
    for i in range(row):
        for j in range(col):
            if grid[i][j]:
                numbers.append((i,j))
                current_num[(i,j)] = [(i,j)]
            else:
                white.append((i,j))

    
    fail = False
    # update()
    guess()

    if not white and check_finish():
        print(time.time()-start)
        return black
    '''
    while True:
        fail = False

        # white.sort(key=sort_white, reverse=True)
        for (i,j) in white:
            if not all((x,y) in black for (x,y) in around(i,j)):
            # if not all((x,y) in black for (x,y) in around(i,j)) and any((x,y) in numbers or (x,y) in prohibited for (x,y) in around(i,j)):
                status.append(deepcopy([white,black,prohibited, current_num, i, j]))
                black.append((i,j))
                white.remove((i,j))
                break

        update()
        guess()

        if fail or not check():
            [white, black, prohibited, current_num, i, j] = status.pop(-1)
            prohibited.append((i,j))
            white.remove((i,j))
            update()
            guess()
        elif not white and check_finish():
            print(time.time()-start)
            return black
    '''

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

