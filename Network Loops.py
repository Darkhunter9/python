def find_cycle(connections):
    def findloop(point, route, startpoint, lastpoint, connections):
        for (i,j) in connections:
            if point in (i,j):
                if point == j:
                    i,j = j,i
                if j != lastpoint:
                    if j == startpoint:
                        resultlist.append(route+[j])
                    elif j not in route:
                        findloop(j, route+[j], startpoint, i, connections)

    elementbook = set()
    resultlist = []
    for (i,j) in connections:
        elementbook.add(i)
        elementbook.add(j)

    for i in elementbook:
        findloop(i, [i], i, i, connections)

    if resultlist:
        resultlist.sort(key = lambda x: len(x), reverse = True)
        return resultlist[0]
    else:
        return []

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def checker(function, connections, best_size):
        user_result = function(connections)
        if not isinstance(user_result, (tuple, list)) or not all(isinstance(n, int) for n in user_result):
            print("You should return a list/tuple of integers.")
            return False
        if not best_size and user_result:
            print("Where did you find a cycle here?")
            return False
        if not best_size and not user_result:
            return True
        if len(user_result) < best_size + 1:
            print("You can find a better loop.")
            return False
        if user_result[0] != user_result[-1]:
            print("A cycle starts and ends in the same node.")
            return False
        if len(set(user_result)) != len(user_result) - 1:
            print("Repeat! Yellow card!")
            return False
        for n1, n2 in zip(user_result[:-1], user_result[1:]):
            if (n1, n2) not in connections and (n2, n1) not in connections:
                print("{}-{} is not exist".format(n1, n2))
                return False
        return True, "Ok"

    
    assert checker(find_cycle, 
                   ((1, 2), (2, 3), (3, 4), (4, 5), (5, 7), (7, 6),
                    (8, 5), (8, 4), (1, 5), (2, 4), (1, 8)), 6), "Example"
    assert checker(find_cycle, 
                   ((1, 2), (2, 3), (3, 4), (4, 5), (5, 7), (7, 6), (8, 4), (1, 5), (2, 4)), 5), "Second"
