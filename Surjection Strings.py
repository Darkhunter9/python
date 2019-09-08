def isometric_strings(str1: str, str2: str) -> bool:
    checklist = {}
    for i in range(len(str1)):
        if str1[i] not in checklist.keys():
            checklist[str1[i]] = str2[i]
        else:
            if str2[i] != checklist[str1[i]]:
                return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(isometric_strings('add', 'egg'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings('add', 'egg') == True
    assert isometric_strings('foo', 'bar') == False
    assert isometric_strings('', '') == True
    assert isometric_strings('all', 'all') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")