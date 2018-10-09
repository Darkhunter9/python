def checkio(first, second):
    result = 0
    firstb = bin(first)[2:]
    second = bin(second)[2:]
    for i in firstb:
        for j in range(len(second)):
            result += (int(i) & int(second[j]))*2**(len(second)-1-j)
            result += (int(i) | int(second[j]))*2**(len(second)-1-j)
            if i != second[j]:
                result += 2**(len(second)-1-j)
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18