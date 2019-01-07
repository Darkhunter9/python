from copy import deepcopy

def lanterns_flow(river_map, minutes):
    river_map = [list(i) for i in river_map]
    map2 = deepcopy(river_map)
    directions = {"S":[1,0], "N":[-1,0], "W":[0,-1], "E":[0,1]}
    walls = {"S":[0,-1], "N":[0,1], "W":[-1,0], "E":[1,0]} 
    traces = []

    while "." in river_map[0]:
        trace = [[0,river_map[0].index(".")]]
        direction = "S"
        river_map[trace[-1][0]][trace[-1][1]] = "X"
        
        while trace[-1][0] != len(river_map) - 1:
            trace.append([trace[-1][0]+directions[direction][0],trace[-1][1]+directions[direction][1]])
            if trace[-1][0] == len(river_map) -1:
                break
            river_map[trace[-1][0]][trace[-1][1]] = "X"
            if river_map[trace[-1][0]+directions[direction][0]][trace[-1][1]+directions[direction][1]] == ".":
                if (river_map[trace[-1][0]+directions[direction][0]+walls[direction][0]]
                [trace[-1][1]+directions[direction][1]+walls[direction][1]] != "X"):
                    if (river_map[trace[-1][0]+walls[direction][0]]
                [trace[-1][1]+walls[direction][1]] != "X"):
                        # change direction
                        if direction in "SN":
                            if (river_map[trace[-1][0]+directions["E"][0]+walls["E"][0]]
                            [trace[-1][1]+directions["E"][1]+walls["E"][1]] == "X"):
                                direction = "E"
                            else:
                                direction = "W"
                        else:
                            if (river_map[trace[-1][0]+directions["N"][0]+walls["N"][0]]
                            [trace[-1][1]+directions["N"][1]+walls["N"][1]] == "X"):
                                direction = "N"
                            else:
                                direction = "S"
            else: 
                # == "X", must change direction
                if direction in "SN":
                    if river_map[trace[-1][0]][trace[-1][1]-1] == "X":
                        direction = "E"
                    else:
                        direction = "W"
                else:
                    if river_map[trace[-1][0]+1][trace[-1][1]] == "X":
                        direction = "N"
                    else:
                        direction = "S"

        traces.append(trace)

    locations = [i[minutes] for i in traces]
    result = []
    for i in locations:
        for k in [-1,0,1]:
            for l in [-1,0,1]:
                if i[0]+k >= 0 and i[0]+k <= len(river_map)-1:
                    if map2[i[0]+k][i[1]+l] == "." and [i[0]+k,i[1]+l] not in result:
                        result.append([i[0]+k,i[1]+l])
    
    return len(result)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert lanterns_flow(("X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X......X",
                          "X......X",
                          "X......X",
                          "X......X",
                          "XXX....X"), 0) == 8, "Start"
    assert lanterns_flow(("X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X......X",
                          "X......X",
                          "X......X",
                          "X......X",
                          "XXX....X"), 7) == 18, "7th minute"
    assert lanterns_flow(("X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X......X",
                          "X......X",
                          "X......X",
                          "X......X",
                          "XXX....X"), 9) == 17, "9th minute"
