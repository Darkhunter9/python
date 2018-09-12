def shot(wall1, wall2, shot_point, later_point):
    #replace this for solution
    return 100

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert shot((2, 2), (5, 7), (11, 2), (8, 3)) == 100, "1st case"
    assert shot((2, 2), (5, 7), (11, 2), (7, 2)) == 0, "2nd case"
    assert shot((2, 2), (5, 7), (11, 2), (8, 4)) == 29, "3th case"
    assert shot((2, 2), (5, 7), (11, 2), (9, 5)) == -1, "4th case"
    assert shot((2, 2), (5, 7), (11, 2), (10.5, 3)) == -1, "4th case again"