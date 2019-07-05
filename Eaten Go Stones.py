import numpy as np
from itertools import product

def judge(board, color):
    record = np.zeros((len(board), len(board[0])))
    result = 0
    for i,j in product(range(len(board)), repeat=2):
        if board[i][j] == color and record[(i,j)] == 0:
            eaten = True
            stack = [[i,j]]
            record[(i,j)] = 1
            n = 0

            while stack:
                [k,l] = stack.pop()
                n += 1
                for [x,y] in [[-1,0],[1,0],[0,1],[0,-1]]:
                    if k+x >= 0 and k+x <= len(board)-1 and l+y >= 0 and l+y <= len(board[0])-1:
                        if board[k+x][l+y] == '+':
                            eaten = False
                        elif board[k+x][l+y] == color and record[(k+x,l+y)] == 0:
                            stack.append([k+x, l+y])
                            record[(k+x,l+y)] = 1

            if eaten:
                result += n
    
    return result

def go_game(board):
    W = judge(board, 'W')
    B = judge(board, 'B')

    return {'B': B, 'W': W}

if __name__ == '__main__':
    print("Example:")
    print(go_game(['++++W++++',
                   '+++WBW+++',
                   '++BWBBW++',
                   '+W++WWB++',
                   '+W++B+B++',
                   '+W+BWBWB+',
                   '++++BWB++',
                   '+B++BWB++',
                   '+++++B+++']))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert go_game(['++++W++++',
                    '+++WBW+++',
                    '++BWBBW++',
                    '+W++WWB++',
                    '+W++B+B++',
                    '+W+BWBWB+',
                    '++++BWB++',
                    '+B++BWB++',
                    '+++++B+++']) == {'B': 3, 'W': 4}
    print("Coding complete? Click 'Check' to earn cool rewards!")