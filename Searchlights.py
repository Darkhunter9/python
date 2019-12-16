from math import pi, sin, cos, tan

def judge(p,lights):
    [(x0,y0)] = p
    [(x, y, r)] = lights
    return (x0-x)**2+(y0-y)**2 <= r**2

def searchlights(polygons, lights):
    result = 0
    for polygon in polygons:
        
        [x0,y0,l,k] = polygon
        
        if any(judge([(x0,y0)],[(x,y,r)]) for [x,y,r] in lights):
            result += 1

        angle0 = pi-2*pi/k

        angle = (pi-angle0)*0.5
        k0 = tan(angle)
        
        for i in range(k-1):
            if i+1 > k/2:
                dy = l/(1/k0**2+1)**0.5
            else:
                dy = -l/(1/k0**2+1)**0.5
            dx = dy/k0
            if k0 < 9999 and abs(k0) > 10**(-4):
                x0 += dx
                y0 += dy
            elif k0 >= 9999:
                if i+1 > k/2:
                    y0 += l
                else:
                    y0 -= l
            else:
                if i+1 > k/2:
                    x0 += l
                else:
                    x0 -= l
            if x0 > 0 and y0 > 0 and any(judge([(x0,y0)],[(x,y,r)]) for [x,y,r] in lights):
                    result += 1

            angle += (pi-angle0)
            k0 = tan(angle)

    return result


if __name__ == '__main__':
    # print("Example:")
    # print (searchlights([(2, 3, 2, 3)], [(1, 2, 1)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert(searchlights([(2, 3, 2, 3)], [(1, 2, 1)])) == 1, 'regular triangle'
    # assert(searchlights([(4, 5, 2, 4)], [(4, 4, 3)])) == 4, 'square'
    assert(searchlights([(6, 7, 2, 5)], [(2, 3, 2)])) == 0, 'regular pentagon'
    assert(searchlights([(4, 2, 2, 6)], [(4, 2, 3)])) == 3, 'regular hexagon'
    assert(searchlights([(1, 7, 2, 8)], [(0, 5, 4)])) == 5, 'regular octagon'
    print("Coding complete? Click 'Check' to earn cool rewards!")