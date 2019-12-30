from copy import deepcopy
import random

def find_path(scanner, memory):
    DIR_reverse = {"N": 'S', "S": 'N', "W": 'E', "E": 'W'}
    DIR = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
    memory_binary = bin(memory)[2:]
    memory_binary = '0'*(100-len(memory_binary)) + memory_binary
    memory_list = [[j for j in memory_binary[i*10:(i+1)*10]] for i in range(10)]
    memory_list[0][0] = '1'
    path = []
    pool = []

    for (direction, distance) in scanner.items():
        if distance and memory_list[DIR[direction][0]][DIR[direction][1]] == '0':
            pool.append([direction,1])
    
    if pool:
        if len(pool) > 1:
            random.seed()
        [final_direction, final_distance] = random.choice(pool)
    else:
        final_direction = random.choice([i for i in scanner.keys() if scanner[i]])
        final_distance = 1
        if final_direction in 'WE':
            for i in range(1,10):
                memory_list[0][i] = '0'
        else:
            for i in range(1,10):
                memory_list[i][0] = '0'
        
    
    path += [final_direction]*final_distance
    for i in range(final_distance):
        for j, l in enumerate(memory_list):
            memory_list[j] = l[DIR[final_direction][1]%10:] + l[:DIR[final_direction][1]%10]
        memory_list = memory_list[DIR[final_direction][0]%10:] + memory_list[:DIR[final_direction][0]%10]
    memory_binary = ''.join(k for k in [''.join(j) for j in memory_list])
    return ''.join(path), int('0b'+memory_binary,2)

    # for debuging
    raise ValueError


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    DIR = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
    WALL = "X"
    EXIT = "E"
    EMPTY = "."
    MAX_STEP = 300

    def get_visible(maze, player):
        result = {}
        for direction, (dr, dc) in DIR.items():
            cr, cc = player
            distance = -1
            while maze[cr][cc] != WALL:
                cr += dr
                cc += dc
                distance += 1
            result[direction] = distance
        return result

    def checker(func, player, maze):
        step = 0
        memory = 0
        while True:
            result, memory = func(get_visible(maze, player), memory)
            if not isinstance(result, str) or any(ch not in DIR.keys() for ch in result):
                print("The function should return a string with directions.")
                return False
            if not isinstance(memory, int) or memory < 0 or memory >= 2 ** 100:
                print("The memory number should be an integer from 0 to 2**100.")
                return False
            for act in result:
                if step >= MAX_STEP:
                    print("You are tired and your scanner is off. Bye bye.")
                    return False
                r, c = player[0] + DIR[act][0], player[1] + DIR[act][1]
                if maze[r][c] == WALL:
                    print("BAM! You in the wall at {}, {}.".format(r, c))
                    return False
                elif maze[r][c] == EXIT:
                    print("GRATZ!")
                    return True
                else:
                    player = r, c
                    step += 1

    assert checker(find_path, (1, 1), [
        "XXXXXXXXXXXX",
        "X..........X",
        "X.XXXXXXXX.X",
        "X.X......X.X",
        "X.X......X.X",
        "X.X......X.X",
        "X.X......X.X",
        "X.X......X.X",
        "X.X......X.X",
        "X.XXXXXXXX.X",
        "X.........EX",
        "XXXXXXXXXXXX",
    ]), "Simple"
    assert checker(find_path, (1, 4), [
        "XXXXXXXXXXXX",
        "XX...X.....X",
        "X..X.X.X.X.X",
        "X.XX.X.X.X.X",
        "X..X.X.X.X.X",
        "XX.X.X.X.X.X",
        "X..X.X.X.X.X",
        "X.XX.X.X.X.X",
        "X..X.X.X.X.X",
        "XX.X.X.X.X.X",
        "XE.X.....X.X",
        "XXXXXXXXXXXX",
    ]), "Up Down"
    assert checker(find_path, (10, 10), [
        "XXXXXXXXXXXX",
        "X..........X",
        "X.XXXXXXXX.X",
        "X.X......X.X",
        "X.X.XX.X.X.X",
        "X.X......X.X",
        "X.X......X.X",
        "X.X..E...X.X",
        "X.X......X.X",
        "X.XXXX.XXX.X",
        "X..........X",
        "XXXXXXXXXXXX",
    ]), "Left"
