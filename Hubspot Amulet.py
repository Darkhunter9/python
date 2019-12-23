import numpy as np

def checkio(matrix):
    d = {0:0,1:225,2:315}
    r = {}

    for i in range(3):
        c = [j[i] for j in matrix]
        angle_min = -180*sum(c)-d[i]
        angle_max = 180*sum(c)-d[i]
        r[i] = [angle_min//360+1,angle_max//360+1]
    
    c = np.array(matrix).T
    for i in range(r[0][0],r[0][1]):
        for j in range(r[1][0],r[1][1]):
            for k in range(r[2][0],r[2][1]):
                result = np.linalg.solve(c,np.array([[360*i],[360*j+225],[360*k+315]]))
                if all(l >= -180 and l <= 180 and abs(l-round(l))<10**(-3) for l in result.flatten()):
                    # return result.flatten().tolist()
                    return [int(round(i)) for i in result.flatten()]

    

    return [0, 0, 0]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':

    def check_it(func, matrix):
        result = func(matrix)
        if not all(-180 <= el <= 180 for el in result):
            print("The angles must be in range from -180 to 180 inclusively.")
            return False
        f, s, t = result
        temp = [0, 0, 0]
        temp[0] += f
        temp[1] += matrix[0][1] * f
        temp[2] += matrix[0][2] * f

        temp[0] += matrix[1][0] * s
        temp[1] += s
        temp[2] += matrix[1][2] * s

        temp[0] += matrix[2][0] * t
        temp[1] += matrix[2][1] * t
        temp[2] += t
        temp = [n % 360 for n in temp]
        if temp == [0, 225, 315]:
            return True
        else:
            print("This is the wrong final position {0}.".format(temp))
            return False

    assert check_it(checkio, [[1,3,5],[3,1,5],[2,5,1]])
    assert check_it(checkio,
                    [[1, 2, 3],
                     [3, 1, 2],
                     [2, 3, 1]]), "1st example"
    assert check_it(checkio,
                    [[1, 4, 2],
                     [2, 1, 2],
                     [2, 2, 1]]), "2nd example"
    assert check_it(checkio,
                    [[1, 2, 5],
                     [2, 1, 1],
                     [2, 5, 1]]), "3rd example"