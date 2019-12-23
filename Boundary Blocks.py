from typing import List, Tuple, Iterable
import numpy as np


def boundary_blocks(grid: List[str]) -> Iterable[Tuple[int]]:
    a = len(grid)
    b = len(grid[0])
    g = np.zeros([a,b])
    seen = []
    unseen = []
    queue = []
    block = []
    result = []

    def search(i,j):
        l = []

        for (di,dj) in [(-1,0),(1,0),(0,-1),(0,1)]:
            if i+di >= 0 and i+di < a and j+dj >= 0 and j+dj < b:
                if g[(i+di,j+dj)] == 0 and (i+di,j+dj) in unseen:
                    l.append((i+di,j+dj))

        return l

    for i in range(a):
        for j in range(b):
            if grid[i][j] == 'X':
                g[(i,j)] = -1
                block.append((i,j))
            else:
                unseen.append((i,j))
    
    while unseen:
        if not queue:
            queue.append(unseen.pop(0))
            seen.append(queue[-1])
            g[queue[-1]] = np.max(g) + 1
        else:
            (i,j) = queue.pop(0)
            l = search(i,j)
            for (k,l) in l:
                g[(k,l)] = g[(i,j)]
                queue.append((k,l))
                unseen.remove((k,l))
                seen.append((k,l))
    
    for (i,j) in block:
        temp = set()
        temp = {g[(i+di,j+dj)] for (di,dj) in [(-1,0),(1,0),(0,-1),(0,1)] 
                if i+di >= 0 and i+di < a and j+dj >= 0 and j+dj < b and g[(i+di,j+dj)] > 0}
        if len(temp) > 1:
            result.append((i,j))

    return set(result)


if __name__ == '__main__':
    assert set(boundary_blocks(['..X',
                                '.X.',
                                'X..'])) == {(0, 2), (1, 1), (2, 0)}, '#1 3x3'
    assert set(boundary_blocks(['...',
                                '.X.',
                                'X..'])) == set(), '#2 3x3'
    assert set(boundary_blocks(['X.X.',
                                '.X..',
                                '..X.',
                                '....'])) == {(0, 0), (0, 2), (1, 1)}, '#3 4x4'

    print('The local tests are done. Click on "Check" for more real tests.')