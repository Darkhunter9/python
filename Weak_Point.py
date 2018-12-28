def weak_point(matrix):
    sum_row = sum(matrix[0])
    row = 0
    for i in range(len(matrix)):
        if sum(matrix[i]) < sum_row:
            sum_row = sum(matrix[i])
            row = i
    
    sum_col = sum(matrix[i][0] for i in range(len(matrix)))
    col = 0
    for i in range(len(matrix[0])):
        if sum(matrix[j][i] for j in range(len(matrix))) < sum_col:
            sum_col = sum(matrix[j][i] for j in range(len(matrix)))
            col = i

    return [row,col]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"