from typing import Iterable
from math import factorial

def reversed_permutation_index(length: int, index: int) -> Iterable[int]:
    result = []
    candidates = list(range(length))
    index -= 1

    for i in range(length-1):
        result.append(candidates[index//factorial(length-1-i)])
        index = index%factorial(length-1-i)
        candidates.remove(result[-1])
    
    result.append(candidates[-1])
    
    return tuple(result)


if __name__ == '__main__':
    assert tuple(reversed_permutation_index(3, 5)) == (2, 0, 1)
    assert tuple(reversed_permutation_index(9, 279780)) == (6, 8, 3, 4, 2, 1, 7, 5, 0)
    assert tuple(reversed_permutation_index(6, 271)) == (2, 1, 3, 0, 4, 5)
    assert tuple(reversed_permutation_index(12, 12843175)) == (0, 4, 7, 5, 8, 2, 10, 6, 3, 1, 9, 11)
    assert tuple(reversed_permutation_index(15, 787051783737)) == (9, 0, 6, 2, 5, 7, 12, 10, 3, 8, 11, 4, 13, 1, 14)
    assert tuple(reversed_permutation_index(18, 3208987196401056)) == (9, 0, 6, 17, 8, 12, 11, 1, 10, 14, 3, 15, 2, 13, 16, 7, 5, 4)
    assert tuple(reversed_permutation_index(21, 38160477453633042937)) == (15, 13, 14, 6, 10, 5, 19, 16, 11, 0, 9, 18, 2, 17, 4, 20, 12, 1, 3, 7, 8)
    assert tuple(reversed_permutation_index(24, 238515587608877815254677)) == (9, 5, 4, 12, 13, 17, 7, 0, 23, 16, 11, 8, 15, 21, 2, 3, 22, 1, 10, 19, 6, 20, 14, 18)
    assert tuple(reversed_permutation_index(27, 6707569694907742966546817183)) == (16, 17, 10, 23, 4, 22, 7, 18, 2, 21, 13, 6, 9, 8, 19, 3, 25, 12, 26, 24, 14, 1, 0, 20, 15, 5, 11)
