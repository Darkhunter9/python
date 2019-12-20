def sliced(piece):
    return sum(([x, y] for x, y in zip(piece, piece[1:])), [])

def is_incorrect(up, down):
    return len({x+y for x, y in zip(up, down)}) > 1

def broken_window(pieces):
    stack = [([], [], [], [], list(enumerate(pieces)))]
    while stack:
        up, down, up_idx, down_idx, pieces = stack.pop()
        if is_incorrect(up, down):
            continue
        if not pieces and len(up) == len(down):
            return up_idx, down_idx
        for k in range(len(pieces)):
            (index, piece), _pieces = pieces[k], pieces[:k]+pieces[k+1:]
            if len(up) < len(down):
                piece = sliced(piece[::-1])
                stack += [(up+piece, down, up_idx+[index], down_idx, _pieces)]
            else:
                piece = sliced(piece)
                stack += [(up, down+piece, up_idx, down_idx+[index], _pieces)]

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
    # assert checker(broken_window, [[9,7,6,13],[11,2],[0,2],[2,1,10,8,0],[11,2],[3,0],[0,7,6,4],[0,10,9,11,8,2],[11,13,5,3,12,11,5,2,4,3,13,10]])
    # assert checker(broken_window, [[0,3,0],[0,1,1,0],[3,0],[0,3,2,2,3]])
    # assert checker(broken_window, [[0, 3, 1, 3], [2, 4,2,5,4,2,3,4], [1,2,3,1,0]])
    assert checker(broken_window, [[0, 3, 4, 1], [4, 0], [3, 0], [0, 1, 4, 0]])
    assert checker(broken_window, [[0, 1], [0, 1]])
    assert checker(broken_window, [[1, 1], [1, 1], [1, 1], [1, 1]])
    print("Coding complete? Click 'Check' to earn cool rewards!")