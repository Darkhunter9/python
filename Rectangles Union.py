from typing import List, Tuple
import numpy as np

def rectangles_union(recs: List[Tuple[int]]) -> int:
    if not recs:
        return 0
        
    recs_array = np.array(recs)
    border1 = (np.min(recs_array[:,0]), np.min(recs_array[:,1]))
    border2 = (np.max(recs_array[:,2]), np.max(recs_array[:,3]))
    grid = np.mgrid[border1[0]:border2[0]+1, border1[1]:border2[1]+1]

    count = 0
    for (i,j) in zip(list(grid[0].flatten()), list(grid[1].flatten())):
        for k in range(len(recs)):
            if i >= recs_array[(k,0)] and i < recs_array[(k,2)] and j >= recs_array[(k,1)] and j < recs_array[(k,3)]:
                count += 1
                break

    return count

if __name__ == '__main__':
    print("Example:")
    print(rectangles_union([
        (6, 3, 8, 10),
        (4, 8, 11, 10),
        (16, 8, 19, 11)
    ]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert rectangles_union([
        (6, 3, 8, 10),
        (4, 8, 11, 10),
        (16, 8, 19, 11)
    ]) == 33
    assert rectangles_union([
        (16, 8, 19, 11)
    ]) == 9
    assert rectangles_union([
        (16, 8, 19, 11),
        (16, 8, 19, 11)
    ]) == 9
    assert rectangles_union([
        (16, 8, 16, 8)
    ]) == 0
    assert rectangles_union([
        
    ]) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
