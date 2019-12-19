from typing import Iterable


def flood_area(diagram: str) -> Iterable[int]:
    points = [0]
    area = []
    result = [0]
    dh = {'\\': -1,
        '_': 0,
        '/': 1}
    
    for i in diagram:
        points.append(points[-1]+dh[i])

    max_h = max(points)
    middle = points.index(max_h)
    for i in range(len(points)-1):
        if diagram[i] == '\\':
            area.append(0.5+max_h-points[i])
        elif diagram[i] == '_':
            area.append(max_h-points[i])
        else:
            area.append(-0.5+max_h-points[i])
    
    for i in range(max_h-1,min(points[0],points[-1])-1,-1):
        for j in range(middle):
            if all(i >= points[k] for k in range(0,j+2)):
                area[j] -= 1
            elif all(i >= points[k] for k in range(0,j+1)) and i < points[j+1]:
                area[j] -= 0.5
        
        for j in range(len(points)-1,middle,-1):
            if all(i >= points[k] for k in range(len(points)-1,j-2,-1)):
                area[j-1] -= 1
            elif all(i >= points[k] for k in range(len(points)-1,j-1,-1)) and i < points[j-1]:
                area[j-1] -= 0.5
    
    i = 0
    h = 0
    while area:
        if area[0] > 0.5:
            result[-1] += area.pop(0)
        elif area[0] == 0.5 and diagram[i] == '/':
            result[-1] += area.pop(0)
            h = points[i+1]
            result.append(0)
        else:
            h = points[i+1]
            result.append(area.pop(0))
        i += 1
    
    result = [i for i in result if i > 0]
    return result


if __name__ == '__main__':
    print("Example:")
    print(list(flood_area(r'\\//')))
    assert list(flood_area(r'\\//')) == [4], 'valley'
    assert list(flood_area(r'/\\///\_/\/\\\\/_/\\///__\\\_\\/_\/_/')) == [4, 2, 1, 19, 9], 'mountains'
    assert list(flood_area(r'_/_\_')) == [], 'hill'

    print("Coding complete? Click 'Check' to earn cool rewards!")

