from typing import Tuple, Iterable
from copy import deepcopy

def inertia(grid: Tuple[str], start: tuple) -> Iterable[str]:
    # some constants
    grid, (x, y) = list(map(list, grid)), start
    nb_rows, nb_cols = len(grid), len(grid[0])
    GEM, ROUGH, ICE, ROCK, MINE = '$. X*'
    MOVES = {'NW': (-1, -1), 'N': (-1, 0), 'NE': (-1, 1),
                'W': ( 0, -1),                'E': ( 0, 1),
                'SW': ( 1, -1), 'S': ( 1, 0), 'SE': ( 1, 1)}
    DIRECTIONS = dict(zip(MOVES.values(),MOVES.keys()))
    GEM_LIST = []
    for i in range(nb_rows):
        for j in range(nb_cols):
            if grid[i][j] == GEM:
                GEM_LIST.append((i,j))
    
    # calculate moving route and final stop
    # raise error if no move or end up in mine
    def move(start, direction):
        route = []
        (i,j) = start
        (di,dj) = MOVES[direction]
        stop = False

        while not stop:
            if not (0 <= i + di < nb_rows and 0 <= j + dj < nb_cols):
                stop = True
                break
            elif grid[i+di][j+dj] == ROCK:
                stop = True
                break
            elif grid[i+di][j+dj] == ROUGH:
                stop = True
                route.append((i+di,j+dj))
                break
            elif grid[i+di][j+dj] == MINE:
                raise ValueError
            else:
                route.append((i+di,j+dj))
                i += di
                j += dj

        if not route:
            raise ValueError
        else:
            return route, route[-1]

    # return route and directions found first to get a gem
    def find_route(start):
        queue = [[start,[start],[],[start]]]
        while queue:
            [current, route, directions, stops] = queue.pop(0)
            
            for i in POSSIBLE_MOVE[current[0]][current[1]].keys():
                stop = POSSIBLE_MOVE[current[0]][current[1]][i][1]
                # make sure the new stop is not dead point, and hasn't been arrived in this sub-route
                if POSSIBLE_MOVE[stop[0]][stop[1]] and stop not in stops:
                    # check for completion
                    if any(j in route+POSSIBLE_MOVE[current[0]][current[1]][i][0] for j in GEM_LIST):
                        return route[1:]+POSSIBLE_MOVE[current[0]][current[1]][i][0], directions+[i]
                    # make sure the new stop hasn't been arrived in other routes in the queue (very important trimming)
                    if not any(stop in j[3] for j in queue):
                        queue.append(deepcopy([stop,
                                                route+POSSIBLE_MOVE[current[0]][current[1]][i][0],
                                                directions+[i],
                                                stops+[stop]]))
        raise ValueError

    # calculate possible move of each grid
    POSSIBLE_MOVE = []
    for i in range(nb_rows):
        POSSIBLE_MOVE.append([])
        for j in range(nb_cols):
            POSSIBLE_MOVE[-1].append({})
            for k in ['NW','N','NE','W','E','SW','S','SE']:
                try:
                    route, stop = move((i,j),k)
                    POSSIBLE_MOVE[-1][-1][k] = deepcopy([route, stop])
                except:
                    pass
    # due to some point that can be reached are dead point (mines on all possible directions)
    # possible moves can be cleaned
    # probably should write a while loop....
    for i in range(nb_rows):
        for j in range(nb_cols):
            del_list = []
            for k in POSSIBLE_MOVE[i][j].keys():
                stop = POSSIBLE_MOVE[i][j][k][1]
                if not POSSIBLE_MOVE[stop[0]][stop[1]]:
                    del_list.append(k)
            if del_list:
                for k in del_list:
                    POSSIBLE_MOVE[i][j].pop(k)
    for i in range(nb_rows):
        for j in range(nb_cols):
            del_list = []
            for k in POSSIBLE_MOVE[i][j].keys():
                stop = POSSIBLE_MOVE[i][j][k][1]
                if not POSSIBLE_MOVE[stop[0]][stop[1]]:
                    del_list.append(k)
            if del_list:
                for k in del_list:
                    POSSIBLE_MOVE[i][j].pop(k)

    # search
    route = [start]
    directions = []
    l = len(GEM_LIST)
    while GEM_LIST:
        while True:
            try:
                temp_route, temp_directions = find_route(route[-1])
                break
            except:
                pass
        route += temp_route
        directions += temp_directions
        GEM_LIST = list(set(GEM_LIST) - (set(GEM_LIST)&set(route)))
    
    return directions

if __name__ == '__main__':
    def checker(function, grid, start):
        result = function(grid, start)
        GEM, ROUGH, ICE, ROCK, MINE = '$. X*'
        MOVES = {'NW': (-1, -1), 'N': (-1, 0), 'NE': (-1, 1),
                  'W': ( 0, -1),                'E': ( 0, 1),
                 'SW': ( 1, -1), 'S': ( 1, 0), 'SE': ( 1, 1)}
        grid, (x, y) = list(map(list, grid)), start
        nb_rows, nb_cols = len(grid), len(grid[0])
        for nb, move in enumerate(result, 1):
            try:
                dx, dy = MOVES[move]
            except KeyError:
                print(f"I don't understand your {nb}-th move: '{move}'.")
                return False
            while 0 <= x + dx < nb_rows and 0 <= y + dy < nb_cols and \
                  grid[x + dx][y + dy] != ROCK:
                x, y = x + dx, y + dy
                if grid[x][y] == ROUGH:
                    break
                elif grid[x][y] == GEM:
                    grid[x][y] = ICE
                elif grid[x][y] == MINE:
                    print(f"You are dead at {(x, y)}, bye!")
                    return False
        try:
            coord = next((i, j) for i, row in enumerate(grid)
                                for j, cell in enumerate(row) if cell == GEM)
        except StopIteration:
            print(f"Great, you did it in {nb} moves!")
            return True
        print(f"You have at least forgot one gem at {coord}.")
        return False

    GRIDS = (
            # ('', (14,25),["X$.*$$*$.*X$$ *   *$. $.$XXX .","$XX$ * .*.$X X...$$ .  *  X.* ",".*.X*X.$X.*. .$$.$.**$XX$.$XX*"," $X* X .X .*$  *.*$$$*. .. X.*","XX.X$* X.X.$$X$X**X.$.*X$* $X$",". $.*$ *$   $*.X . XX$ *X.X$$X","X* X .*X*.X . XX.X$.X .$*$.*..","$*  . *. X.$X$. .*X.$ .X...**$","$..$$.X*X *X*..*$X.**XX X$* $$","** $.$ *$X$*$**.$* $X$$*$... $","$.X.$.* .*X$.**$   *.*$.   ***","X**XX X$X .$*.. $X*$X*$X$*X * ","$X.X $..X X**$ .X $$   XX****$",".*X *X. XX* ..XX**X..X $.. *  ","$*..X.$*XX..* $.$$**X X$$. ...","$ *X* $$X*  *$... **X*    X$$*","$*   X$$X $$* X*X*  .*$   $$XX",".$..*$ $..XX*. .XXX ..X$*$.  $","X$$X.X**X$X**  *.$**X. XX$$ **","X  XXX.  *$ ** .* .*X  X*.X*$ "]),
            # ('', (8,2), 
            # ["**.*..*$XX*.X *.X.*X",
            # "*.$  ..*$.X .*$  X$ ",
            # "X*$*$* * .$$$ $ .$$X",
            # "*..**$X$.*..X*X  $$ ",
            # "$..*XX*XX*$X * $..  ",
            # ".$..$$X.*X$** *$X.X.",
            # "* .* $ **.X$X.$$*XXX",
            # ".X  .$X. X. X*XX*.**",
            # "*...X*X.$XX*$$**. * ",
            # "  *$$$   ***.**     ",
            # " $*.$X..$  **.*X*..X",
            # "X$X$ X X$ ..XX.$. $*",
            # " X. .*$$**.XX$ ***$ ",
            # "$$XX $ X$ .. $X  XXX",
            # ".. XX$X.X $X$ . $$.*",
            # " * $.X$ .$$*X. *$$XX"]),

            # ('',(9,13),
            #     ["*X $ .X  *.*$$.",
            #     "$$$X $X*XX $.$$",
            #     "*X$**X.*** .*X ",
            #     ".X. .XX$.*$.$$$",
            #     "$X $X*$* . *.$*",
            #     "$.$*.  ..  . X.",
            #     "..X..  X$** $X*",
            #     "X$$ *XX*.*.X.X ",
            #     "*  *  *$X.X$*X.",
            #     " *  * . *$.$*.$",
            #     " * X XXX.$X $..",
            #     "*XXX*..$$*.*$XX"]),

            ('5x5', (1, 1), ('*X$$.',
                              ' .$*.',
                              '... X',
                              ' *$* ',
                              'XXX*$')),

             ('7x6', (6, 1), ('**$.  ',
                              '$*$.. ',
                              'X.**.$',
                              '*XX$ .',
                              '.X  XX',
                              'X$* X$',
                              '$.*  .')),

             ('5x10', (3, 8), (' X**$X.$X*',
                               '*$ X$.X*$.',
                               '* *X$..$$X',
                               '*.  .* *. ',
                               'X.$.XX $ .'))
                               )

    for dim, start, grid in GRIDS:
        assert checker(inertia, grid, start), f'You failed with the grid {dim}.'

    print('The local tests are done. Click on "Check" for more real tests.')
