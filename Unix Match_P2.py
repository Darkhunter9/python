import re

def unix_match(filename: str, pattern: str) -> bool:
    f1 = re.sub(r'\[!\]','\[\!\]', pattern)
    f1 = re.sub(r'\[!','[^', f1)
    
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
    # print(unix_match("name.txt","name[]txt"))
    # print(unix_match('somefile.txt', '*'))
    # print(unix_match("[!]check.txt","[!]check.txt"))
    print(unix_match("checkio","[c[]heckio"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', 'somefile.txt') == True
    assert unix_match('1name.txt', '[!abc]name.txt') == True
    assert unix_match('log1.txt', 'log[!0].txt') == True
    assert unix_match('log1.txt', 'log[1234567890].txt') == True
    assert unix_match('log1.txt', 'log[!1].txt') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")