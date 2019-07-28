from collections import Counter

def cards(deck, hand):
    count = Counter(hand)

    if count[0] > 1 or count[deck] > 1:
        return False
    
    if any(count[i] >= 3 for i in count.keys()):
        return False
    
    if max(hand) > deck or min(hand) < 0:
        return False
    
    if all(i in hand for i in range(deck+1)):
        return False
    
    for i in count.keys():
        if count[i] == 2:
            j = i+1
            while j in hand and j <= deck:
                if count[j] >= 2 or j == deck:
                    return False
                j += 1
            j = i-1
            while j in hand and j >= 0:
                if count[j] >= 2 or j == 0:
                    return False
                j -= 1
    
    return True

if __name__ == '__main__':
    print("Example:")
    print(cards(5, [2, 0, 1, 2]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert cards(5, [2, 0, 1, 2]) == False
    assert cards(10, [9, 9, 6, 6]) == True
    assert cards(10, [11]) == False
    assert cards(3, [0, 1, 1]) == False
    assert cards(10, [3, 3, 5, 6, 6, 7]) == True
    assert cards(8, [4, 4, 5, 6, 7]) == True
    assert cards(7, [4, 4, 5, 6, 7]) == False
    assert cards(4, [0, 0]) == False
    assert cards(4, [2, 2]) == True
    assert cards(4, [4, 4]) == False
    assert cards(4, [2, 2, 2]) == False
    assert cards(4, [1, 1, 2, 2]) == False
    assert cards(4, [2, 2, 3, 3]) == False
    assert cards(4, [0, 1, 2, 3, 3]) == False
    assert cards(4, [1, 1, 2, 3, 4]) == False
    assert cards(4, [0, 1, 2, 3, 4]) == False
    assert cards(4, [1, 1, 2, 3, 3]) == False
    assert cards(10, [1, 1, 2, 3, 4, 5, 6, 7, 7]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
