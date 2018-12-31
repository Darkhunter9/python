GOAL =  (1, 2, 1, 0, 2, 0, 0, 3, 0, 4, 3, 4)


def puzzle88(state):
    s = list(state)
    moves = 0
    out = ''
    while (moves < 12) and (score(s) != (0,-6)):
        min_i, min_score, min_farthest = -1, 60, 6
        for i in range(4):
            cur_farthest, cur_score = score(rotate(s, i))
            if (cur_score + 100*cur_farthest) < (min_score+100*min_farthest):
                min_score, min_farthest = cur_score, cur_farthest
                min_i = i
        out += str(min_i+1)
        moves += 1
        #print(s, min_i, out)
        s = rotate(s, min_i)
        #print(out, s, min_score, min_farthest)
    return out

def rotate(state, disc):
    rotate_disc = [[2,1,5,0,4,3,6,7,8,9,10,11],[0,3,2,6,1,5,4,7,8,9,10,11],
                   [0,1,2,3,4,7,6,10,5,9,8,11],[0,1,2,3,4,5,8,7,11,6,10,9]]
    return [state[rotate_disc[disc][i]] for i in range(12)]

def score(state):
    scores = [[1,2,2,0,1,0,0,1,0,2,2,1],[0,5,0,2,4,1,3,2,4,6,3,5],[2,0,3,1,0,4,2,5,3,5,6,4],
              [4,6,5,3,5,2,4,0,1,3,0,2],[5,3,6,4,2,3,1,4,2,0,5,0]]
    extra_score = [[None, None],[0,2],[4,1],[7,10],[11,9]]
    farthest, out = -1, 0
    for i in range(5):
        for j in range(12):
            if state[j] == i:
                if (j == extra_score[i][0]):
                    if (state[extra_score[i][1]] != i):
                        #print(j, i, state[j], extra_score[i], state[extra_score[i][1]])
                        out += 3
                        farthest = max(farthest, 3)
                    else:
                        out -= 1.5
                farthest = max(farthest, scores[i][j])
                out += scores[i][j]
    #print(farthest, out)
    return farthest, out

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert puzzle88((0, 2, 1, 3, 2, 1, 4, 0, 0, 4, 0, 3)) in ('1433', '4133'), "Example"
    assert puzzle88((0, 2, 1, 2, 0, 0, 4, 1, 0, 4, 3, 3)) in ('4231', '4321'), "Rotate all"
    assert puzzle88((0, 2, 1, 2, 4, 0, 0, 1, 3, 4, 3, 0)) in ('2314', '2341', '3214', '3241'), "Four paths"