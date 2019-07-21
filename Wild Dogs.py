import itertools as it
import numpy as np

def line(coords):
    if all(i[0] == coords[0][0] for i in coords):
        return abs(coords[0][0])
    elif all(i[0] == i[1] for i in coords):
        return 0
    else:
        if len(coords) >= 3:
            k = (coords[0][1]-coords[1][1]) / (coords[0][0]-coords[1][0])
            for j in coords[2:]:
                if ((j[1]-coords[1][1]) / (j[0]-coords[1][0])) != k:
                    return False

        A = np.array(coords[:2])
        b = np.ones((2,1))
        s = np.linalg.solve(A,b)
        return 1 / (s[(0,0)]**2+s[(1,0)]**2)**0.5
    

def wild_dogs(coords):
    n = len(coords)
    distance = 999
    while n >= 2:
        for i in it.combinations(coords, n):
            in_line = line(i)
            if in_line is not False:
                distance = min(distance,in_line)
        if distance < 999:
            if not distance%1:
                return int(distance)
            else:
                return round(distance,2)
        n -= 1
    return 0

if __name__ == '__main__':
    print("Example:")
    wild_dogs([[2,20],[3,25],[10,60],[20,110],[1,-17],[540,-11]])
    print(wild_dogs([(7, 122), (8, 139), (9, 156), 
                     (10, 173), (11, 190), (-100, 1)]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert wild_dogs([(7, 122), (8, 139), (9, 156), 
                      (10, 173), (11, 190), (-100, 1)]) == 0.18

    assert wild_dogs([(6, -0.5), (3, -5), (1, -20)]) == 3.63

    assert wild_dogs([(10, 10), (13, 13), (21, 18)]) == 0

    print("Coding complete? Click 'Check' to earn cool rewards!")
