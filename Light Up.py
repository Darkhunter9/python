from typing import Tuple, Iterable  # or List, Set...
import numpy as np
from copy import deepcopy

def neighbour(row, col, i, j):
    for (di, dj) in [(-1,0),(1,0),(0,-1),(0,1)]:
        if 0 <= i+di < row and 0 <= j+dj < col:
            yield (i+di,j+dj)

def find_blank(grid, light, record, prohibited):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (not light[(i,j)]) and (not record[(i,j)]) and (not prohibited[(i,j)]):
                yield (i,j)

def update(grid, record, x, y):
    row = len(grid)
    col = len(grid[0])
    record[(x,y)] = 1
    dx1 = x-1
    dx2 = x+1
    dy1 = y-1
    dy2 = y+1
    while dx1 >= 0:
        if grid[dx1][y] == ' ':
            record[(dx1, y)] = 1
            dx1 -= 1
        else:
            break
    while dx2 < row:
        if grid[dx2][y] == ' ':
            record[(dx2, y)] = 1
            dx2 += 1
        else:
            break
    while dy1 >= 0:
        if grid[x][dy1] == ' ':
            record[(x, dy1)] = 1
            dy1 -= 1
        else:
            break
    while dy2 < col:
        if grid[x][dy2] == ' ':
            record[(x, dy2)] = 1
            dy2 += 1
        else:
            break
    
    return record

def conflict(grid, light, record, pos_wall, prohibited):
    row = len(grid)
    col = len(grid[0])
    
    # check lights
    zeros = np.where(light == 1)
    for (i,j) in zip(zeros[0],zeros[1]):
        di1 = i-1
        di2 = i+1
        dj1 = j-1
        dj2 = j+1
        n = 0
        while di1 >= 0:
            if n > 0:
                break
            if record[(di1,j)] == -1:
                break
            elif light[(di1,j)] == 1:
                n += 1
                break
            else:
                di1 -= 1

        while di2 < row:
            if n > 0:
                break
            if record[(di2,j)] == -1:
                break
            elif light[(di2,j)] == 1:
                n += 1
                break
            else:
                di2 += 1

        while dj1 >= 0:
            if n > 0:
                break
            if record[(i,dj1)] == -1:
                break
            elif light[(i,dj1)] == 1:
                n += 1
                break
            else:
                dj1 -= 1

        while dj2 < col:
            if n > 0:
                break
            if record[(i,dj2)] == -1:
                break
            elif light[(i,dj2)] == 1:
                n += 1
                break
            else:
                dj2 += 1

        if n > 0:
            return True
    
    # check whether wall are surrounded with right number of light
    # X01234
    for (i,j) in zip(pos_wall[0], pos_wall[1]):
        if grid[i][j] not in ' X':
            target = int(grid[i][j])
            available = 0
            for (di, dj) in neighbour(row, col, i, j):
                    if light[(di,dj)] == 1:
                        target -= 1
                    if record[(di,dj)] == 0 and prohibited[(di,dj)] == 0:
                        available += 1
            if target < 0 or available < target:
                return True
    
    # check impossible
    zeros = np.where((record == 0) & (prohibited == 1))
    for (i,j) in zip(zeros[0],zeros[1]):
        di1 = i-1
        di2 = i+1
        dj1 = j-1
        dj2 = j+1
        n = 0
        while di1 >= 0:
            if n > 0:
                break
            if record[(di1,j)] == -1:
                break
            elif record[(di1,j)] == 0 and prohibited[(di1,j)] != 1:
                n += 1
                break
            else:
                di1 -= 1

        while di2 < row:
            if n > 0:
                break
            if record[(di2,j)] == -1:
                break
            elif record[(di2,j)] == 0 and prohibited[(di2,j)] != 1:
                n += 1
                break
            else:
                di2 += 1

        while dj1 >= 0:
            if n > 0:
                break
            if record[(i,dj1)] == -1:
                break
            elif record[(i,dj1)] == 0 and prohibited[(i,dj1)] != 1:
                n += 1
                break
            else:
                dj1 -= 1

        while dj2 < col:
            if n > 0:
                break
            if record[(i,dj2)] == -1:
                break
            elif record[(i,dj2)] == 0 and prohibited[(i,dj2)] != 1:
                n += 1
                break
            else:
                dj2 += 1

        if n == 0:
            return True
    return False

def obvious(grid, light, record, pos_wall, prohibited):
    row = len(grid)
    col = len(grid[0])
    for (i,j) in zip(pos_wall[0], pos_wall[1]):
        if grid[i][j] not in '0X':
            target = int(grid[i][j])
            available = []
            for (di, dj) in neighbour(row, col, i, j):
                if light[(di,dj)] == 1:
                    target -= 1
                elif record[(di,dj)] == 0 and (not prohibited[(di,dj)]):
                    available.append((di, dj))
            if len(available) == target:
                for (di,dj) in available:
                    light[(di,dj)] = 1
                    record = update(grid, record, di, dj)
            if not target:
                for (di,dj) in available:
                    prohibited[(di,dj)] = 1
    
    zeros = np.where(record == 0)
    for (i,j) in zip(zeros[0],zeros[1]):
        if not record[(i,j)]:
            di1 = i-1
            di2 = i+1
            dj1 = j-1
            dj2 = j+1
            n = []
            if not prohibited[(i,j)]:
                n.append((i,j))
            
            while di1 >= 0:
                if len(n) > 1:
                    break
                if record[(di1,j)] == -1:
                    break
                elif record[(di1,j)] == 0 and prohibited[(di1,j)] == 0:
                    n.append((di1,j))
                di1 -= 1

            while di2 < row:
                if len(n) > 1:
                    break
                if record[(di2,j)] == -1:
                    break
                elif record[(di2,j)] == 0 and prohibited[(di2,j)] == 0:
                    n.append((di2,j))
                di2 += 1

            while dj1 >= 0:
                if len(n) > 1:
                    break
                if record[(i,dj1)] == -1:
                    break
                elif record[(i,dj1)] == 0 and prohibited[(i,dj1)] == 0:
                    n.append((i,dj1))
                dj1 -= 1

            while dj2 < col:
                if len(n) > 1:
                    break
                if record[(i,dj2)] == -1:
                    break
                elif record[(i,dj2)] == 0 and prohibited[(i,dj2)] == 0:
                    n.append((i,dj2))
                dj2 += 1

            if len(n) == 1:
                (x,y) = n[0]
                light[(x,y)] = 1
                record = update(grid, record, x, y)

    return (light, record, prohibited)

def solve(grid, light, record, pos_wall, prohibited):
    if (0 not in record) and (not conflict(grid, light, record, pos_wall, prohibited)):
        return light
    else:
        result = None
        row = len(grid)
        col = len(grid[0])

        while True:
            temp_light = deepcopy(light)
            temp_record = deepcopy(record)
            temp_prohibited = deepcopy(prohibited)
            (light, record, prohibited) = obvious(grid, light, record, pos_wall, prohibited)
            if np.all(temp_light == light) and np.all(temp_record == record) and np.all(temp_prohibited == prohibited):
                if (0 not in record) and (not conflict(grid, light, record, pos_wall, prohibited)):
                    return light
                break
        if conflict(grid, light, record, pos_wall, prohibited):
            return None
        else:
            for (i,j) in find_blank(grid, light, record, prohibited):
                light[(i,j)] = 1
                result = solve(grid, deepcopy(light), update(grid, deepcopy(record), i, j), pos_wall, deepcopy(prohibited))
                if result is not None:
                    return result
                else:
                    light[(i,j)] = 0
                    prohibited[(i,j)] = 1
    return result

def light_up(grid: Tuple[str]) -> Iterable[Tuple[int]]:
    row = len(grid)
    col = len(grid[0])

    coord = []
    record = np.zeros((row,col), dtype=int) # whether the grid is illuminated
    light = np.zeros_like(record, dtype=int) # pos of the lights
    prohibited = np.zeros_like(record, dtype=int)
    for i in range(row):
        for j in range(col):
            if grid[i][j] != ' ':
                record[(i,j)] = -1
                light[(i,j)] = -1
                prohibited[(i,j)] = 1

                if grid[i][j] == '4':
                    for (di, dj) in [(-1,0),(1,0),(0,-1),(0,1)]:
                        light[(i+di,j+dj)] = 1
                        record = update(grid, record, i+di, j+dj)
                elif grid[i][j] == '0':
                    for (di, dj) in [(-1,0),(1,0),(0,-1),(0,1)]:
                            if 0 <= i+di < len(grid) and 0 <= j+dj < len(grid[0]):
                                prohibited[(i+di,j+dj)] = 1
    for i in range(row):
        for j in range(col):
            if grid[i][j] == ' ':
                if all(record[(di,dj)] == -1 for (di, dj) in neighbour(row, col, i, j)):
                    light[(i,j)] = 1
                    record = update(grid, record, i, j)
                
    pos_wall = np.where(light == -1)
    

    result = solve(grid, light, record, pos_wall, prohibited)
    pos_light = np.where(result == 1)
    return zip(pos_light[0].tolist(),pos_light[1].tolist())


if __name__ == '__main__':
    light_up(["  01  X   1  XX 3 X X  X X    ","  XX   X XX0X1 X   X       2  "," X  XX   1 XXX  X   2       X1","    0X 2    X  XXX     XXX  XX","1  1XX XX  X  X  1 X1  1 XXX  ","   X X  X  2    X XX1  XXXXX  ","0  XX1 XXXXXX X1     X       2","       X1  X  X0      XX X1 2 ","      X  X X    XX 0  XXXX    ","2 0 XX         2   X X X   XX "," X  XX  0XXX  1 1 XX   X    1X","X    X    0X XX X X2 2XXXX 1X ","   X3   X    X         X  XXX ","2 XX 3  X XX   3 XX        XX0"," X X  X2 1   X    XX  0X X   X","X   X 00  X0    X   1 XX  1 X ","110        X1 X   XX X  3 X2 X"," XXX  X         X    0   XX   "," X0 2XX0X XX 1 XX X1    X    X","XX    X   X1 X X  1X0X  XX  2 "," XX   2 X X   2         XX X 3","    XXXX  2 XX    X 0  X      "," X XX XX      XX  2  XX       ","2       X     11 XXX1XX XX1  X","  XXXXX  XX3 X    X  X  2 X   ","  XXX 2  0X X  1  X  0X XXX  X","01  XXX     1XX  X    X X1    ","XX       1   X  XX1 X   XX  1 ","  1       1   X XX1XX 1   X1  ","    1 1  X X X XX  X   0  X1  "])
    light_up(["  21     0 2 X"," 2      XX    "," 0      X0    ","   1       1X ","2  1X   X     ","  1   X  1   2","       0  2   ","   1  0       ","0   1  1   1  ","     X   01  0"," XX       1   ","    01      0 ","    X2      X ","2 1 X     X0  "])
    light_up(["     X    ","      1   ","   03  1X ","0    2X X "," 0  X     ","     2  1 "," 1 0X    2"," XX  11   ","   0      ","    0     "])
    def checker(function, grid):
        result = function(grid)
        # Check it...
        *WALLS, LIGHT, LIT, DARK = '01234XL. '
        grid = list(map(list, grid))
        nb_rows, nb_cols = len(grid), len(grid[0])
        # Check types and transform result into a Set[Tuple[int]].
        user_lights = set()
        for elem in result:
            if not (isinstance(elem, (tuple, list)) and len(elem) == 2
                    and all(isinstance(n, int) for n in elem)):
                print("Your iterable result should contain "
                      "tuples/lists of 2 ints.")
                return False
            i, j = light = tuple(elem)
            if light in user_lights:  # Duplicates are not allowed.
                print(f"You can't put two lights at the same place {light}.")
                return False
            if not (0 <= i < nb_rows and 0 <= j < nb_cols):
                print("You can't put a light outside the grid "
                      f"like at {light}.")
                return False
            user_lights.add(light)
        # Check if the result respect numbers in the grid.
        digits = ((i, j, int(cell))
                  for i, row in enumerate(grid)
                  for j, cell in enumerate(row) if cell.isdigit())
        for i, j, nb_lights in digits:
            nb_user_lights = len({(i - 1, j), (i, j - 1),
                                  (i + 1, j), (i, j + 1)} & user_lights)
            if nb_user_lights != nb_lights:
                print(f"The cell {(i, j)} should have {nb_lights} "
                      f"neighboring lights, not {nb_user_lights}.")
                return False
        # Put user lights on the grid, check if it's possible.
        for i, j in user_lights:
            if grid[i][j] == LIT:  # LIGHTS CONFLICT!
                print(f"Light at {(i, j)} is wrongly lit by another.")
                return False
            if grid[i][j] in WALLS:
                print(f"You can't put a light in the wall at {(i, j)}.")
                return False
            grid[i][j] = LIGHT  # Put a light in DARKness.
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = i + di, j + dj
                while (0 <= ni < nb_rows and 0 <= nj < nb_cols
                       and grid[ni][nj] not in WALLS):
                    grid[ni][nj] = LIT
                    ni, nj = ni + di, nj + dj
        # Finally, check if the all grid is lit.
        nb_dark = sum(row.count(DARK) for row in grid)
        if nb_dark:
            print(f"There are still {nb_dark} cell(s) in the dark.")
            return False
        return True

    GRIDS = (
            # ('    1  ',
            #   '   0X  ',
            #   'X2     ',
            #   ' 0   0 ',
            #   '     11',
            #   '  X0   ',
            #   '  1    '),

            #  ('    X X',
            #   '  X    ',
            #   ' 2     ',
            #   '   4   ',
            #   '  X   X',
            #   '0   2  ',
            #   '   3   ',
            #   '     2 ',
            #   '    X  ',
            #   '1 0    '),

             ('        2 ',
              '   1      ',
              '1     2  X',
              '1  1   3  ',
              ' XX 1 3   ',
              '   1 2 X0 ',
              '  1   X  X',
              '1  1     0',
              '      0   ',
              ' X        '),

             ('   3  1   ',
              ' 0        ',
              ' X  X X1  ',
              '          ',
              '2 X 0  1X ',
              ' X0  1 X X',
              '          ',
              '  1X 0  X ',
              '        0 ',
              '   0  1   '))

    for n, grid in enumerate(GRIDS, 1):
        assert checker(light_up, grid), f'You failed the test #{n}.'

    print('The local tests are done. Click on "Check" for more real tests.')

