from collections import deque

def check(a):
    l = []
    for i in a:
        if i in '([{':
            l.append(i)
        elif i in ')]}':
            if not l: return False
            elif l[-1]+i not in '()[]{}': return False
            else:
                l.pop()

    return True

def remove_brackets(a):
    BRACKETS = '()[]{}'
    PAIR = {'(':')','[':']','{':'}'}

    b = [i for i in a]
    l = deque()
    record = deque()

    while b:
        temp = b.pop()
        if temp in ')]}':
            if any(i+temp in '()[]{}' for i in b):
                l.appendleft(temp)
                record.appendleft(temp)
            else:
                continue
        elif temp in '([{':
            if not record: continue
            elif temp+record[0] in '()[]{}':
                l.appendleft(temp)
                record.popleft()
            else:
                if not any(temp+i in '()[]{}' for i in record):
                    continue
                else:
                    if record.index(PAIR[temp]) <= 1:
                        record.popleft()
                        record.popleft()
                        l.popleft()
                        l.appendleft(temp)                        

    return ''.join(l)


if __name__ == '__main__':
    print("Example:")
    print(remove_brackets('(()()'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert remove_brackets('(()()') == '()()'
    assert remove_brackets('[][[[') == '[]'
    assert remove_brackets('[[(}]]') == '[[]]'
    assert remove_brackets('[[{}()]]') == '[[{}()]]'
    assert remove_brackets('[[[[[[') == ''
    assert remove_brackets('[[[[}') == ''
    assert remove_brackets('') == ''
    print("Coding complete? Click 'Check' to earn cool rewards!")
