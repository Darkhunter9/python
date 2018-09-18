import copy

def judge(berserker,enemies):
    templist1 = set()
    templist2 = set()
    templist3 = set()
    if enemies:
        for i in enemies:
            if berserker[0] == i[0]:
                templist1.add(i)
            elif berserker[1] == i[1]:
                templist2.add(i)
        for i in templist1:
            for j in templist1:
                if i != j and (int(i[1])-int(berserker[1]))*(int(j[1])-int(berserker[1])) > 0:
                    if abs(int(i[1])-int(berserker[1])) > abs(int(j[1])-int(berserker[1])):
                        templist3.add(i)
                    else:
                        templist3.add(j)
        for i in templist2:
            for j in templist2:
                if i != j and (ord(i[0])-ord(berserker[0]))*(ord(j[0])-ord(berserker[0])) > 0:
                    if abs(ord(i[0])-ord(berserker[0])) > abs(ord(j[0])-ord(berserker[0])):
                        templist3.add(i)
                    else:
                        templist3.add(j)
    return ((templist1 | templist2) - templist3)

def berserk_rook(berserker, enemies):
    n = 0
    templist = judge(berserker,enemies)
    if not templist:
        return n
    else:
        enemylist = copy.deepcopy(enemies)
        n = max(berserk_rook(i,enemylist-{i}) for i in templist) + 1
        # for i in templist:
        #     enemylist = copy.deepcopy(enemies)
        #     enemylist.remove(i)
        #     templist2.append(berserk_rook(i,enemylist))
        # n = max(templist2) + 1
    return n

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert berserk_rook('d3', {'d6', 'b6', 'c8', 'g4', 'b8', 'g6'}) == 5, "one path"
    assert berserk_rook('a2', {'f6', 'f2', 'a6', 'f8', 'h8', 'h6'}) == 6, "several paths"
    assert berserk_rook('a2', {'f6', 'f8', 'f2', 'a6', 'h6'}) == 4, "Don't jump through"
    assert berserk_rook("c5", {"a5","d5","g5","h5","b5","e5","f5"}) == 7