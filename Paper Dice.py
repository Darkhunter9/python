import numpy as np
def check(m):
    count = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[(i,j)]:
                temp_count = 0
                for (di,dj) in [(-1,0),(1,0)]:
                    if i+di >=0 and i+di < len(m) and j+dj >= 0 and j+dj < len(m[0]):
                        if m[(i+di,j+dj)]:
                            temp_count += 1
                            break
                for (di,dj) in [(0,-1),(0,1)]:
                    if i+di >=0 and i+di < len(m) and j+dj >= 0 and j+dj < len(m[0]):
                        if m[(i+di,j+dj)]:
                            temp_count += 1
                            break
                if not temp_count%2:
                    count += 1
    if not count%2:
        return True
    return False


def paper_dice(paper):
    n = len(paper)
    m = len(paper[0])
    record = np.zeros((n,m), dtype=int)
    dice_dict = {}

    for i in range(n):
        for j in range(m):
            if paper[i][j].isdigit():
                record[(i,j)] = int(paper[i][j])
                dice_dict[int(paper[i][j])] = (i,j)
    
    if len(dice_dict.keys()) != 6:
        return False
    
    count = 0
    for i in dice_dict.keys():
        for j in dice_dict.keys():
            (x1,y1) = dice_dict[i]
            (x2,y2) = dice_dict[j]
            if i == j:
                continue
            elif (abs(y1-y2) == 2 or abs(x1-x2) == 2) and i+j == 7:
                if (x1 == x2 or y1 == y2) or check(record[min(x1,x2):max(x1,x2)+1,min(y1,y2):max(y1,y2)+1]):
                    count += 1
    
    if count < 6:
        return False
    
    return True



if __name__ == '__main__':
    print(paper_dice(["    ","1   ","2354","  6 ","    "]))
    assert paper_dice([
                '  1  ',
                ' 235 ',
                '  6  ',
                '  4  ']) is True, 'cross'
    assert paper_dice([
                '    ',
                '12  ',
                ' 36 ',
                '  54',
                '    ']) is True, 'zigzag'
    assert paper_dice(['123456']) is False, '1 line'
    assert paper_dice([
                '123  ',
                '  456']) is False, '2 lines_wrong'
    assert paper_dice([
                '126  ',
                '  354']) is True, '2 lines_right'
    print("Check done.")