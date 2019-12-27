def mind_switcher(jounal):
    # swap and remove j from d if possible, restricted to i in N
    def swap(i, j):
        log.append({i, j})
        d[i], d[j] = d[j], d[i]
        if d[j] == j: del d[j]

    # make initial state
    d = {}
    for i, j in jounal:
        d[i], d[j] = d.get(j, j), d.get(i, i)

    # remove redundant member
    for i in list(d.keys()):
        if d[i] == i: del d[i]

    N1, N2 = 'nikola', 'sophia'
    d[N1], d[N2] = N = (N1, N2)
    log = []

    while len(d) > 2:
        if d[N1] in N and d[N2] in N:
            swap(N1, next(i for i in d.keys() if i not in N))
            swap(N2, d[N1])
        if d[N1] not in N: swap(N1, d[N1])
        if d[N2] not in N: swap(N2, d[N2])

    if d[N1] != N1: swap(N1, N2)
    return tuple(log)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def check_solution(func, data):
        robots = {"nikola": "nikola", "sophia": "sophia"}
        switched = []
        for pair in data:
            switched.append(set(pair))
            r1, r2 = pair
            robots[r1], robots[r2] = robots.get(r2, r2), robots.get(r1, r1)

        result = func(data)
        if not isinstance(result, (list, tuple)) or not all(isinstance(p, set) for p in result):
            print("The result should be a list/tuple of sets.")
            return False
        for pair in result:
            if len(pair) != 2:
                print(1, "Each pair should contain exactly two names.")
                return False
            r1, r2 = pair
            if not isinstance(r1, str) or not isinstance(r2, str):
                print("Names must be strings.")
                return False
            if r1 not in robots.keys():
                print("I don't know '{}'.".format(r1))
                return False
            if r2 not in robots.keys():
                print("I don't know '{}'.".format(r2))
                return False
            if set(pair) in switched:
                print("'{}' and '{}' already were switched.".format(r1, r2))
                return False
            switched.append(set(pair))
            robots[r1], robots[r2] = robots[r2], robots[r1]
        for body, mind in robots.items():
            if body != mind:
                print("'{}' has '{}' mind.".format(body, mind))
                return False
        return True

    assert check_solution(mind_switcher, ({"scout", "super"},))
    assert check_solution(mind_switcher, ({'hater', 'scout'}, {'planer', 'hater'}))
    assert check_solution(mind_switcher, ({'scout', 'driller'}, {'scout', 'lister'},
                                          {'hater', 'digger'}, {'planer', 'lister'}, {'super', 'melter'}))