from itertools import combinations, permutations

def check(cube):
    common = set(cube[0])
    for i in range(1,len(cube)):
        common = common & set(cube[i])
    if len(common) < 4:
        return False
    
    for i in combinations(common,4):
        for (c1,c2,c3,c4) in permutations(i,4):
            relationship = None
            if (set([cube[0].index(c1), cube[0].index(c2)]) in ({0,3},{1,2},{4,5}) and
            set([cube[0].index(c3), cube[0].index(c4)]) in ({0,3},{1,2},{4,5})):
                relationship = [(c1,c2),(c3,c4)]
                break
        if not relationship:
            continue
        else:
            if all(set([j.index(c1), j.index(c2)]) in ({0,3},{1,2},{4,5}) and
        set([j.index(c3), j.index(c4)]) in ({0,3},{1,2},{4,5}) for j in cube[1:]):
                return True       
    
    return False

def tower(cubes):
    n = len(cubes)
    while n > 1:
        for i in combinations(cubes,n):
            if check(i):
                return n
        n -= 1
    return 1

if __name__ == '__main__':
    print("Example:")
    print(tower(['GYVABW', 'AOCGYV', 'CABVGO', 'OVYWGA']))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert tower(['GYVABW', 'AOCGYV', 'CABVGO', 'OVYWGA']) == 3
    assert tower(['ABCGYW', 'CAYRGO', 'OCYWBA', 'ACYVBR', 'GYVABW']) == 1
    assert tower(['GYCABW', 'GYCABW', 'GYCABW', 'GYCABW', 'GYCABW']) == 5
    print("Coding complete? Click 'Check' to earn cool rewards!")
