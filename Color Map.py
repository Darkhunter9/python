def neighbour(n, region, ndict):
    templist = []
    for i in range(len(region)):
        if n in region[i]:
            templist.append([i,region[i].index(n)])
            break
    pointer = 0
    while pointer < len(templist):
        [i,j] = templist[pointer]
        for [k,l] in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
            if (i+k >= 0 
            and i+k < len(region) 
            and j+l >= 0 
            and j+l < len(region[0])):
                if region[i+k][j+l] == n and [i+k,j+l] not in templist:
                    templist.append([i+k,j+l])
                elif region[i+k][j+l] != n and region[i+k][j+l] not in ndict[n]:
                    ndict[n].append(region[i+k][j+l])
        pointer += 1


def color_map(region):
    N = max(max(region[i]) for i in range(len(region)))
    colordict = {}
    ndict = {}
    tasklist = []
    for i in range(N+1):
        colordict[i] = 0
        ndict[i] = []
        tasklist.append(i)
    
    while tasklist:
        n = tasklist.pop(0)
        neighbour(n, region, ndict)

    i = 0
    while i <= N:
        colordict[i] += 1
        if all(colordict[i] != colordict[j] for j in ndict[i]):
            i += 1
            continue
        if colordict[i] == 4:
            colordict[i] = 0
            i -= 1

    return list(colordict.values())


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    NEIGHS = ((-1, 0), (1, 0), (0, 1), (0, -1))
    COLORS = (1, 2, 3, 4)
    ERROR_NOT_FOUND = "Didn't find a color for the country {}"
    ERROR_WRONG_COLOR = "I don't know about the color {}"

    def checker(func, region):
        user_result = func(region)
        if not isinstance(user_result, (tuple, list)):
            print("The result must be a tuple or a list")
            return False
        country_set = set()
        for i, row in enumerate(region):
            for j, cell in enumerate(row):
                country_set.add(cell)
                neighbours = []
                if j < len(row) - 1:
                    neighbours.append(region[i][j + 1])
                if i < len(region) - 1:
                    neighbours.append(region[i + 1][j])
                try:
                    cell_color = user_result[cell]
                except IndexError:
                    print(ERROR_NOT_FOUND.format(cell))
                    return False
                if cell_color not in COLORS:
                    print(ERROR_WRONG_COLOR.format(cell_color))
                    return False
                for n in neighbours:
                    try:
                        n_color = user_result[n]
                    except IndexError:
                        print(ERROR_NOT_FOUND.format(n))
                        return False
                    if cell != n and cell_color == n_color:
                        print("Same color neighbours.")
                        return False
        if len(country_set) != len(user_result):
            print("Excess colors in the result")
            return False
        return True
    assert checker(color_map, ((11,11,11,11,11,12,12,13,13,13,),(11,8,8,8,9,9,10,10,10,13,),(11,8,2,2,2,1,1,1,10,13,),(11,8,2,2,0,0,1,1,10,13,),(11,6,6,3,0,0,4,5,5,13,),(11,6,6,3,3,4,4,5,5,14,),(11,6,6,6,7,7,5,5,5,14,),(11,11,11,11,11,14,14,14,14,14,),))
    assert checker(color_map, (
        (0, 0, 0),
        (0, 1, 1),
        (0, 0, 2),
    )), "Small"
    assert checker(color_map, (
        (0, 0, 2, 3),
        (0, 1, 2, 3),
        (0, 1, 1, 3),
        (0, 0, 0, 0),
    )), "4X4"
    assert checker(color_map, (
        (1, 1, 1, 2, 1, 1),
        (1, 1, 1, 1, 1, 1),
        (1, 1, 0, 1, 1, 1),
        (1, 0, 0, 0, 1, 1),
        (1, 1, 0, 4, 3, 1),
        (1, 1, 1, 3, 3, 3),
        (1, 1, 1, 1, 3, 5),
    )), "6 pack"
    assert checker(color_map, (
        (7,4,4,4),
        (7,0,1,5),
        (7,2,3,5),
        (6,6,6,5),
        ))
    
