import numpy as np

def is_covered(room, sensors):
    def check(x,y):
        for i in sensors:
            if (x-i[0])**2+(y-i[1])**2 <= i[2]**2:
                return True
        return False
    
    [x,y] = np.mgrid[0:room[0],0:room[1]]
    for [i,j] in np.array([x.flatten(),y.flatten()]).T:
        if not check(i,j):
            return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(is_covered([200, 150], [[100, 75, 130]]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_covered([200, 150], [[100, 75, 130]]) == True
    assert is_covered([200, 150], [[50, 75, 100], [150, 75, 100]]) == True
    assert is_covered([200, 150], [[50, 75, 100], [150, 25, 50], [150, 125, 50]]) == False
    assert is_covered([200, 150], [[100, 75, 100], [0, 40, 60], [0, 110, 60], [200, 40, 60], [200, 110, 60]]) == True
    assert is_covered([200, 150], [[100, 75, 100], [0, 40, 50], [0, 110, 50], [200, 40, 50], [200, 110, 50]]) == False
    assert is_covered([200, 150], [[100, 75, 110], [105, 75, 110]]) == False
    assert is_covered([200, 150], [[100, 75, 110], [105, 75, 20]]) == False
    assert is_covered([3, 1], [[1, 0, 2], [2, 1, 2]]) == True
    assert is_covered([30, 10], [[0, 10, 10], [10, 0, 10], [20, 10, 10], [30, 0, 10]]) == True
    assert is_covered([30, 10], [[0, 10, 8], [10, 0, 7], [20, 10, 9], [30, 0, 10]]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
