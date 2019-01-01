import re
from copy import deepcopy

def unix_match(filename: str, pattern: str) -> bool:
    f1 = re.sub(r'\[!\]','\[\!\]', pattern)
    f1 = re.sub(r'\[!','[^', f1)
    
    try:
        if re.match(f1,filename) and "!" not in pattern:
            return True
    except Exception:
        pass

    f1 = f1.replace(".", "\\.").replace("*", ".*").replace("?", ".")

    try:
        if re.match(f1,filename):
            return True
    except Exception:
        f1 = re.sub(r'\[\]','\[\]', f1)
        if re.match(f1,filename):
            return True
    
    
    return False


if __name__ == '__main__':
    print("Example:")
    print(unix_match('somefile.txt', '*'))
    print(unix_match("[?*]","[[][?][*][]]"))
    print(unix_match("1name.txt","[!1234567890]*"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', '*') == True
    assert unix_match('other.exe', '*') == True
    assert unix_match('my.exe', '*.txt') == False
    assert unix_match('log1.txt', 'log?.txt') == True
    assert unix_match('log1.txt', 'log[1234567890].txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    assert unix_match('log12.txt', 'log??.txt') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")