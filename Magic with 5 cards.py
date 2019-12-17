from itertools import count
from copy import deepcopy

RANKS = tuple('A 2 3 4 5 6 7 8 9 10 J Q K'.split())
SUITS = tuple('♣♦♥♠')


def bot(*cards, n=1):
    """Determine four cards the bot has to say to the magician."""
    # Obviously not always just the first four, put your code here instead.
    result = []

    list1 = [i[-1] for i in cards]
    for i in SUITS:
        if list1.count(i) >= 2:
            suit = i
    
    pile1 = []
    pile2 = []
    for i in cards:
        if suit in i and len(pile1) < 2:
            pile1.append(i)
        else:
            pile2.append(i)

    A = pile1[0]
    B = pile1[1]
    # A -> B
    d1 = (RANKS.index(B[:B.index(' ')])-RANKS.index(A[:A.index(' ')])+13)%13
    if d1 <= 6:
        hide = B
        show = A
    else:
        hide = A
        show = B
        d1 = 13-d1
    
    pile2.sort(key = lambda i: (RANKS.index(i[:i.index(' ')]),SUITS.index(i[-1])))
    if d1 in [5,6]:
        result.append(pile2.pop(0))
    elif d1 in [3,4]:
        result.append(pile2.pop(1))
    else:
        result.append(pile2.pop())
    
    if d1%2:
        result.append(pile2[0])
        result.append(pile2[1])
    else:
        result.append(pile2[1])
        result.append(pile2[0])
    
    result.insert((n-1)%4,show)

    return result


def magician(*cards, n=1):
    """Determine the fifth card with only four cards."""
    # Obviously not a random card, put your code here instead.
    show = cards[(n-1)%4]
    pile1 = [i for i in cards]
    pile1.pop((n-1)%4)

    pile2 = deepcopy(pile1)
    pile2.sort(key = lambda i: (RANKS.index(i[:i.index(' ')]),SUITS.index(i[-1])))
    
    d = (3 - pile2.index(pile1[0]))*2
    if pile2.index(pile1[1]) < pile2.index(pile1[2]):
        d -= 1
    
    return RANKS[(RANKS.index(show[:show.index(' ')])+d)%13] + show[-2:]

    # from random import choice
    # deck = [f'{r} {s}' for r in RANKS for s in SUITS]
    # for card in cards:
    #     deck.remove(card)
    # return choice(deck)


if __name__ == '__main__':
    bot('K ♦', 'K ♠', '2 ♣', '8 ♠', '10 ♠', n=3)
    assert list(bot('A ♥', '3 ♦', 'K ♠', 'Q ♣', 'J ♦')) == ['J ♦', 'A ♥', 'Q ♣', 'K ♠']
    assert magician('J ♦', 'A ♥', 'Q ♣', 'K ♠') == '3 ♦'

    assert list(bot('10 ♦', 'J ♣', 'Q ♠', 'K ♥', '7 ♦', n=2)) == ['Q ♠', '7 ♦', 'J ♣', 'K ♥']
    assert magician('Q ♠', '7 ♦', 'J ♣', 'K ♥', n=2) == '10 ♦'