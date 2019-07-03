import numpy as np

def checkio(matrix):
    #replace this for solution
    tempmatrix = np.array(matrix)
    record = np.zeros_like(tempmatrix, dtype=int)
    result = [0,0]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if not record[(i,j)]:
                record[(i,j)] = 1
                wlist = [(i,j)]
                count = 1
                while wlist:
                    (tempi, tempj)= wlist.pop(0)
                    for (k,l) in [(-1,0),(1,0),(0,-1),(0,1)]:
                        if (tempi+k >= 0 and tempj+l >=0 
                        and tempi+k < len(matrix) and tempj+l < len(matrix[0])
                        and record[(tempi+k,tempj+l)] == 0
                        and matrix[tempi+k][tempj+l] == matrix[tempi][tempj]):
                            record[(tempi+k,tempj+l)] = 1
                            wlist.append((tempi+k,tempj+l))
                            count += 1
                if count > result[0]:
                    result = [count, matrix[i][j]]
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [1, 2, 3, 4, 5],
        [1, 1, 1, 2, 3],
        [1, 1, 1, 2, 2],
        [1, 2, 2, 2, 1],
        [1, 1, 1, 1, 1]
    ]) == [14, 1], "14 of 1"

    assert checkio([
        [2, 1, 2, 2, 2, 4],
        [2, 5, 2, 2, 2, 2],
        [2, 5, 4, 2, 2, 2],
        [2, 5, 2, 2, 4, 2],
        [2, 4, 2, 2, 2, 2],
        [2, 2, 4, 4, 2, 2]
    ]) == [19, 2], '19 of 2'