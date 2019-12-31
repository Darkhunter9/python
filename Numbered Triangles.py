from copy import deepcopy
from itertools import permutations

def checkio(chips):
    triangle = chips.pop(0)
    queue = []
    result = []

    for i in range(3):
        queue.append([[triangle[i:]+triangle[:i]],deepcopy(chips)])
    
    while queue:
        [triangles, rest] = queue.pop(0)

        if not rest:
            if triangles[-1][1] == triangles[0][0]:
                result.append(sum(i[2] for i in triangles))
            else: continue

        for (i,triangle) in enumerate(rest):
            for j in set(permutations(triangle)):
                next_triangle = list(j)
                if triangles[-1][1] == next_triangle[0]:
                    queue.append([triangles+[next_triangle], rest[:i]+rest[i+1:]])

    if result:
        return max(result)
    else:
        return 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # checkio([[9,9,9],[9,9,9],[9,9,9],[9,9,9],[9,9,9],[9,9,9]])
    assert checkio(
        [[1, 4, 20], [3, 1, 5], [50, 2, 3],
         [5, 2, 7], [7, 5, 20], [4, 7, 50]]) == 152, "First"
    assert checkio(
        [[1, 10, 2], [2, 20, 3], [3, 30, 4],
         [4, 40, 5], [5, 50, 6], [6, 60, 1]]) == 210, "Second"
    assert checkio(
        [[1, 2, 3], [2, 1, 3], [4, 5, 6],
         [6, 5, 4], [5, 1, 2], [6, 4, 3]]) == 21, "Third"
    assert checkio(
        [[5, 9, 5], [9, 6, 9], [6, 7, 6],
         [7, 8, 7], [8, 1, 8], [1, 2, 1]]) == 0, "Fourth"
