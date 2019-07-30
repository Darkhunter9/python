def hypercube(grid):
    word = ['h', 'y', 'p', 'e', 'r', 'c', 'u', 'b', 'e']
    start = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = grid[i][j].lower()
            if grid[i][j] == 'h':
                start.append((i,j))

    
    def find(i, j, rank, route):
        for (di,dj) in [(-1,0),(1,0),(0,-1),(0,1)]:
            if i+di >= 0 and i+di < len(grid) and j+dj >= 0 and j+dj < len(grid[0]):
                if (i+di,j+dj) not in route and grid[i+di][j+dj] == word[rank+1]:
                    if rank+2 == len(word):
                        return True
                    else:
                        if find(i+di,j+dj,rank+1,route+[((i+di,j+dj))]):
                            return True
        return

    for (i,j) in start:
        if find(i, j, 0, [(i,j)]):
            return True

    return False

if __name__ == '__main__':
    print("Example:")
    print(hypercube([
              ['g', 'f', 'H', 'Y', 'v'],
              ['z', 'e', 'a', 'P', 'u'],
              ['s', 'B', 'T', 'e', 'y'],
              ['k', 'u', 'c', 'R', 't'],
              ['l', 'O', 'k', 'p', 'r']]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert hypercube([
              ['g', 'f', 'H', 'Y', 'v'],
              ['z', 'e', 'a', 'P', 'u'],
              ['s', 'B', 'T', 'e', 'y'],
              ['k', 'u', 'c', 'R', 't'],
              ['l', 'O', 'k', 'p', 'r']]) == True
    assert hypercube([
              ['H', 'a', 't', 's', 'E'],
              ['a', 'Y', 'p', 'u', 'B'],
              ['a', 'a', 'P', 'y', 'U'],
              ['x', 'x', 'x', 'E', 'C'],
              ['z', 'z', 'z', 'z', 'R']]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
