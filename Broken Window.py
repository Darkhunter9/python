from typing import List, Tuple
from copy import deepcopy

def broken_window(pieces: List[List[int]]) -> Tuple[List[int], List[int]]:
    queue = []
    l = int(sum([len(i)-1 for i in pieces])/2)
    height = int(sum([sum(i) for i in pieces])/(l+1))

    def complete(bottom,top):
        bottom_h = [0]
        top_h = [0]

        if bottom:
            for i in range(len(bottom)):
                bottom_h[-1] = max(bottom_h[-1],bottom[i][0])
                bottom_h += bottom[i][1:]
        
        if top:
            for i in range(len(top)):
                top_h[-1] = max(top_h[-1],top[i][-1])
                top_h += top[i][::-1][1:]
        
        result = [0]*(l+1)
        for i in range(len(bottom_h)):
            result[i] += bottom_h[i]
        for i in range(len(top_h)):
            result[i] += top_h[i]

        if any(result[i] > height for i in range(len(result))):
            raise ValueError

        for i in range(len(result)):
            if result[i] < height:
                return i
        return l+1
    
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
                    # if c2 > c:
                    temp_pieces2 = deepcopy(temp_pieces)
                    temp_pieces2.remove(i)
                    queue.append([bottom,top+[i],temp_pieces2])
                except:
                    pass
        else:
            for i in temp_pieces:
                try:
                    c2 = complete(bottom+[i],top)
                    # if c2 > c:
                    temp_pieces2 = deepcopy(temp_pieces)
                    temp_pieces2.remove(i)
                    queue.append([bottom+[i],top,temp_pieces2])
                except:
                    pass
        
        if c2 == l+1:
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
    assert checker(broken_window, [[0, 3, 1, 3], [2, 4,2,5,4,2,3,4], [1,2,3,1,0]])
    assert checker(broken_window, [[0, 3, 4, 1], [4, 0], [3, 0], [0, 1, 4, 0]])
    assert checker(broken_window, [[0, 1], [0, 1]])
    assert checker(broken_window, [[1, 1], [1, 1], [1, 1], [1, 1]])
    print("Coding complete? Click 'Check' to earn cool rewards!")

