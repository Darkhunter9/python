from math import pi, acos
from itertools import product

def fortress_cannons(fort, cannons, enemies):
    directions = ['N', 'S', 'NE', 'SE', 'NW', 'SW']
    direction_coords = [(0,-1),(0,1),(0.5*3**0.5,-0.5),(0.5*3**0.5,0.5),(-0.5*3**0.5,-0.5),(-0.5*3**0.5,0.5)]
    coords = {}
    plan = {}

    for i in 'ABCDEFGHIJKL':
        for j in range(1,10):
            x = (ord(i)-65)*0.5*3**0.5
            if (ord(i)-65)%2:
                y = (j-1)+0.5
            else:
                y = j-1
            coords[i+str(j)] = (x,y)
    
    def distance(x0, y0, x1, y1):
        return ((x1-x0)**2+(y1-y0)**2)**0.5

    def distance_manhattan(cell):
        ''' Calculate Manhattan distance between two cells. '''
        return max([abs(cell[0]), abs(cell[1]), abs(cell[0] + cell[1])])

    def cover(fort, arc, direction, dmin, dmax):
        direction_coord = direction_coords[directions.index(direction)]
        b = (direction_coord[0]**2 + direction_coord[1]**2)**0.5
        theta = arc/180*pi/2
        (x0, y0) = coords[fort]
        result = []

        for i in 'ABCDEFGHIJKL':
            for j in range(1,10):
                (x1, y1) = coords[i+str(j)]
                a = distance(x0,y0,x1,y1)
                x_step = int(round(abs(x1-x0)/(0.5*3**0.5)))
                y_step = int(round(abs(y1-y0)-0.5*x_step)) if abs(y1-y0)-0.5*x_step >= 0 else 0
                if dmin <= x_step+y_step <= dmax:
                    c = distance(x1,y1,x0+direction_coord[0],y0+direction_coord[1])
                    theta_1 = acos(max(min((a**2+b**2-c**2)/2/a/b,1),-1))
                    if theta_1 - theta <= 0.05:
                        result.append(i+str(j))
                else:
                    continue
        return result
    
    # print(distance(*coords['A3'],*coords['L3']))
    for n,(arc, dmin, dmax) in enumerate(cannons):
        plan[n] = {}
        for i in directions:
            plan[n][i] = cover(fort, arc, i, dmin, dmax)
    
    for i in product(directions, repeat=len(cannons)):
        covered = set()
        for j in enumerate(i):
            covered = covered | set(plan[j[0]][j[1]])
            if all(k in covered for k in enemies):
                return list(i)
    return None

if __name__ == '__main__':
    fortress_cannons("D6",[[60,2,2],[60,4,4],[60,6,6],[60,8,8]],["F5","G4","J4","K2"])
    assert fortress_cannons('F5', [(0, 1, 4)], {'F2'}) == ['N'], '0 degree'
    assert fortress_cannons('F5', [(60, 1, 6)], {'K4'}) == ['NE'], '60 degree' 
    assert fortress_cannons('F5', [(120, 1, 4)],{'B3', 'E8'}) == ['SW'], '120 degree'
    assert fortress_cannons('F5', [(0, 2, 6), (120, 1, 3), (60, 1, 4)], {'L2', 'D3', 'C6', 'E9'}) == ['NE', 'NW', 'S'], '3 cannons'
    assert fortress_cannons('F5', [(0, 1, 6), (120, 2, 3)], {'A3', 'E6', 'G7'}) is None, 'None'
    print("Coding complete? Click 'Check' to earn cool rewards!")

