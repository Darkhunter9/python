from itertools import zip_longest

def simplify(fromstr):
    x = Poly((1, 0))
    return str(eval(fromstr))

class Poly(object):
    def __init__(self, coef):
        coef = tuple(coef)
        while len(coef) > 0 and coef[0] == 0:
            coef = coef[1:]
        self.coef = coef

    def __str__(self):
        if len(self.coef) == 0:
            return '0'
        return "".join(termstr(c, len(self.coef) - i - 1) for i, c in enumerate(self.coef)).lstrip('+')

    def __add__(self, other):
        if not isinstance(other, Poly):
            other = Poly((other,))
        return Poly(a + b for a, b in reversed(list(zip_longest(reversed(self.coef), reversed(other.coef), fillvalue=0))))

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + other*(-1)

    def __rsub__(self, other):
        return self*(-1) + other

    def __mul__(self, other):
        if not isinstance(other, Poly):
            return Poly(a * other for a in self.coef)

        result = Poly((0,))
        for i in range(len(other.coef)):
            shift = (0,)*i
            result += Poly((self * other.coef[-i-1]).coef + shift)
        return result

    def __rmul__(self, other):
        return self * other

    def __pow__(self, other):
        assert isinstance(other, int) and other >= 0
        if other == 0: return Poly([1])
        if other == 1: return self
        return self**(other-1) * self

def termstr(c, p):
    if c == 0: return ''
    if p == 0: return "{:+d}".format(c)

    if c == 1: c = '+'
    elif c == -1: c = '-'
    else: c = "{:+d}*".format(c)
    p = '' if p == 1 else '**'+str(p)
    return "{}x{}".format(c, p)

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # print(simplify(u"98*85*x*(x-x-(x*(x-41-(x)+3-31+(41)*54*13-x+(x))))"))
    assert simplify("(x-1)*(x+1)") == "x**2-1", "First and simple"
    assert simplify("(x+1)*(x+1)") == "x**2+2*x+1", "Almost the same"
    assert simplify("(x+3)*x*2-x*x") == "x**2+6*x", "Different operations"
    assert simplify("x+x*x+x*x*x") == "x**3+x**2+x", "Don't forget about order"
    assert simplify("(2*x+3)*2-x+x*x*x*x") == "x**4+3*x+6", "All together"
    assert simplify("x*x-(x-1)*(x+1)-1") == "0", "Zero"
    assert simplify("5-5-x") == "-x", "Negative C1"
    assert simplify("x*x*x-x*x*x-1") == "-1", "Negative C0"