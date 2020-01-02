def init_pairs(family, couples):
    c = [(x[0], x[1]) for x in couples]+[(x[1], x[0]) for x in couples]
    return [x for x in __import__('itertools').permutations(family, 2)
            if x not in c]


def is_valid(last_chain, chains, best):
    flatten = [x for y in last_chain for x in y]
    unique = list(set(flatten))
    ret = all([flatten.count(x) <= 2 for x in unique])
    return ret and not len(chains) < len(best)-1


def find_chains(family, couples):
    family = sorted(list(family))
    couples = [list(x) for x in couples]
    pairs = init_pairs(family, couples)
    stack, best = [([], [], pairs)], []
    while stack:
        chains, last_chain, pairs = stack.pop()
        if not last_chain:
            best = chains if len(best) < len(chains) else best
            if pairs:
                stack += [(chains, [pairs[0]], pairs[1:])]
            continue
        first, last = last_chain[0][0], last_chain[-1][1]
        if len(last_chain) == len(family) and first == last:
            stack += [(chains+[last_chain], [], pairs)]
            continue
        for i in [x for x in pairs if last in x[0]]:
            if is_valid(last_chain+[i], chains, best):
                remove = [x for x in pairs if x != i]
                stack += [(chains, last_chain+[i], remove)]
    return [[x[0] for x in y] for y in best]