from typing import Tuple, Iterable  # or List, Set...

def light_up(grid: Tuple[str]) -> Iterable[Tuple[int]]:
    
    *DIGITS, WALL, LIGHT, LIT, DARK, NOLIGHT = '01234XL. *'
    WALLS=DIGITS+[WALL]
    directions=((-1, 0), (1, 0), (0, -1), (0, 1))

    grid = list(map(list,grid))
    nb_row,nb_col=len(grid),len(grid[0])
    in_grid=lambda i,j: 0<=i<nb_row and 0<=j<nb_col
    neighbors={(i,j):[(i+di,j+dj) for di,dj in directions if in_grid(i+di,j+dj)] for i in range(nb_row) for j in range(nb_col) if grid[i][j] in DIGITS}
    
    def light_a_torch(i,j):
        grid[i][j]=LIGHT
        dark.remove((i,j))
        for k,l in [(k,l) for k,l in visible[(i,j)] if grid[k][l]==DARK]:
            grid[k][l]=LIT
            dark.remove((k,l))
        for k,l in [(k,l) for k,l in visible[(i,j)] if grid[k][l]==NOLIGHT]:
            grid[k][l]=LIT
            no_light.remove((k,l))

    def alone_in_the_dark(i,j):
        for k,l in visible[(i,j)]:
            if grid[k][l]==DARK: return False
        return 1992 # If you are puzzled, check on Internet what Alone in the Dark 1992 is

    def visible_neighbors(cell):
        visible=[]
        i,j=cell
        for di,dj in directions:
            ni,nj=i+di,j+dj
            while (0<=ni<nb_row and 0<=nj<nb_col and grid[ni][nj] not in WALLS):
                visible.append((ni,nj))
                ni,nj=ni+di,nj+dj
        return visible
    
    count=0
    # Let's build interesting tables:
    dark,no_light,digits=[],[],[]
    for i,row in enumerate(grid):
        for j,cell in enumerate(row):
            if cell==DARK:
                dark.append((i,j))
            elif cell in DIGITS:
                digits.append((i,j))

    visible={cell:visible_neighbors(cell) for cell in dark}
    under_test=[]
    while (dark or no_light):
        count+=1
        progressing=False
        break_out=False

        for i,j in no_light:
            if alone_in_the_dark(i,j):
                #That's too bad, no one will be able to bring us light
                break_out=True
        if not break_out:
            for i,j in list(digits):
                cell=int(grid[i][j])
                nb_light=sum([grid[k][l]==LIGHT for k,l in neighbors[(i,j)]])
                dark_neighbors=[(k,l) for k,l in neighbors[(i,j)] if grid[k][l]==DARK]
                nb_total=nb_light+len(dark_neighbors)
                if nb_light>cell:
                    # Oops too many light, let's remove last one
                    break_out=True
                elif nb_light==cell:
                    # This wall is already well lighted, let's ensure other directions will have no light
                    for k,l in dark_neighbors:
                        dark.remove((k,l))
                        grid[k][l]=NOLIGHT
                        no_light.append((k,l))
                        progressing=True
                    digits.remove((i,j))
                elif nb_total==cell:
                    # There is just enough neighbors to get full light
                    for k,l in dark_neighbors:
                        light_a_torch(k,l)
                        progressing=True
                    digits.remove((i,j))
                elif nb_total<cell:
                    break_out=True
                if break_out: break
        if not progressing and not break_out:
            for i,j in dark:
                # Dark cells must be lighted from somewhere else or be a light themselves
                if alone_in_the_dark(i,j):
                    # Let light a torch
                    light_a_torch(i,j)
                    progressing=True
        
        if not progressing and not break_out:
            # Time to do something else
            if dark:
                # Time to sort this table to make best use of our tests:
                # But as sorting is expensive, only do it once in a while
                if count%1000==0:
                    dark.sort(key=lambda cell:(sum([grid[i][j]==DARK for i,j in visible[cell]]),-len(visible[cell])))
                k,l=dark[0]
                # Keep track of grid and no_light before testing this cell
                under_test.append((k,l,
                                   [list(row) for row in grid],
                                   list(digits),
                                  ))
                light_a_torch(k,l)
            else:
                #No more options, time to move backward one step
                break_out=True
        if break_out:
            # Time to move backward one step:
            k,l,old_grid,old_digits=under_test.pop()
            grid=[list(row) for row in old_grid]
            dark,no_light=[],[]
            for i,row in enumerate(grid):
                for j,cell in enumerate(row):
                    if cell==DARK:
                        dark.append((i,j))
                    elif cell==NOLIGHT:
                        no_light.append((i,j))
            digits=list(old_digits)
            dark.remove((k,l))
            grid[k][l]=NOLIGHT
            no_light.append((k,l))
            
    return ((i,j) for i in range(nb_row) for j in range(nb_col) if grid[i][j]==LIGHT)