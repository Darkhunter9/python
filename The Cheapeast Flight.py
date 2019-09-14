from typing import List
from collections import defaultdict


def cheapest_flight(costs: List, a: str, b: str) -> int:
    book = {}
    nodes = set()
    for [d1,d2,cost] in costs:
        if d1 not in book.keys():
            book[d1] = {}
        book[d1][d2] = cost
        if d2 not in book.keys():
            book[d2] = {}
        book[d2][d1] = cost
        nodes = nodes | {d1,d2}

    unvisited = {node:None for node in nodes}
    visited = defaultdict(int)
    current = a
    currentdistance = 0
    unvisited[a] = currentdistance

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
    
    return visited[b]


if __name__ == '__main__':
    print("Example:")
    print(cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'A',
 'C'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'A',
 'C') == 70
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'C',
 'A') == 70
    assert cheapest_flight([['A', 'C', 40],
  ['A', 'B', 20],
  ['A', 'D', 20],
  ['B', 'C', 50],
  ['D', 'C', 70]],
 'D',
 'C') == 60
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['D', 'F', 900]],
 'A',
 'F') == 0
    assert cheapest_flight([['A', 'B', 10],
  ['A', 'C', 15],
  ['B', 'D', 15],
  ['C', 'D', 10]],
 'A',
 'D') == 25
    print("Coding complete? Click 'Check' to earn cool rewards!")