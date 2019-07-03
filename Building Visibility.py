import numpy as np

def checkio(buildings):
    building_sort = sorted(buildings, key=lambda t: (t[-1],-t[1]), reverse=True)
    result = 1

    for i in range(1, len(building_sort)):
        left = building_sort[i][0]
        right = building_sort[i][2]
        for j in range(i):
            if building_sort[j][3] <= building_sort[i][1]:
                if left >= building_sort[j][0] and right <= building_sort[j][2]:
                    left = 0
                    right = 0
                    break
                elif left >= building_sort[j][0] and left < building_sort[j][2] and right > building_sort[j][2]:
                    left = building_sort[j][2]
                elif left < building_sort[j][0] and right > building_sort[j][0] and right <=  building_sort[j][2]:
                    right = building_sort[j][0]
        if left >= 0 and right > left:
            result += 1

    return result


if __name__ == '__main__':
    assert checkio([
        [1, 1, 4, 5, 3.5],
        [2, 6, 4, 8, 5],
        [5, 1, 9, 3, 6],
        [5, 5, 6, 6, 8],
        [7, 4, 10, 6, 4],
        [5, 7, 10, 8, 3]
    ]) == 5, "First"
    assert checkio([
        [1, 1, 11, 2, 2],
        [2, 3, 10, 4, 1],
        [3, 5, 9, 6, 3],
        [4, 7, 8, 8, 2]
    ]) == 2, "Second"
    assert checkio([
        [1, 1, 3, 3, 6],
        [5, 1, 7, 3, 6],
        [9, 1, 11, 3, 6],
        [1, 4, 3, 6, 6],
        [5, 4, 7, 6, 6],
        [9, 4, 11, 6, 6],
        [1, 7, 11, 8, 3.25]
    ]) == 4, "Third"
    assert checkio([
        [0, 0, 1, 1, 10]
    ]) == 1, "Alone"
    assert checkio([
        [2, 2, 3, 3, 4],
        [2, 5, 3, 6, 4]
    ]) == 1, "Shadow"