from fractions import Fraction
import numpy as np

METALS = ('gold', 'tin', 'iron', 'copper')


def checkio(alloys):
    """
        Find proportion of gold
    """
    p = np.zeros((len(alloys.keys())+1,4))
    r = np.zeros(len(alloys.keys())+1)

    n = 0
    for i in alloys.keys():
        metals = i.split('-')
        for j in metals:
            p[(n,METALS.index(j))] = 1.
        r[n] = alloys[i]
        n += 1
    
    p[-1] = np.ones(4)
    r[-1] = Fraction(1,1)
    result = np.linalg.solve(p,r)
    
    return Fraction(result[0]).limit_denominator(10000)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({
        'gold-tin': Fraction(1, 2),
        'gold-iron': Fraction(1, 3),
        'gold-copper': Fraction(1, 4),
        }) == Fraction(1, 24), "1/24 of gold"
    assert checkio({
        'tin-iron': Fraction(1, 2),
        'iron-copper': Fraction(1, 2),
        'copper-tin': Fraction(1, 2),
        }) == Fraction(1, 4), "quarter"
