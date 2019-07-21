import numpy as np

def house(plan):
    if '#' not in plan:
        return 0
        
    temp_plan = plan.split('\n')[1:-1]
    x0 = len(temp_plan)-1
    x1 = 0
    y0 = len(temp_plan[0])-1
    y1 = 0

    grid = np.mgrid[0:len(temp_plan),0:len(temp_plan[0])]
    for (x,y) in zip(grid[0].flatten(),grid[1].flatten()):
        if temp_plan[x][y] == '#':
            if x < x0:
                x0 = x
            if x > x1:
                x1 = x
            if y < y0:
                y0 = y
            if y > y1:
                y1 = y
    
    return abs(x1-x0+1)*abs(y1-y0+1)

    return 0

if __name__ == '__main__':
    print("Example:")
    print(house('''
0000000
##00##0
######0
##00##0
#0000#0
'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

    assert house('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

    assert house('''0000
0000
#000
''') == 1

    assert house('''0000
0000
''') == 0

    assert house('''
0##0
0000
#00#
''') == 12

    print("Coding complete? Click 'Check' to earn cool rewards!")
