import math
import numpy as np

def calculate(rest,cut):
    return [rest[0]*cut[1] - cut[0]*rest[1],rest[1]*cut[1]]

def divide_pie(groups):
    np.set_numeric_ops(suppress=True)
    number = 0
    rest = [1,1]
    for i in groups:
        number += abs(i)
    for i in groups:
        if i > 0:
            rest = calculate(rest,[i,number])
        else:
            rest = calculate(rest,[-i*rest[0],number*rest[1]])
    temp = math.gcd(rest[0],rest[1])
    return (int(rest[0]/temp),int(rest[1]/temp))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance((2, -2), (tuple, list)), "Return tuple or list"
    assert tuple(divide_pie((2, -1, 3))) == (1, 18), "Example"
    assert tuple(divide_pie((1, 2, 3))) == (0, 1), "All know about the pie"
    assert tuple(divide_pie((-1, -1, -1))) == (8, 27), "One by one"
    assert tuple(divide_pie((10,))) == (0, 1), "All together"