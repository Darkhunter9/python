def judge(point,steps):
    for k in range(1,len(steps)):
        if steps[k][2] == 0:
            if ((point[0]-steps[k][0])**2+(point[1]-steps[k][1])**2) != ((point[0]-steps[k-1][0])**2+(point[1]-steps[k-1][1])**2):
                return False
        else:
            if (((point[0]-steps[k][0])**2+(point[1]-steps[k][1])**2)-((point[0]-steps[k-1][0])**2+(point[1]-steps[k-1][1])**2))*steps[k][2] > 0:
                return False
    return True

def checkio(steps):
    options = [[i,j] for i in range(10) for j in range(10)]
    for [i,j,k] in steps:
        if [i,j] in options:
            options.remove([i,j])
    if len(steps) == 1:
        return options[0]
    options.sort(key = lambda x:(x[0]-steps[-1][0])**2+(x[1]-steps[-1][1])**2,reverse=True)
    for [i,j] in options:
        if judge([i,j],steps):
            return [i,j]

if __name__ == '__main__':
    # This part is using only for self-checking and not necessary for auto-testing
    from math import hypot
    MAX_STEP = 12

    def check_solution(func, goal, start):
        prev_steps = [start]
        for step in range(MAX_STEP):
            row, col = func([s[:] for s in prev_steps])
            if [row, col] == goal:
                return True
            if 10 <= row or 0 > row or 10 <= col or 0 > col:
                print("You gave wrong coordinates.")
                return False
            prev_distance = hypot(prev_steps[-1][0] - goal[0], prev_steps[-1][1] - goal[1])
            distance = hypot(row - goal[0], col - goal[1])
            alteration = 0 if prev_distance == distance else (1 if prev_distance > distance else -1)
            prev_steps.append([row, col, alteration])
        print("Too many steps")
        return False

    assert check_solution(checkio, [7, 7], [5, 5, 0]), "1st example"
    assert check_solution(checkio, [5, 6], [0, 0, 0]), "2nd example"
