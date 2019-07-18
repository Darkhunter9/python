move_dict = [[1,2],[-1,2],[1,-2],[-1,-2]]
def move(start):
    result = []

    for i in start:
        tempresult = []
        x = ord(i[0]) - 96
        y = int(i[1])

        result.append(chr(x+96)+str(y))
        for [dx, dy] in move_dict:
            if x+dx > 0 and y+dy > 0 and x+dx < 9 and y+dy < 9:
                tempresult.append([x+dx, y+dy])
            if x+dy > 0 and y+dx > 0 and x+dy < 9 and y+dx < 9:
                tempresult.append([x+dy, y+dx])
        
        for [x, y] in tempresult:
            result.append(chr(x+96)+str(y))

    return result

def chess_knight(start, moves):
    tempresult = [start]
    result = []

    for i in range(moves):
        tempresult = move(tempresult)

    for i in tempresult:
        if i not in result:
            result.append(i)
    
    if moves%2:
        result.remove(start)

    return sorted(result)

if __name__ == '__main__':
    print("Example:")
    print(chess_knight('a1', 1))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert chess_knight('a1', 1) == ['b3', 'c2']
    assert chess_knight('h8', 2) == ['d6', 'd8', 'e5', 'e7', 'f4', 'f7', 'f8', 'g5', 'g6', 'h4', 'h6', 'h8']
    print("Coding complete? Click 'Check' to earn cool rewards!")