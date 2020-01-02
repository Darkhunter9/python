import random
import numpy as np
from collections import defaultdict

# def expected(dice_number, sides, target, board):
#     def experiment():
#         current = 0
#         n = 0
#         while current != target:
#             current += round(sum([random.uniform(1,sides) for i in range(dice_number)]))
#             current = current % len(board)
#             while board[current]:
#                 current += board[current]
#             n += 1
#         return n

#     result = []
#     for i in range(100000):
#         result.append(experiment())
#     result = sum(result)/len(result)
#     return result

def expected(dice_number, sides, target, board):
    first_distribution = {}
    for i in range(len(board)):
        first_distribution[i] = 0.
    first_distribution[0] = 1.
    distribution = [first_distribution]

    dices = np.zeros((sides,)*dice_number, dtype=int)
    it = np.nditer(dices, flags=['multi_index'])
    while not it.finished:
        dices[it.multi_index] = np.sum(it.multi_index) + dice_number
        it.iternext()
    
    unique, counts = np.unique(dices.flatten(), return_counts=True)
    advances = dict(zip(unique, counts))
    total = sum(advances.values())
    for i in advances.keys():
        advances[i] /= total
    


    def expand():
        last_distribution = distribution[-1]
        next_distribution = {}
        for i in range(len(board)):
            next_distribution[i] = 0.

        for i in last_distribution.keys():
            if i != target or len(distribution) == 1:
                for j in advances.keys():
                    stop = (i+j) % len(board)
                    while board[stop]:
                        stop += board[stop]
                        stop = stop % len(board)
                    # next_distribution[stop] += last_distribution[i]*advances[j]/(sum(last_distribution.values())-last_distribution[target])
                    next_distribution[stop] += last_distribution[i]*advances[j]
        
        distribution.append(next_distribution)
    
    for i in range(1000):
        expand()

    expected = 0.
    for i in range(len(distribution)):
        expected += i*distribution[i][target]

    return expected
        



if __name__ == '__main__':
    #These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert(almost_equal(expected(1, 4, 3, [0, 0, 0, 0]), 4.0))
    assert(almost_equal(expected(1, 4, 1, [0, 0, 0, 0]), 4.0))
    assert(almost_equal(expected(1, 4, 3, [0, 2, 1, 0]), 1.3))
    assert(almost_equal(expected(1, 4, 3, [0, -1, -2, 0]), 4.0))
    assert(almost_equal(expected(1, 6, 1, [0] * 10), 8.6))
    assert(almost_equal(expected(2, 6, 1, [0] * 10), 10.2))
