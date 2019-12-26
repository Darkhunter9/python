import re

def between_markers(text: str, begin: str, end: str) -> str:
    if begin in '[{()}':
        begin = '\%s' % begin
    if end in '[{()}':
        end = '\%s' % end
            
    p = r'(%s).*?(%s)' %(begin, end)
    (b,e) = re.search(p,text).span()
    return text[b+1:e-1]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')