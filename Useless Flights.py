from typing import List
from collections import defaultdict

def useless_flight(schedule: List) -> List:
    book = {}
    new = {}
    nodes = set()
    result = []
    for [d1,d2,cost] in schedule:
        if d1 not in book.keys():
            book[d1] = {}
        book[d1][d2] = cost
        if d2 not in book.keys():
            book[d2] = {}
        book[d2][d1] = cost
        nodes = nodes | {d1,d2}
    
    

    for j in nodes:
        unvisited = {node:None for node in nodes}
        visited = defaultdict(int)
        current = j
        currentdistance = 0
        unvisited[current] = currentdistance

        while True:
            for neighbour, distance in book[current].items():
                if neighbour not in unvisited: continue
                newdistance = currentdistance + distance
                if unvisited[neighbour] is None or unvisited[neighbour] > newdistance:
                    unvisited[neighbour] = newdistance
            visited[current] = currentdistance
            del unvisited[current]
            if not unvisited or all(i is None for i in unvisited.values()): break
            candidates = [node for node in unvisited.items() if node[1]]
            current, currentdistance = sorted(candidates, key=lambda x:x[1])[0]
        
        new[j] = visited
    
    for k in range(len(schedule)):
        [i,j,cost] = schedule[k]
        if j in new[i].keys() and cost > new[i][j]:
            result.append(k)
    
    return result


if __name__ == '__main__':
    print("Example:")
    print(useless_flight([['A', 'B', 50],
  ['B', 'C', 40],
  ['A', 'C', 100]]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert useless_flight([['A', 'B', 50],
  ['B', 'C', 40],
  ['A', 'C', 100]]) == [2]
    assert useless_flight([['A', 'B', 50],
  ['B', 'C', 40],
  ['A', 'C', 90]]) == []
    assert useless_flight([['A', 'B', 50],
  ['B', 'C', 40],
  ['A', 'C', 40]]) == []
    assert useless_flight([['A', 'C', 10],
  ['C', 'B', 10],
  ['C', 'E', 10],
  ['C', 'D', 10],
  ['B', 'E', 25],
  ['A', 'D', 20],
  ['D', 'F', 50],
  ['E', 'F', 90]]) == [4, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")