import numpy as np
from copy import copy
from itertools import permutations

def check(square):
    if np.count_nonzero(square) != square.shape[0]*square.shape[1]:
        return False
    else:
        temp1 = np.sum(square, axis=1)
        temp2 = np.sum(square.T, axis=1)
        temp3 = np.sum(np.diagonal(square))
        temp4 = np.sum(np.diagonal(square[::-1]))
        if temp3 != temp4 or np.any(temp3 != temp1) or np.any(temp3 != temp2):
            return False
    return True

def checkio(data):
    if type(data) != np.ndarray:
        square = np.array(data)
    else:
        square = data

    n = len(data)
    templist = []

    coord = np.where(square == 0)

    for i in range(1,n**2+1):
        if i not in square:
            templist.append(i)
    
    for i in permutations(templist):
        squarecopy = copy(square)
        count = 0
        for j in zip(coord[0], coord[1]):
            squarecopy[j] = i[count]
            count += 1
        if check(squarecopy):
            return squarecopy.tolist()



if __name__ == '__main__':
    #This part is using only for self-testing.
    def check_solution(func, in_square):
        SIZE_ERROR = "Wrong size of the answer."
        MS_ERROR = "It's not a magic square."
        NORMAL_MS_ERROR = "It's not a normal magic square."
        NOT_BASED_ERROR = "Hm, this square is not based on given template."
        result = func(in_square)
        #check sizes
        N = len(result)
        if len(result) == N:
            for row in result:
                if len(row) != N:
                    print(SIZE_ERROR)
                    return False
        else:
            print(SIZE_ERROR)
            return False
        #check is it a magic square
        # line_sum = (N * (N ** 2 + 1)) / 2
        line_sum = sum(result[0])
        for row in result:
            if sum(row) != line_sum:
                print(MS_ERROR)
                return False
        for col in zip(*result):
            if sum(col) != line_sum:
                print(MS_ERROR)
                return False
        if sum([result[i][i] for i in range(N)]) != line_sum:
            print(MS_ERROR)
            return False
        if sum([result[i][N - i - 1] for i in range(N)]) != line_sum:
            print(MS_ERROR)
            return False

        #check is it normal ms
        good_set = set(range(1, N ** 2 + 1))
        user_set = set([result[i][j] for i in range(N) for j in range(N)])
        if good_set != user_set:
            print(NORMAL_MS_ERROR)
            return False
        #check it is the square based on input
        for i in range(N):
            for j in range(N):
                if in_square[i][j] and in_square[i][j] != result[i][j]:
                    print(NOT_BASED_ERROR)
                    return False
        return True


    assert check_solution(checkio,
                          [[2, 7, 6],
                           [9, 5, 1],
                           [4, 3, 0]]), "1st example"

    assert check_solution(checkio,
                          [[0, 0, 0],
                           [0, 5, 0],
                           [0, 0, 0]]), "2nd example"

    assert check_solution(checkio,
                          [[1, 15, 14, 4],
                           [12, 0, 0, 9],
                           [8, 0, 0, 5],
                           [13, 3, 2, 16]]), "3rd example"
