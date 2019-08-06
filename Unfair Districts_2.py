from collections import defaultdict

def unfair_districts(amount_of_people, grid):
    rows = len(grid)
    cols = len(grid[0])

    dist_map = [[' ' for _ in range(cols)] for _ in range(rows)]

    def find_blank():
        for i in range(rows):
            for j in range(cols):
                if dist_map[i][j] == ' ':
                    return i, j
        return None, None

    def check_win():
        count_by_dist = defaultdict(int)
        for i in range(rows):
            for j in range(cols):
                count_by_dist[dist_map[i][j]] += grid[i][j][0] - grid[i][j][1]
        wins = 0
        losses = 0
        for result in count_by_dist.values():
            if result > 0:
                wins += 1
            elif result < 0:
                losses += 1
        return wins > losses

    def build_dist(c, total, row, col):
        new_total = total + sum(grid[row][col])
        if new_total > amount_of_people:
            return False

        dist_map[row][col] = c

        # If we have enough people in this district, start building the next district.
        # Or if the map is full, check if we won.
        if new_total == amount_of_people:
            next_c = chr(ord(c) + 1)
            next_row, next_col = find_blank()

            if next_row is not None:
                result = build_dist(next_c, 0, next_row, next_col)
            else:
                result = check_win()

            if not result:
                dist_map[row][col] = ' '
            return result

        for i in range(rows):
            for j in range(cols):
                # Try each blank adjacent cell recursively.
                if dist_map[i][j] != ' ':
                    continue
                if (i > 0 and dist_map[i-1][j] == c
                        or j > 0 and dist_map[i][j-1] == c
                        or i < rows-1 and dist_map[i+1][j] == c
                        or j < cols - 1 and dist_map[i][j+1] == c):
                    result = build_dist(c, new_total, i, j)
                    if result:
                        return True

        # No win here. Backtrack.
        dist_map[row][col] = ' '
        return False

    result = build_dist('A', 0, 0, 0)

    if result:
        return [''.join(row) for row in dist_map]

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