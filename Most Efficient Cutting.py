def most_efficient_cutting(bom):
    bom = sorted(bom, reverse=True)
    queue = [[6000-bom.pop(0), bom, 0]]
    result = []

    while queue:
        [current, rest, wasted] = queue.pop(0)

        if not rest:
            result.append(wasted+current)
            continue

        if all(current < i for i in rest):
            queue.append([6000-rest.pop(0), rest, wasted+current])
        else:
            for (i, next_) in enumerate(rest):
                if next_ <= current:
                    queue.append([current-next_, rest[:i]+rest[i+1:], wasted])

    return min(result)
    
    
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert(most_efficient_cutting([3000, 2200, 2000, 1800, 1600, 1300]) == 100)
    assert(most_efficient_cutting([4000, 4000, 4000]) == 6000), "wasted: 3x2000"
    assert(most_efficient_cutting([1]) == 5999), "5999"
    assert(most_efficient_cutting([3001, 3001]) == 5998), "2x2999"
    assert(most_efficient_cutting([3000, 2200, 1900, 1800, 1600, 1300]) == 200), "2x5900"
    assert(most_efficient_cutting([3000]) == 3000)
    assert(most_efficient_cutting([3000, 2200, 2000, 1800, 1600, 1400]) == 0)
    
    print('"Run" is good. How is "Check"?')