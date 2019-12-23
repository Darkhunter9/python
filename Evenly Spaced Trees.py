from typing import List

def gcd(a,b):
    a,b = (a,b) if a >= b else (b,a)
    while b:
         a,b = b,a%b
    return a

def evenly_spaced_trees(trees: List[int]) -> int:
    distances = [trees[i+1]-trees[i] for i in range(len(trees)-1)]
    distance = min([gcd(i,j) for (i,j) in zip(distances,distances[1:])])

    start = trees[0]
    need = 0
    while trees[-1]-start:
        start += distance
        need += start not in trees

    return need


if __name__ == '__main__':
    print("Example:")
    print(evenly_spaced_trees([0, 2, 6]))
    assert evenly_spaced_trees([0, 2, 6]) == 1, 'add 1'
    assert evenly_spaced_trees([1, 3, 6]) == 3, 'add 3'
    assert evenly_spaced_trees([0, 2, 4]) == 0, 'no add'
    print("Coding complete? Click 'Check' to earn cool rewards!")

