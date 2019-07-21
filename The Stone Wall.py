import numpy as np

def stone_wall(wall):
    temp = wall.split('\n')
    while '' in temp:
        temp.remove('')

    a = np.zeros((len(temp),len(temp[0])), dtype=int)
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            if temp[i][j] == '#':
                a[(i,j)] = 1
    
    record = len(a)
    while record >= 0:
        for i in range(a.shape[1]):
            if np.count_nonzero(a[:,i]) == len(a) - record:
                return i
        record -= 1

    return 0

if __name__ == '__main__':
    print("Example:")
    print(stone_wall('''
##########
####0##0##
00##0###00
'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert stone_wall('''
##########
####0##0##
00##0###00
''') == 4

    assert stone_wall('''
#00#######
#######0##
00######00
''') == 1

    assert stone_wall('''
#####
#####
#####
''') == 0

    print("Coding complete? Click 'Check' to earn cool rewards!")
