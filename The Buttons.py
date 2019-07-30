import numpy as np

def buttons(ceiling):
    result = []
    ceiling_list = ceiling.split('\n')
    while '' in ceiling_list:
        ceiling_list.remove('')

    state = np.zeros((len(ceiling_list),len(ceiling_list[0])),dtype=int)
    for i in range(state.shape[0]):
        for j in range(state.shape[1]):
            if ceiling_list[i][j] != '0':
                state[(i,j)] = 1
    
    for i in range(state.shape[0]):
        for j in range(state.shape[1]):
            if ceiling_list[i][j] != '0' and state[(i,j)]:
                s = int(ceiling_list[i][j])
                temp_list = [(i,j)]
                state[(i,j)] = 0
                while temp_list:
                    (k,l) = temp_list.pop()
                    for (dk,dl) in [(-1,0),(1,0),(0,1),(0,-1)]:
                        if k+dk >= 0 and l+dl >= 0 and k+dk < len(ceiling_list) and l+dl < len(ceiling_list[0]):
                            if ceiling_list[k+dk][l+dl] != '0' and state[(k+dk,l+dl)]:
                                s += int(ceiling_list[k+dk][l+dl])
                                state[(k+dk,l+dl)] = 0
                                temp_list.append((k+dk,l+dl))
                result.append(s)

    return sorted(result, reverse=True)

if __name__ == '__main__':
    print("Example:")
    print(buttons('''
001203
023001
100220'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert buttons('''
001203
023001
100220''') == [8, 4, 4, 1]

    assert buttons('''
000000
000055
000055''') == [20]

    assert buttons('''
908070
060504
302010''') == [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
