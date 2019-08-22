from typing import Iterable

def can_balance(weights: Iterable) -> int:
    pos = len(weights)//2
    distance = [abs(i-pos) for i in range(len(weights))]
    record = set()

    while 0 <= pos < len(weights):
        left = sum([i[0]*i[1] for i in zip(weights[:pos],distance[:pos])])
        right = sum([i[0]*i[1] for i in zip(weights[pos+1:],distance[pos+1:])])
        if left == right:
            return pos
        elif left > right:
            pos -= 1
            record.add(-1)
        else:
            pos += 1
            record.add(1)
        if len(record) > 1:
            return -1
        distance = [abs(i-pos) for i in range(len(weights))]
    return -1


if __name__ == '__main__':
    print("Example:")
    print(can_balance([6, 1, 10, 5, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert can_balance([6, 1, 10, 5, 4]) == 2
    assert can_balance([10, 3, 3, 2, 1]) == 1
    assert can_balance([7, 3, 4, 2, 9, 7, 4]) == -1
    assert can_balance([42]) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
