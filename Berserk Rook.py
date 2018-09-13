def berserk_rook(berserker, enemies):
    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert berserk_rook('d3', {'d6', 'b6', 'c8', 'g4', 'b8', 'g6'}) == 5, "one path"
    assert berserk_rook('a2', {'f6', 'f2', 'a6', 'f8', 'h8', 'h6'}) == 6, "several paths"
    assert berserk_rook('a2', {'f6', 'f8', 'f2', 'a6', 'h6'}) == 4, "Don't jump through"