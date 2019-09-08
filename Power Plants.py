from typing import Set, Tuple, List, Dict
from collections import Counter

def power_plants(network: Set[Tuple[str, str]], ranges: List[int]) -> Dict[str, int]:
    network = set([tuple(i) for i in network])
    plants = [i for sublist in network for i in sublist]
    count = min(Counter(plants).values())
    edges = [i for i in plants if plants.count(i) == count]
    edges = list(set(edges))
    plants = list(set(plants))
    result = {}
    lit = set()
    distances = {}
    
    for i in plants:
        distances[i] = {}
        for j in plants:
            if i != j:
                if (i,j) in network or (j,i) in network:
                    distances[i][j] = 1
                else:
                    distances[i][j] = None
            else:
                distances[i][j] = 0
    
    for i in plants:
        visited = {}
        current = i
        currentDistance = 0
        unvisited = {node: None for node in plants}
        unvisited[current] = currentDistance
        while True:
            for neighbour, distance in distances[current].items():
                if neighbour not in unvisited or not distance: continue
                newDistance = currentDistance + distance
                if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                    unvisited[neighbour] = newDistance
            visited[current] = currentDistance
            del unvisited[current]
            if not unvisited: 
                distances[i] = visited
                break
            candidates = [node for node in unvisited.items() if node[1]]
            current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
    
    # strategy 1: cover more plants at edges
    ranges = sorted(ranges, reverse=True)
    for i in ranges:
        waitlist = {}
        for j in plants:
            # if j in lit: continue
            light = [k for k in distances[j].keys() if distances[j][k] <= i and k not in lit]
            edge = [k for k in light if k in edges]
            waitlist[j] = [len(light), len(edge), light]
        final = sorted([k for k in waitlist.items()], key=lambda x: (x[1][1],x[1][0]), reverse=True)[0]
        result[final[0]] = i
        lit = lit | set(final[1][2])
        if len(lit) == len(plants):
            return result
    
    # strategy 2: cover more plants
    lit = set()
    result = {}
    for i in ranges:
        waitlist = {}
        for j in plants:
            # if j in lit: continue
            light = [k for k in distances[j].keys() if distances[j][k] <= i and k not in lit]
            edge = [k for k in light if k in edges]
            waitlist[j] = [len(light), len(edge), light]
        final = sorted([k for k in waitlist.items()], key=lambda x: x[1][1]+x[1][0], reverse=True)[0]
        result[final[0]] = i
        lit = lit | set(final[1][2])
        if len(lit) == len(plants):
            return result


if __name__ == '__main__':
    power_plants([["A","B"],["B","C"],["C","D"],["D","E"],["F","G"],["G","H"],["H","I"],["I","J"],["K","L"],["L","M"],["M","N"],["N","O"],["P","Q"],["Q","R"],["R","S"],["S","T"],["U","V"],["V","W"],["W","X"],["X","Y"],["A","F"],["B","G"],["C","H"],["D","I"],["E","J"],["F","K"],["G","L"],["H","M"],["I","N"],["J","O"],["K","P"],["L","Q"],["M","R"],["N","S"],["O","T"],["P","U"],["Q","V"],["R","W"],["S","X"],["T","Y"]],[3,3])
    power_plants([["A","B"],["B","C"],["C","D"],["D","E"]],[2,1])
    assert power_plants({('A', 'B'), ('B', 'C')}, [1]) == {'B': 1}
    assert power_plants({('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')}, [2]) == {'C': 2}
    assert power_plants({('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F')}, [1, 1]) == {'B': 1, 'E': 1}
    assert power_plants({('A', 'B'), ('B', 'C'), ('A', 'D'), ('B', 'E')}, [1, 0]) == {'B': 1, 'D': 0}

    print('The local tests are done. Click on "Check" for more real tests.')
