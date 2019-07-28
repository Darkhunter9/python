def stones(pile, moves):
    move = set(moves)
    results = [True] + [False] * pile
    for i in range(1,pile+1):
        possible = [x for x in move if i - x >= 0]
        results[i] = any((not results[i - j]) for j in possible)
    
    if results[-1]:
        return 1
    else:
        return 2

if __name__ == '__main__':
    print("Example:")
    print(stones(99, [1,2,7, 3, 4]))
    print(stones(17, [1, 3, 4]))
    print(stones(100, [1]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert stones(17, [1, 3, 4]) == 2
    assert stones(17, [1, 3, 4, 6, 9]) == 1
    assert stones(99, [1]) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
