def Ld(a, b):
    '''Levenshtein distance'''
    if not a: return len(b)
    if not b: return len(a)
    return min(Ld(a[1:], b[1:])+(a[0] != b[0]), Ld(a[1:], b)+1, Ld(a, b[1:])+1)
steps_to_convert = Ld