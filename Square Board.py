from typing import Tuple
Coordinate = Tuple[int, int]


def square_board(side: int, token: int, steps: int) -> Coordinate:
    perimeter = 4*side-4
    coord = {}
    for i in range(perimeter):
        if i < side:
            coord[i] = (side-1,side-1-i)
        elif i < 2*side-1:
            coord[i] = (2*side-2-i,0)
        elif i < 3*side-2:
            coord[i] = (0,i-2*side+2)
        else:
            coord[i] = (i-3*side+3,side-1)
    
    final = (token+steps+10*perimeter) %perimeter
    return coord[final]

if __name__ == '__main__':
    print("Example:")
    print(square_board(4, 1, 4))
    assert square_board(4, 1, 4) == (1, 0)
    assert square_board(6, 2, -3) == (4, 5)

    print("Coding complete? Click 'Check' to earn cool rewards!")

