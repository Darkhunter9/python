import heapq
cx = [-1,0,1,0]
cy = [0,1,0,-1]

def checkio(data):
    priority_queue = []
    heapq.heapify(priority_queue)
    rown = len(data)
    coln = len(data[0])
    visit = set()
    for i in range(coln):
        if data[0][i] == 1:
            heapq.heappush(priority_queue, (1, 0, i))
        else:
            heapq.heappush(priority_queue, (0, 0, i))
        visit.add((0, i))

    while priority_queue:
        step, x, y = heapq.heappop(priority_queue)
        #print x, y, step
        if x == rown-1:
            return step
        for i in range(4):
            tx = x + cx[i]
            ty = y + cy[i]
            if tx >= 0 and tx < rown and ty >= 0 and ty < coln:
                if (tx, ty) not in visit:
                    if data[tx][ty] == 1:
                        heapq.heappush(priority_queue, (step+1, tx, ty))
                    else:
                        heapq.heappush(priority_queue, (step, tx, ty))
                    visit.add((tx, ty))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[1, 1, 1, 1, 0, 1, 1],
                    [1, 1, 1, 1, 0, 0, 1],
                    [1, 1, 1, 1, 1, 0, 1],
                    [1, 1, 0, 1, 1, 0, 1],
                    [1, 1, 0, 1, 1, 1, 1],
                    [1, 0, 0, 1, 1, 1, 1],
                    [1, 0, 1, 1, 1, 1, 1]]) == 2, "1st example"
    assert checkio([[0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 0, 1, 0, 1, 1],
                    [1, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0]]) == 3, "2nd example"
    assert checkio([[1, 1, 1, 1, 1, 0, 1, 1],
                    [1, 0, 1, 1, 1, 0, 1, 1],
                    [1, 0, 1, 0, 1, 0, 1, 0],
                    [1, 0, 1, 1, 1, 0, 1, 1],
                    [0, 0, 1, 1, 0, 0, 0, 0],
                    [1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 0, 1, 1, 1, 1]]) == 2, "3rd example"