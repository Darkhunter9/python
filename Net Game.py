from copy import deepcopy
import numpy as np

def checkio(grid):
    nb_rows, nb_cols = len(grid), len(grid[0])
    visited = {(i, j): False for i in range(nb_rows)
                            for j in range(nb_cols)}
    queue = []

    MOVES = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
    DIRECTIONS = {(-1, 0):'N', (1, 0):'S', (0, -1):'W', (0, 1):'E'}
    OPPOSITE = {'N': 'S', 'S': 'N', 'W': 'E', 'E': 'W'}

    types = {'.' : ('N', 'W', 'S', 'E'),
                     '--': ('NS', 'EW'),
                     '_|': ('NW', 'SW', 'EN', 'ES'),
                     'T' : ('ENW', 'ENS', 'ESW', 'NSW')}
    types_2 = {dirs: tile_type for tile_type, sorted_dirs in types.items()
                                for dirs in sorted_dirs}
    tile_type = lambda tile: types_2.get(''.join(sorted(tile)), None)

    corner = {(0,0):'ES', (0,nb_cols-1):'SW', (nb_rows-1,0):'EN',(nb_rows-1,nb_cols-1):'NW'}
    for (i,j) in [(0,0),(0,nb_cols-1),(nb_rows-1,0),(nb_rows-1,nb_cols-1)]:
        if tile_type(grid[i][j]) == '_|':
            visited[(i,j)] = True
            grid[i][j] = corner[(i,j)]
    
    def obvious(visited,grid):
        n = 0
        temp_visited = deepcopy(visited)
        temp_grid = deepcopy(grid)
        while list(temp_visited.values()).count(False) != n:
            n = list(temp_visited.values()).count(False)
            potential = []
            # collect neighbours of determined tiles as potential
            for (i,j) in temp_visited.keys():
                if temp_visited[(i,j)]:
                    for (di,dj) in [(-1,0),(1,0),(0,-1),(0,1)]:
                        if 0 <= i+di < nb_rows and 0 <= j+dj < nb_cols and not temp_visited[(i+di,j+dj)]:
                            potential.append((i+di,j+dj))
            for i in range(nb_cols):
                if not temp_visited[(0,i)]: potential.append((0,i))
                if not temp_visited[(nb_rows-1,i)]: potential.append((nb_rows-1,i))
            for i in range(1,nb_rows-1):
                if not temp_visited[(i,0)]: potential.append((i,0))
                if not temp_visited[(i,nb_cols-1)]: potential.append((i,nb_cols-1))
            for i in range(1,nb_rows-1):
                for j in range(1,nb_cols-1):
                    if not temp_visited[(i,j)] and tile_type(temp_grid[i][j]) == '.':
                        potential.append((i,j))
            potential = set(potential)
            # for each potential
            for (i,j) in potential:
                neighbours = []
                must = []
                mustnot = []
                # exclude outward direction
                if i == 0:
                    mustnot.append('N')
                elif i == nb_rows-1:
                    mustnot.append('S')
                if j == 0:
                    mustnot.append('W')
                elif j == nb_cols-1:
                    mustnot.append('E')
                # collect neighboured determined tiles of potential
                for (di,dj) in [(-1,0),(1,0),(0,-1),(0,1)]:
                    if 0 <= i+di < nb_rows and 0 <= j+dj < nb_cols and temp_visited[(i+di,j+dj)]:
                        neighbours.append((i+di,j+dj))
                # hints given by neighboured determined tiles
                for (k,l) in neighbours:
                    for nwse in temp_grid[k][l]:
                        dk, dl = MOVES[nwse]
                        if k+dk == i and l+dl == j:
                            must.append(OPPOSITE[nwse])
                            break
                    else:
                        mustnot.append(DIRECTIONS[(k-i,l-j)])

                if tile_type(temp_grid[i][j]) == '.':
                    for k in MOVES.keys():
                        (di,dj) = MOVES[k]
                        if 0 <= i+di < nb_rows and 0 <= j+dj < nb_cols and tile_type(temp_grid[i+di][j+dj]) == '.':
                            mustnot.append(k)


                # judge
                must = set(must)
                mustnot = set(mustnot)
                if len(must)+len(mustnot) > 4 or len(must) > len(temp_grid[i][j]) or len(mustnot) > 4-len(temp_grid[i][j]):
                    raise ValueError
                if tile_type(temp_grid[i][j]) == '--':
                    if len(must) == 2 and tile_type(''.join(sorted(list(must)))) == '_|':
                        raise ValueError
                    if len(mustnot) == 2 and tile_type(''.join(sorted(list(mustnot)))) == '_|':
                        raise ValueError
                if tile_type(temp_grid[i][j]) == '_|':
                    if len(must) == 2 and tile_type(''.join(sorted(list(must)))) == '--':
                        raise ValueError
                    if len(mustnot) == 2 and tile_type(''.join(sorted(list(mustnot)))) == '--':
                        raise ValueError

                if len(must) == len(temp_grid[i][j]):
                    temp_grid[i][j] = ''.join(sorted(list(must)))
                    temp_visited[(i,j)] = True
                elif 4-len(mustnot) == len(temp_grid[i][j]):
                    temp_grid[i][j] = ''.join(sorted(list({'E','W','N','S'}-mustnot)))
                    temp_visited[(i,j)] = True
                elif tile_type(temp_grid[i][j]) == '--' and (must or mustnot):
                    if 'N' in must or 'S' in must or 'W' in mustnot or 'E' in mustnot:
                        temp_grid[i][j] = 'NS'
                    else:
                        temp_grid[i][j] = 'EW'
                    temp_visited[(i,j)] = True
                elif tile_type(temp_grid[i][j]) == '_|' and len(must) == len(mustnot) == 1:
                    if list(must)[0] != OPPOSITE[list(mustnot)[0]]:
                        temp_grid[i][j] = ''.join(sorted([list(must)[0],OPPOSITE[list(mustnot)[0]]]))
                        temp_visited[(i,j)] = True
        
        return [temp_visited, temp_grid]

    def cycle_existence(new, old = None):
        """ Recursively search if there is a closed loop / cycle. """
        check_visited[old] = True
        i, j = new
        for nwse in temp_grid2[i][j]:
            di, dj = MOVES[nwse]
            x, y = neighbor = i + di, j + dj
            if not (0 <= x < nb_rows and 0 <= y < nb_cols):
                raise ValueError
            if OPPOSITE[nwse] not in temp_grid2[x][y]:
                raise ValueError
            if check_visited[neighbor]:
                if neighbor != old:
                    return True # closed loop / cycle found.
            elif cycle_existence(neighbor, new): # Visit the neighbor.
                return True
        check_visited[new] = True

    [visited, grid] = obvious(visited, grid)
    
    if False not in visited.values():
        return grid
    
    queue.append([visited,grid])
    while queue:
        temp_visited, temp_grid = queue.pop(0)
        try:
            [temp_visited2, temp_grid2] = obvious(temp_visited, temp_grid)
            if False not in temp_visited2.values():
                check_visited = {(i, j): False for i in range(nb_rows)
                                     for j in range(nb_cols)}
                try:
                    if cycle_existence((0,0)):
                        continue
                except:
                    continue
                if all(check_visited.values()):
                    return temp_grid2
                else:
                    continue
        except:
            continue

        for [i,j] in list(np.mgrid[0:nb_rows,0:nb_cols].T.reshape((-1,2))):

            if not temp_visited2[(i,j)]:
                temp_visited3 = deepcopy(temp_visited2)
                temp_visited3[(i,j)] = True

                neighbours = []
                must = []
                mustnot = []
                # exclude outward direction
                if i == 0:
                    mustnot.append('N')
                elif i == nb_rows-1:
                    mustnot.append('S')
                if j == 0:
                    mustnot.append('W')
                elif j == nb_cols-1:
                    mustnot.append('E')
                # collect neighboured determined tiles of potential
                for (di,dj) in [(-1,0),(1,0),(0,-1),(0,1)]:
                    if 0 <= i+di < nb_rows and 0 <= j+dj < nb_cols and temp_visited[(i+di,j+dj)]:
                        neighbours.append((i+di,j+dj))
                # hints given by neighboured determined tiles
                for (k,l) in neighbours:
                    for nwse in temp_grid[k][l]:
                        dk, dl = MOVES[nwse]
                        if k+dk == i and l+dl == j:
                            must.append(OPPOSITE[nwse])
                            break
                    else:
                        mustnot.append(DIRECTIONS[(k-i,l-j)])
                
                # judge
                must = set(must)
                mustnot = set(mustnot)


                for k in types[tile_type(grid[i][j])]:
                    if not any(l in mustnot for l in k) and all(l in k for l in must):
                        temp_grid3 = deepcopy(temp_grid2)
                        temp_grid3[i][j] = k
                        queue.append([deepcopy(temp_visited3), temp_grid3])
                
                break
    
    return grid


if __name__ == '__main__':
    def checker(function, input_grid):
        input_copy = [row[:] for row in input_grid]
        result = function(input_copy)
        # Check the result...
        class Error(Exception): pass
        try:
            # 1) Check all types.
            if not (isinstance(result, (tuple, list)) and \
                    all(isinstance(row, (tuple, list)) for row in result) and \
                    all(isinstance(s, str) for row in result for s in row)):
                raise Error("The result must be a list/tuple "
                            "of lists/tuples of strings.")
            # 2) Check all sizes.
            nb_rows, nb_cols = len(input_grid), len(input_grid[0])
            if not (len(result) == nb_rows and \
                    all(len(row) == nb_cols for row in result)):
                raise Error("The result must have the same size as input data.")
            # 3) Check all tile types.
            types = {'.' : ('N', 'W', 'S', 'E'),
                     '--': ('NS', 'EW'),
                     '_|': ('NW', 'SW', 'EN', 'ES'),
                     'T' : ('ENW', 'ENS', 'ESW', 'NSW')}
            types = {dirs: tile_type for tile_type, sorted_dirs in types.items()
                                     for dirs in sorted_dirs}
            tile_type = lambda tile: types.get(''.join(sorted(tile)), None)
            for i in range(nb_rows):
                for j in range(nb_cols):
                    if tile_type(result[i][j]) != tile_type(input_grid[i][j]):
                        raise Error("You can only rotate the tiles, not change"
                                    f" them like you did at {(i, j)}.")
            # 4) Check if there is no closed loop / cycle.
            MOVES = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
            OPPOSITE = {'N': 'S', 'S': 'N', 'W': 'E', 'E': 'W'}
            visited = {(i, j): False for i in range(nb_rows)
                                     for j in range(nb_cols)}
            def cycle_existence(new, old = None):
                """ Recursively search if there is a closed loop / cycle. """
                visited[old] = True
                i, j = new
                for nwse in result[i][j]:
                    di, dj = MOVES[nwse]
                    x, y = neighbor = i + di, j + dj
                    if not (0 <= x < nb_rows and 0 <= y < nb_cols):
                        raise Error(f"Tile {new} should not point outward.")
                    if OPPOSITE[nwse] not in result[x][y]:
                        raise Error(f"The tile {new} point to {neighbor}: "
                                    "it should be reciprocal.")
                    if visited[neighbor]:
                        if neighbor != old:
                            return True # closed loop / cycle found.
                    elif cycle_existence(neighbor, new): # Visit the neighbor.
                        return True
                visited[new] = True
            start = 0, 0
            if cycle_existence(start):
                raise Error("There must be no closed loop.")
            # 5) We should have visited all cells if it's entirely connected.
            if not all(visited.values()):
                miss = sum(not v for v in visited.values())
                raise Error(f"The result must be entirely connected. {miss} "
                            f"tiles are not connected to the tile at {start}.")
        except Error as error:
            print(error.args[0]) # error message
            return False
        return True

    GRIDS = (
        ('', [["S","NW","E","S","SE"],
        ["NS","WE","WS","N","NS"],
        ["WS","WSE","WSE","NSE","WS"],
        ["S","NSE","WSE","NW","W"],
        ["S","W","SE","SE","NS"],
        ["SE","WSE","NE","NS","WE"],
        ["W","WSE","S","NWE","SE"],
        ["E","NE","NWE","NSE","S"],
        ["NW","NSE","NWE","NW","N"],
        ["WS","NWE","WS","WSE","N"],
        ["E","NSE","WS","NE","NSE"],
        ["WS","WSE","W","W","WSE"],
        ["E","NSE","NE","E","NWS"],
        ["WS","WSE","N","N","NW"],
        ["E","WS","WE","NS","N"]]),

        # ('', [["E","S","W","NWE","E","NE","SE","S","W","WS","N"],
        # ["NS","WE","E","NS","E","NWE","NW","SE","NS","WSE","NW"],
        # ["NWE","NSE","WSE","NSE","NE","NS","E","NWE","NWS","SE","N"],
        # ["WSE","E","W","WSE","WSE","NSE","SE","NW","W","N","S"],
        # ["WSE","SE","S","SE","S","NWE","WSE","NSE","NWS","NSE","NSE"],
        # ["E","W","N","NSE","SE","WSE","W","WSE","NSE","NW","NS"],
        # ["S","NE","NE","NWE","NS","WSE","SE","S","E","S","WE"],
        # ["N","SE","WS","W","NWS","NWS","NSE","NE","S","E","NWS"],
        # ["NWE","NSE","WSE","NS","NWE","NS","WS","NWE","NWE","S","WE"],
        # ["NS","W","WE","S","NWS","WE","N","NE","NWS","N","WSE"],
        # ["WS","E","SE","W","E","S","E","WE","NSE","N","N"]]),

       ('8x4',[["SE","SE","W","NW","WSE","N","N","W"],
        ["S","NSE","NSE","N","WSE","NSE","NWS","WE"],
        ["N","WS","WSE","WSE","NE","NS","SE","WS"],
        ["N","NS","NE","N","W","NWS","NS","S"]]),
            
            ('3x3', [['NW' , 'S'  , 'W' ],
                      ['WSE', 'NWE', 'SE'],
                      ['N'  , 'NW' , 'E' ]]),

             ('6x3', [['W' , 'NW' , 'E'  ],
                      ['NS', 'WE' , 'S'  ],
                      ['WE', 'SE' , 'NWE'],
                      ['NE', 'NSE', 'SE' ],
                      ['WS', 'NSE', 'WS' ],
                      ['SE', 'W'  , 'E'  ]]),

             ('5x5', [['NW' , 'S'  , 'N'  , 'E'  , 'SE'],
                      ['NS' , 'W'  , 'NWE', 'NWE', 'SE'],
                      ['WSE', 'NSE', 'NWE', 'W'  , 'E' ],
                      ['WE' , 'WS' , 'WSE', 'SE' , 'WE'],
                      ['W'  , 'NE' , 'N'  , 'NW' , 'WS']]))

    for dim, grid in GRIDS:
        assert checker(checkio, grid), f'You failed with the grid {dim}.'

    print('The local tests are done. Click on "Check" for more real tests.')
