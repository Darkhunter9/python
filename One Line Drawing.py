from copy import deepcopy

def draw(segments):
    segments2 = deepcopy(segments)    
    points = []
    for i in segments:
        points.append((i[0],i[1]))
        points.append((i[2],i[3]))
    points = set(points)

    intersections = {}
    odd = 0
    ends = []
    for i in points:
        intersections[i] = []
        for j in segments:
            if i[0] == j[0] and i[1] == j[1]:
                intersections[i].append((j[2],j[3]))
            elif i[0] == j[2] and i[1] == j[3]:
                intersections[i].append((j[0],j[1]))
        if len(intersections[i])%2:
            odd += 1
            ends.append(i)

    if odd == 1 or odd >= 3:
        return []
    
    if ends:
        start = ends[0]
        end = ends[1]
    else:
        start = list(points)[0]
        end = intersections[start][0]

    result = [tuple(start)]
    current = start
    while segments2:
        for i in segments2:
            p1 = (i[0],i[1])
            p2 = (i[2],i[3])
            if current == p1 and p2 != end and p2 != start and end not in intersections[p2]:
                current = p2
                segments2 -= {i}
                result.append(p2)
                break
            elif current == p2 and p1 != end and p1 != start and end not in intersections[p1]:
                current = p1
                segments2 -= {i}
                result.append(p1)
                break
        else:
            for i in segments2:
                p1 = (i[0],i[1])
                p2 = (i[2],i[3])
                if current == p1:
                    current = p2
                    segments2 -= {i}
                    result.append(p2)
                    break
                elif current == p2:
                    current = p1
                    segments2 -= {i}
                    result.append(p1)
                    break
    
    return tuple(result)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def checker(func, in_data, is_possible=True):
        user_result = func(in_data)
        if not is_possible:
            if user_result:
                print("How did you draw this?")
                return False
            else:
                return True
        if len(user_result) < 2:
            print("More points please.")
            return False
        data = list(in_data)
        for i in range(len(user_result) - 1):
            f, s = user_result[i], user_result[i + 1]
            if (f + s) in data:
                data.remove(f + s)
            elif (s + f) in data:
                data.remove(s + f)
            else:
                print("The wrong segment {}.".format(f + s))
                return False
        if data:
            print("You forgot about {}.".format(data[0]))
            return False
        return True

    assert checker(draw,{(1,1,2,2),(2,1,2,2),(2,1,3,2),(2,1,3,1),(1,1,0,2),(1,1,0,0),(3,2,3,1),(0,0,0,2)})
    assert checker(draw,{(55,30,55,55),(40,20,55,55),(55,30,70,44),(10,50,55,55),(10,50,40,20),(40,20,70,44),(40,20,55,30),(55,55,70,44),(10,50,55,30),(10,50,70,44)})
    assert checker(draw,{(11,11,55,66),(22,33,33,56),(22,33,55,66),(11,11,22,33),(55,66,33,56)})
    assert checker(draw,{(50,40,60,40),(60,10,70,20),(20,40,30,40),(50,10,60,10),(30,10,40,25),(10,30,20,40),(40,25,50,10),(30,40,40,25),(20,10,30,10),(10,20,10,30),(60,40,70,30),(10,20,20,10),(40,25,50,40),(70,30,70,20)})
    assert checker(draw,
                   {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5)}), "Example 1"
    assert checker(draw,
                   {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7),
                    (4, 7, 7, 5), (7, 5, 7, 2), (1, 5, 7, 2), (7, 5, 1, 2)},
                   False), "Example 2"
    assert checker(draw,
                   {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5),
                    (7, 5, 7, 2), (1, 5, 7, 2), (7, 5, 1, 2), (1, 5, 7, 5)}), "Example 3"
