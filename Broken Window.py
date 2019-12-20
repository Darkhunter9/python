from typing import List, Tuple
from copy import deepcopy

def broken_window(pieces: List[List[int]]) -> Tuple[List[int], List[int]]:
    queue = []
    l = int(sum([len(i)-1 for i in pieces])/2)
    height = int(sum([sum([(i[j]+i[j+1])*0.5 for j in range(len(i)-1)]) for i in pieces])/l)

    def complete(bottom,top):
        '''
        calculate the number of completed points
        raise ValueError if clearly the order doesn't work
        '''

        bottom_h = []
        top_h = []
        c = 0

        if bottom:
            bottom_h = deepcopy(bottom[0])
            for i in range(1,len(bottom)):
                bottom_h[-1] = [bottom_h[-1],bottom[i][0]]
                bottom_h += bottom[i][1:]
        
        if top:
            top_h = deepcopy(top[0][::-1])
            for i in range(1,len(top)):
                top_h[-1] = [top_h[-1],top[i][-1]]
                top_h += top[i][::-1][1:]
        
        n = min(len(bottom_h),len(top_h))
        for i in range(n):
            if isinstance(bottom_h[i], int) and isinstance(top_h[i],int):
                if bottom_h[i] + top_h[i] != height:
                    raise ValueError
                else:
                    c += 1
            elif isinstance(bottom_h[i], list) and isinstance(top_h[i],list):
                if bottom_h[i][0] + top_h[i][0] == bottom_h[i][1] + top_h[i][1] == height:
                    c += 1
                else:
                    raise ValueError
            elif isinstance(bottom_h[i], int) and isinstance(top_h[i],list):
                if i < n-1 or i == len(bottom_h)-1:
                    if bottom_h[i] + top_h[i][0] != height:
                        raise ValueError
                    else:
                        c += 1
                else:
                    if bottom_h[i] + top_h[i][0] == bottom_h[i] + top_h[i][1] == height:
                        c += 1
                    else:
                        raise ValueError
            elif isinstance(bottom_h[i], list) and isinstance(top_h[i],int): 
                if i < n-1 or i == len(top_h)-1:
                    if bottom_h[i][0] + top_h[i] != height:
                        raise ValueError
                    else:
                        c += 1
                else:
                    if bottom_h[i][0] + top_h[i] == bottom_h[i][1] + top_h[i] == height:
                        c += 1
                    else:
                        raise ValueError

        return c
    
    def output():
        [bottom, top, temp_pieces] = queue[-1]
        bottom_indices = []
        top_indices = []

        for i in bottom:
            indices = [j for j, x in enumerate(pieces) if x == i]
            for j in indices:
                if j not in bottom_indices and j not in top_indices:
                    bottom_indices.append(j)
                    break
        for i in top:
            indices = [j for j, x in enumerate(pieces) if x == i]
            for j in indices:
                if j not in bottom_indices and j not in top_indices:
                    top_indices.append(j)
                    break
        
        return (top_indices,bottom_indices)

    for i in pieces:
        temp_pieces = deepcopy(pieces)
        temp_pieces.remove(i)        
        queue.append([[i],[],temp_pieces])
    
    while queue:
        [bottom, top, temp_pieces] = queue.pop()
        c = complete(bottom,top)

        if sum([len(i)-1 for i in bottom]) >= sum([len(i)-1 for i in top]):
            for i in temp_pieces:
                try:
                    c2 = complete(bottom,top+[i])
                    temp_pieces2 = deepcopy(temp_pieces)
                    temp_pieces2.remove(i)
                    queue.append([bottom,top+[i],temp_pieces2])
                    if 'c2' in locals() and c2 == l+1:
                        return output()
                except:
                    pass
        else:
            for i in temp_pieces:
                try:
                    c2 = complete(bottom+[i],top)
                    temp_pieces2 = deepcopy(temp_pieces)
                    temp_pieces2.remove(i)
                    queue.append([bottom+[i],top,temp_pieces2])
                    if 'c2' in locals() and c2 == l+1:
                        return output()
                except:
                    pass

    return ([],[])


if __name__ == '__main__':

    def checker(func, pieces):
        answer = func(pieces)

        if not (isinstance(answer, (tuple, list))
                and len(answer) == 2
                and isinstance(answer[0], list) and isinstance(answer[1], list)):
            print('wrong type:', answer)
            return False

        if set(answer[0]+answer[1]) != set(range(len(pieces))):
            print('wrong value:', answer)
            return False

        tops = [list(reversed(pieces[t])) for t in answer[0]]
        bottoms = [pieces[b] for b in answer[1]]
        height = set()

        top = tops.pop(0)
        bottom = bottoms.pop(0)
        while True:
            height |= set(map(sum, zip(top, bottom)))
            if len(top) < len(bottom) and tops:
                bottom = bottom[len(top)-1:]
                top = tops.pop(0)
            elif len(top) > len(bottom) and bottoms:
                top = top[len(bottom)-1:]
                bottom = bottoms.pop(0)
            elif len(top) == len(bottom):
                if tops and bottoms:
                    top = tops.pop(0)
                    bottom = bottoms.pop(0)
                elif not tops and not bottoms:
                    break
                else:
                    return False
            else:
                return False

        return len(height) == 1

    print("Example:")
    # print(broken_window([[0, 1], [0, 1]]))
    assert checker(broken_window, [[9,7,6,13],[11,2],[0,2],[2,1,10,8,0],[11,2],[3,0],[0,7,6,4],[0,10,9,11,8,2],[11,13,5,3,12,11,5,2,4,3,13,10]])
    assert checker(broken_window, [[0,3,0],[0,1,1,0],[3,0],[0,3,2,2,3]])
    assert checker(broken_window, [[0, 3, 1, 3], [2, 4,2,5,4,2,3,4], [1,2,3,1,0]])
    assert checker(broken_window, [[0, 3, 4, 1], [4, 0], [3, 0], [0, 1, 4, 0]])
    assert checker(broken_window, [[0, 1], [0, 1]])
    assert checker(broken_window, [[1, 1], [1, 1], [1, 1], [1, 1]])
    print("Coding complete? Click 'Check' to earn cool rewards!")

