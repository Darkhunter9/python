'''
Compute the convex hull of the cloud.
For each edge of the convex hull:
    compute the edge orientation (with arctan),
    rotate the convex hull using this orientation in order to compute easily the bounding rectangle area with min/max of x/y of the rotated convex hull,
    Store the orientation corresponding to the minimum area found,
Return the rectangle corresponding to the minimum area found
'''

from math import atan2,atan,cos,sin

def distance(pa,pb):
    return ((pa[0]-pb[0])**2+(pa[1]-pb[1])**2)**0.5

def calculate_angle(p0,p1,p2):
    d01 = distance(p0,p1)
    d02 = distance(p0,p2)
    d12 = distance(p1,p2)
    return (d01**2+d12**2-d02**2)/2/d01/d12
    

def inscribe(contour):
    points = sorted(contour,key=lambda i: i[1])
    hull = []

    # 1st point
    hull.append(points[0])
    
    # 2nd point
    point = hull[0]
    points.sort(key= lambda i: atan2((i[1]-point[1]),(i[0]-point[0])))
    hull.append(points.pop(1))

    # rest points
    point0 = hull[0]
    point1 = hull[1]
    while point1 != hull[0]:
        points.sort(key= lambda i: calculate_angle(point0,point1,i))
        hull.append(points.pop(0))
        point0 = point1
        point1 = hull[-1]
    hull.pop()

    result = []
    for i in range(len(hull)):
        point0 = hull[i]
        point1 = hull[i-1]

        if point0[0] == point1[0]:
            result.append((max([j[1] for j in hull])-min([j[1] for j in hull]))*(max([j[0] for j in hull])-min([j[0] for j in hull])))
        else:
            theta = -atan((point0[1]-point1[1])/(point0[0]-point1[0]))
            c = cos(theta)
            s = sin(theta)
            hull_temp = [(c*j[0]-s*j[1],s*j[0]+c*j[1]) for j in hull]
            result.append((max([j[1] for j in hull_temp])-min([j[1] for j in hull_temp]))*(max([j[0] for j in hull_temp])-min([j[0] for j in hull_temp])))
    return min(result)


if __name__ == '__main__':
    # print("Example:")
    # print(inscribe([(1, 1), (1, 2), (0, 2), (3, 5), (3, 4), (4, 4)]))

    def close_enough(contour, answer):
        result = inscribe(contour)
        assert abs(result - answer) <= 1e-3, \
            f'inscribe({contour}) == {answer}, and not {result}'

    # These "asserts" are used for self-checking and not for an auto-testing
    close_enough([(1, 1), (1, 2), (0, 2), (3, 5), (3, 4), (4, 4)], 6.0)
    close_enough([(6, 5), (10, 7), (2, 8)], 20.0)
    close_enough([(2, 3), (3, 8), (8, 7), (9, 2), (3, 2), (4, 4), (6, 6), (7, 3), (5, 3)], 41.538)
    close_enough([(0, 0), (0, 10), (0, 20), (100, 20), (100, 30), (120, 30), (120, 20), (120, 10), (20, 10), (20, 0)], 2679.208)
    close_enough([(10, 250), (60, 300), (300, 60), (250, 10)], 24000.0)
    close_enough([(10, 250), (60, 300), (110, 250), (160, 300), (210, 250), (160, 200), (300, 60), (250, 10)], 48000.0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
