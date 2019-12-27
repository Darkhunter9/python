from typing import List
from math import floor

def fast_train(sections: List[List[int]]) -> int:
    queue = [[1]]
    distance = sum([i[0] for i in sections])
    sl = []

    for i in sections:
        sl += [i[1]]*i[0]

    def check(v):
        speed = []
        for i in v:
            speed += [i]*i
        if any(speed[i] > sl[i] for i in range(len(speed))):
            return False
        return True

    while queue:
        current = queue.pop(0)
        for i in [-1,0,1]:
            if current[-1]+i >= 1 and sum(current+[current[-1]+i]) <= distance and check(current+[current[-1]+i]):
                if sum(current+[current[-1]+i]) == distance:
                    if current[-1]+i == 1:
                        return len(current)+1
                else:
                    queue.append(current+[current[-1]+i])

if __name__ == '__main__':
    print("Example:")
    print(fast_train([(4, 3)]))

    assert fast_train([(4, 3)]) == 3
    assert fast_train([(9, 10)]) == 5
    assert fast_train([(5, 5), (4, 2)]) == 6
    print("Coding complete? Click 'Check' to earn cool rewards!")

