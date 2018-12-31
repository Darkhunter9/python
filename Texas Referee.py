from itertools import combinations

RANKS = "23456789TJQKA"
SUITS = "scdh"

def transfer(text):
    result = []
    if text[0] in "23456789":
        result.append(int(text[0]))
    else:
        result.append(list("TJQKA").index(text[0])+10)
        # A -> 14
    result.append(SUITS.index(text[1]))
    return result

def detransfer(card):
    result = ""
    if card[0] in [2,3,4,5,6,7,8,9]:
        result = str(card[0])
    else:
        result = "TJQKA"[card[0]-10]
    result += SUITS[card[1]]
    return result

def sortcard(cardlist):
    result = []
    result = sorted(cardlist, key = lambda x: (x[0], x[1]), reverse = True)
    return result

# straight flush
def first(cardlist):
    suit = cardlist[0][1]
    if all(i[1] == suit for i in cardlist):
        if all(cardlist[i][0] == cardlist[i+1][0]+1 for i in range(4)):
            return list(cardlist)
    return None

# four of a kind
def second(cardlist):
    if cardlist[0][0] == cardlist[1][0] == cardlist[2][0] == cardlist[3][0]:
        return cardlist
    elif cardlist[4][0] == cardlist[1][0] == cardlist[2][0] == cardlist[3][0]:
        return list(cardlist[1:])+cardlist[0]
    return None

# full house
def third(cardlist):
    if cardlist[0][0] == cardlist[1][0] == cardlist[2][0] and cardlist[3][0] == cardlist[4][0]:
        return list(cardlist)
    elif cardlist[0][0] == cardlist[1][0] and cardlist[2][0] == cardlist[3][0] == cardlist[4][0]:
        return list(cardlist[2:])+list(cardlist[:2])
    return None

# flush
def fourth(cardlist):
    suit = cardlist[0][1]
    if all(i[1] == suit for i in cardlist):
        return list(cardlist)
    return None

# straight
def fifth(cardlist):
    if all(cardlist[i][0] == cardlist[i+1][0]+1 for i in range(4)):
            return list(cardlist)
    return None

# three of a kind
def sixth(cardlist):
    for i in combinations(cardlist,3):
        result = []
        if all(i[j][0] == i[j+1][0] for j in range(2)):
            result = list(i)
            for j in cardlist:
                if j not in i:
                    result.append(j)
            return result
    return None

# two pair
def seventh(cardlist):
    for i in combinations(cardlist,4):
        result =[]
        if i[0][0] == i[1][0] and i[2][0] == i[3][0]:
            result = list(i)
            for j in cardlist:
                if j not in i:
                    result.append(j)
            return result
    return None

# one pair
def eighth(cardlist):
    for i in combinations(cardlist,2):
        result = []
        if i[0][0] == i[1][0]:
            result = list(i)
            for j in cardlist:
                if j not in i:
                    result.append(j)
            return result
    return None

# high card
def ninth(cardlist):
    return list(cardlist)

def texas_referee(cards_str):
    cardlist = []
    for i in range(7):
        cardlist.append(transfer(cards_str[3*i:3*i+2]))
    cardlist = sortcard(cardlist)

    operation = [first,second,third,fourth,fifth,sixth,seventh,eighth,ninth]
    current = 8
    possible = []

    for i in combinations(cardlist,5):
        for j in range(len(operation)):
            if operation[j](i) and j <= current:
                if j != current:
                    possible.clear()
                possible.append(operation[j](i))
                current = j
                break
    
    possible.sort(key= lambda x: (x[0][0],x[1][0],x[2][0],x[3][0],x[4][0],x[0][1],x[1][1],x[2][1],x[3][1],x[4][1]), reverse = True)
    # possible.sort(key= lambda x: (x[i][j] for i in range(5) for j in range(2)), reverse = True)
    result = ""
    for i in sortcard(possible[0]):
        result += detransfer(i)
        result += ","

    return result[:-1]
 

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert texas_referee("Kh,Qh,Ah,9s,2c,Th,Jh") == "Ah,Kh,Qh,Jh,Th", "High Straight Flush"
    assert texas_referee("Qd,Ad,9d,8d,Td,Jd,7d") == "Qd,Jd,Td,9d,8d", "Straight Flush"
    assert texas_referee("5c,7h,7d,9s,9c,8h,6d") == "9c,8h,7h,6d,5c", "Straight"
    assert texas_referee("Ts,2h,2d,3s,Td,3c,Th") == "Th,Td,Ts,3c,3s", "Full House"
    assert texas_referee("Jh,Js,9h,Jd,Th,8h,Td") == "Jh,Jd,Js,Th,Td", "Full House vs Flush"
    assert texas_referee("Js,Td,8d,9s,7d,2d,4d") == "Td,8d,7d,4d,2d", "Flush"
    assert texas_referee("Ts,2h,Tc,3s,Td,3c,Th") == "Th,Td,Tc,Ts,3c", "Four of Kind"
    assert texas_referee("Ks,9h,Th,Jh,Kd,Kh,8s") == "Kh,Kd,Ks,Jh,Th", "Three of Kind"
    assert texas_referee("2c,3s,4s,5s,7s,2d,7h") == "7h,7s,5s,2d,2c", "Two Pairs"
    assert texas_referee("2s,3s,4s,5s,2d,7h,8h") == "8h,7h,5s,2d,2s", "One Pair"
    assert texas_referee("3h,4h,Th,6s,Ad,Jc,2h") == "Ad,Jc,Th,6s,4h", "High Cards"
