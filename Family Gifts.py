from copy import deepcopy

def find_chains(family, couples):
    nb = len(family)
    possible_receiver = {}
    f = sorted(list(family))

    for i in family:
        possible_receiver[i] = family-{i}
    for i in couples:
        [A,B] = list(i)
        possible_receiver[A] -= {B}
        possible_receiver[B] -= {A}

    chains = []
    queue = [[f.pop(0)]]
    while queue:
        temp_chain = queue.pop(0)
        for i in possible_receiver[temp_chain[-1]]:
            if i not in temp_chain:
                temp_chain_2 = temp_chain+[i]
                if len(temp_chain_2) < nb:
                    queue.append(temp_chain_2)
                elif temp_chain_2[0] in possible_receiver[temp_chain_2[-1]]:
                    chains.append(temp_chain_2)

    if not chains:
        return []

    def conflict(chains_of_chains):
        receiver = {}
        for i in family:
            receiver[i] = set()

        for chain in chains_of_chains:
            for i in range(len(chain)):
                if chain[i] in receiver[chain[i-1]]:
                    return True
                else:
                    receiver[chain[i-1]] |= {chain[i]}

        return False

    result = []
    # queue = [[[i], [j for j in chains if not conflict([i,j])]] for i in chains]
    queue = [[[chains[0]], [j for j in chains if not conflict([chains[0],j])]]]
    while queue:
        [temp_chains_of_chains, possible_chains] = queue.pop(0)
        possible_chains = [i for i in possible_chains if not conflict([temp_chains_of_chains[-1],i])]
        if not possible_chains:
            result.append(temp_chains_of_chains)
        else:
            for i in possible_chains:
                queue.append([temp_chains_of_chains+[i], deepcopy(possible_chains)])
                

    result.sort(key=lambda x: len(x))
    return result[-1]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def checker(function, family, couples, total):
        user_result = function(family.copy(), tuple(c.copy() for c in couples))
        if (not isinstance(user_result, (list, tuple)) or
                any(not isinstance(chain, (list, tuple)) for chain in user_result)):
            return False
        if len(user_result) < total:
            return False
        gifted = set()
        for chain in user_result:
            if set(chain) != family or len(chain) != len(family):
                return False
            for f, s in zip(chain, chain[1:] + [chain[0]]):
                if {f, s} in couples:
                    return False
                if (f, s) in gifted:
                    return False
                gifted.add((f, s))
        return True

    find_chains({"Louis","Theodore","Eleanor","Sondra","David","Herbert","Fay","Alexandria","Meghan","Nettie","Autumn","June","Jane","Jeffery","Herminia","Jeannie","Lynnette"}, ({"Theodore","Meghan"},{"Herbert","Eleanor"},{"Louis","Autumn"},{"Nettie","David"},{"Jeffery","Fay"},))
    find_chains({"Loraine","Leah","Jenifer","Russell","Benjamin","Todd","Maryanne","Penny","Matthew"}, ({"Loraine","Benjamin"},{"Leah","Matthew"},{"Todd","Jenifer"},))
    assert checker(find_chains, {'Gary', 'Jeanette', 'Hollie'},
                   ({'Gary', 'Jeanette'},), 0), "Three of us"
    assert checker(find_chains, {'Curtis', 'Lee', 'Rachel', 'Javier'},
                   ({'Rachel', 'Javier'}, {'Curtis', 'Lee'}), 2), "Pairs"
    assert checker(find_chains, {'Philip', 'Sondra', 'Mary', 'Selena', 'Eric', 'Phyllis'},
                   ({'Philip', 'Sondra'}, {'Eric', 'Mary'}), 4), "Pairs and Singles"
