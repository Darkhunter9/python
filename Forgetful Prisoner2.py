def find_path(scanner, memory):
    neighbors = {"S": 1, "N": -1, "E": 1j, "W": -1j}
    bin2dir = {'00': 'S', '01': 'N', '10': 'E', '11': 'W'}
    memory, dir2bin = format(memory, '0100b'), dict(map(reversed, bin2dir.items()))
    path = [bin2dir[memory[6:][2*x:2*x+2]] for x in range(47)] 
    length, visited, pos = int(memory[:6], 2), dict(), 0  
    for d in path[:length]:
        pos -= neighbors[d]
        visited[pos] = visited.get(pos, 0)+1
    move = [(k, visited.get(neighbors[k], 0)) for k, v in scanner.items() if v > 0]
    direct, _ = sorted(move, key=lambda x: x[1])[0]
    length = length+1 if length < 47 else 47
    memory = ''.join([format(length, '06b')]+[dir2bin[x] for x in [direct]+path[:46]])
    return direct, int(memory, 2)

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