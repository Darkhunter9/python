import numpy as np
from copy import deepcopy

record = 0
row = 0
column = 0
people = 0
groups = 0
units = []
it = 0
record = 0

class unit:
    def __init__(self, x, y, win, loss):
        self.x = x
        self.y = y
        self.win = win
        self.loss = loss
        self.t = self.win+self.loss

class group:
    def __init__(self):
        self.l = []
        self.wins = 0
        self.losses = 0
        self.state = 0
        self.t = 0
    
    def add(self, unit):
        self.l.append(unit)
        self.wins += unit.win
        self.losses += unit.loss
        self.t += unit.t
        if self.wins > self.losses:
            self.state = 1
        elif self.wins == self.losses:
            self.state = 0
        else:
            self.state = -1

def search(group, record):
    if group.t == people:
        return [[group, record]]
    
    temp_list = []
    result = []
    for i in group.l:
        for (dx,dy) in [(-1,0),(1,0),(0,1),(0,-1)]:
            if i.x+dx >= 0 and i.x+dx < row and i.y+dy >= 0 and i.y+dy < column:
                if (not record[(i.x+dx,i.y+dy)]) and ((i.x+dx,i.y+dy) not in temp_list):
                    temp_list.append((i.x+dx,i.y+dy))
    
    for (x,y) in temp_list:
        if group.t+units[x][y].t > people:
            continue
        else:
            temp_group = deepcopy(group)
            temp_group.add(units[x][y])
            temp_record = deepcopy(record)
            temp_record[(x,y)] = 1
            result += search(temp_group, temp_record)

    return result

def solve(solution):
    temp_solution = []
    
    for [temp_groups,record] in solution:
        temp_group = group()
        for (j,k) in zip(it[0].flatten(),it[1].flatten()):
            if not record[(j,k)]:
                temp_group.add(units[j][k])
                temp_record = deepcopy(record)
                temp_record[(j,k)] = 1
                break
        for i in search(temp_group, temp_record):
            temp_solution.append([temp_groups+[i[0]], i[1]])

    return temp_solution

def unfair_districts(amount_of_people, grid):
    global record, row, column, people, units, groups, it
    row = len(grid)
    column = len(grid[0])
    it = np.mgrid[0:row,0:column]
    record = np.zeros((row, column), dtype=int)
    people = amount_of_people
    units = []

    # build grid of units
    for i in range(row):
        units.append([])
        for j in range(column):
            units[-1].append(unit(i,j,grid[i][j][0],grid[i][j][1]))
    
    # calculate number of groups
    s = 0
    for (i,j) in zip(it[0].flatten(),it[1].flatten()):
        s += units[i][j].t
    groups = int(s/people)

    result = [[[],record]]
    for i in range(groups):
        result = solve(result)
    
    for [solution,record] in result:
        if len(solution) == groups:
            win = 0
            loss = 0
            for i in solution:
                if i.state == 1:
                    win += 1
                elif i.state == -1:
                    loss += 1
            if win > loss:
                final = ['0'*column]*row
                for i in range(groups):
                    for j in solution[i].l:
                        final[j.x] = final[j.x][:j.y]+str(i)+final[j.x][j.y+1:]
                return final

    return []

if __name__ == '__main__':

    from itertools import chain
    from collections import defaultdict

    def checker(solution, amount_of_people, grid, win_flg=True):

        w, h = len(grid[0]), len(grid)
        size = w * h
        cell_dic = {}

        # make cell_dic
        def adj_cells(cell):
            result = []
            if cell % w != 1 and cell - 1 > 0:
                result.append(cell - 1)
            if cell % w and cell + 1 <= size:
                result.append(cell + 1)
            if (cell - 1) // w:
                result.append(cell - w)
            if (cell - 1) // w < h - 1:
                result.append(cell + w)
            return set(result)

        for i, v in enumerate(chain(*grid)):
            cell_dic[i + 1] = {'vote': v, 'adj': adj_cells(i + 1)}

        answer = solution(amount_of_people, grid)

        if answer == [] and not win_flg:
            return True

        if not isinstance(answer, list):
            print('wrong data type :', answer)
            return False
        else:
            if len(answer) != h:
                print('wrong data length', answer)
                return False
            for an in answer:
                if len(an) != w:
                    print('wrong data length', an)
                    return False

        ds_dic = defaultdict(list)
        for i, r in enumerate(''.join(answer), start=1):
            ds_dic[r].append(i)

        # answer check
        def district_check(d):
            all_cells = set(d[1:])
            next_cells = cell_dic[d[0]]['adj'] & set(d)
            for _ in range(len(d)):
                all_cells -= next_cells
                next_cells = set(chain(*[list(cell_dic[nc]['adj']) for nc in next_cells])) & set(d)
            return not all_cells

        for ch, cells in ds_dic.items():
            dist_people = sum(sum(cell_dic[c]['vote']) for c in cells)
            if not district_check(cells):
                print('wrong district: ', ch)
                return False
            if dist_people != amount_of_people:
                print('wrong people:', ch)
                return False

        # win check
        win, lose = 0, 0
        for part in ds_dic.values():
            vote_a, vote_b = 0, 0
            for p in part:
                a, b = cell_dic[p]['vote']
                vote_a += a
                vote_b += b
            win += vote_a > vote_b
            lose += vote_a < vote_b

        return win > lose

    assert checker(unfair_districts, 6,[[[2,0],[1,1],[1,1],[1,1],[1,1],[0,2]],[[2,0],[1,1],[0,2],[2,0],[0,2],[1,1]]], '6x2grid')
    assert checker(unfair_districts, 5, [
        [[2, 1], [1, 1], [1, 2]],
        [[2, 1], [1, 1], [0, 2]]]), '3x2grid'

    assert checker(unfair_districts, 9, [
        [[0, 3], [3, 3], [1, 1]],
        [[1, 2], [1, 0], [1, 1]],
        [[0, 3], [2, 1], [2, 2]]]), '3x3gid'

    assert checker(unfair_districts, 8, [
        [[1, 1], [2, 0], [2, 0], [3, 3]],
        [[1, 1], [1, 2], [1, 1], [0, 3]],
        [[1, 1], [1, 1], [1, 2], [0, 3]],
        [[1, 1], [1, 1], [1, 1], [2, 0]]]), '4x4gid'

    print('check done')

