from typing import Iterable, List, Tuple, Union
from copy import deepcopy

Node = Union[int, str]
Tree = Tuple[Node, List['Tree']]


def on_same_path(tree: Tree, pairs: List[Tuple[Node, Node]]) -> Iterable[bool]:
    """For each given pair of tree's nodes, say if there are on a same path."""
    result = [True]*len(pairs)

    def search(tree,A,B):
        if not tree[1] or tree[0] == B:
            return False
        if tree[0] == A:
            if any(i[0] == B for i in tree[1]):
                return True
            elif any(search((A,i[1]),A,B) for i in tree[1]):
                return True
        else:
            return any(search(i,A,B) for i in tree[1])

        return

    for i in range(len(pairs)):
        (A, B) = pairs[i]
        result[i] = search(deepcopy(tree), A, B) or search(deepcopy(tree), B, A)

    return result


if __name__ == '__main__':
    example = on_same_path(
        ('Me', [('Daddy', [('Grandpa', []),
                           ('Grandma', [])]),
                ('Mom', [('Granny', []),
                         ('?', [])])]),
        [('Grandpa', 'Me'), ('Daddy', 'Granny')],
    )
    print('Example: it should be [True, False].')
    print(list(example))

    TESTS = (
        (
            ('Me', [('Daddy', [('Grandpa', []),
                               ('Grandma', [])]),
                    ('Mom', [('Granny', []),
                             ('?', [])])]),
            [('Grandpa', 'Me'), ('Daddy', 'Granny')],
            [True, False],
        ),
        (
            (1, [(2, [(4, []),
                      (5, [(7, []),
                           (8, []),
                           (9, [])])]),
                 (3, [(6, [])])]),
            [(1, 5), (2, 9), (2, 6)],
            [True, True, False],
        ),
        (
            (0, [(1, [(2, []),
                      (3, [])]),
                 (4, [(5, []),
                      (6, [])]),
                 (7, [(8, []),
                      (9, [])])]),
            [(4, 2), (0, 5), (2, 3), (9, 2), (6, 4), (7, 8), (8, 1)],
            [False, True, False, False, True, True, False],
        ),
    )

    for test_nb, (tree, pairs, answers) in enumerate(TESTS, 1):
        user_result = list(on_same_path(tree, pairs))
        if user_result != answers:
            print(f'You failed the test #{test_nb}.')
            print(f'Your result: {user_result}')
            print(f'Right result: {answers}')
            break
    else:
        print('Well done! Click on "Check" for real tests.')