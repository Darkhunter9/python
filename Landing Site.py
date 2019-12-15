from typing import Set

def distance(c1,c2):
    return ((c1[0]-c2[0])**2+(c1[1]-c2[1])**2)**0.5

def landing_site(obstacles: Set[str]) -> Set[str]:
    coord = {}
    result = {}
    X = 'ABCDEFGHIJKL'
    for i in X:
        for j in range(1,10):
            result[i+str(j)] = 0
            x = X.index(i)*1.5
            if not X.index(i)%2:
                y = (j-1)*3**0.5
            else:
                y = (j-0.5)*3**0.5
            coord[i+str(j)] = (x,y)
    
    for i in coord.keys():
        if i not in obstacles:
            r = 1
            advance = True
            while advance:
                count = 0
                for j in coord.keys():
                    if distance(coord[i],coord[j]) <= r*3**0.5+0.05:
                        if j in obstacles:
                            r -= 1
                            advance = False
                            break
                        else:
                            count += 1
                if not advance:
                    break
                elif count != (r+1)*r*3+1:
                    advance = False
                    r -= 1
                    break
                else:
                    r += 1
            result[i] = r
            
    r = max(result.values())
    if not r:
        return set()
    site = set(i for i in result.keys() if result[i] == r)
    return site


if __name__ == '__main__':
    assert landing_site({'E5', 'E7', 'F4', 'F6', 'G4', 'G6', 'H3', 'H5'}) == {'C3', 'J7'}, 'crevasse'
    assert landing_site({'A4', 'C2', 'C6', 'C9', 'D4', 'D7', 'F1', 'F5',
                         'F8', 'G4', 'H7', 'I2', 'I5', 'I9', 'K3', 'K8', 'L5'}) == {'B7', 'E3', 'J6'}, 'stones'
    assert landing_site({'D3', 'D4', 'D5', 'D6', 'E3', 'E7', 'F2', 'F7', 'G2',
                         'G8', 'H2', 'H7', 'I3', 'I7', 'J3', 'J4', 'J5', 'J6'}) == {'G5'}, 'crater'
    assert landing_site(set()) == {'E5', 'F5', 'G5', 'H5'}, 'plane'
    assert landing_site({chr(c+65)+str(r+1) for c in range(12) for r in range(9)}) == set(), 'wasteland'

    print('The local tests are done. Click on "Check" for more real tests.')