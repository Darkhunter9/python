def match(filename, pattern):
    result = []
    lp = len(pattern)
    for i in range(len(filename)-lp+1):
        if all(pattern[j] == "?" or pattern[j] == filename[i:][j] for j in range(lp)):
            result.append(i)
    return result          
        
def unix_match(filename: str, pattern: str) -> bool:
    if all(i == "*" for i in pattern):
        return True

    plist = pattern.split("*")
    plist = [i for i in plist if i != ""]
    result = []

    for i in plist:
        result.append(match(filename,i))
    
    
    if any(not i for i in result):
        return False
    else:
        a = min(result[0])
        i = 0
        result.pop(0)
        while result:
            for j in result[0]:
                if a+len(plist[i]) <= j:
                    a = j
                    i += 1
                    result.pop(0)
                    break
            return False
        return True

if __name__ == '__main__':
    print("Example:")
    print(unix_match('somefile.txt', '*'))
    print(unix_match("l.txt","???*"))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', '*') == True
    assert unix_match('other.exe', '*') == True
    assert unix_match('my.exe', '*.txt') == False
    assert unix_match('log1.txt', 'log?.txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    assert unix_match('log12.txt', 'log??.txt') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")