GOAL = (1, 2, 1, 0, 2, 0, 0, 3, 0, 4, 3, 4)


def puzzle88(state):

    def rotate(n, st):

        wk = list(st)
        if n == 1:
            wk[0], wk[3], wk[5], wk[2] = st[2], st[0], st[3], st[5]
        if n == 2:
            wk[1], wk[4], wk[6], wk[3] = st[3], st[1], st[4], st[6]
        if n == 3:
            wk[5], wk[8], wk[10], wk[7] = st[7], st[5], st[8], st[10]
        if n == 4:
            wk[6], wk[9], wk[11], wk[8] = st[8], st[6], st[9], st[11]

        return tuple(wk)

    def solve( st, step='', min_step = ''):

        if min_step and len(step) >= len( min_step):
            return min_step

        if st == GOAL or len(step) >= 10:
            if st == GOAL:
                min_step = step
            return min_step

        for n in range(1, 5):
            min_step = solve(rotate(n, st), step + str(n), min_step)
        return min_step

    return solve(state)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert puzzle88((0, 2, 1, 3, 2, 1, 4, 0, 0, 4, 0, 3)) in ('1433', '4133'), "Example"
    assert puzzle88((0, 2, 1, 2, 0, 0, 4, 1, 0, 4, 3, 3)) in ('4231', '4321'), "Rotate all"
    assert puzzle88((0, 2, 1, 2, 4, 0, 0, 1, 3, 4, 3, 0)) in ('2314', '2341', '3214', '3241'), "Four paths"
