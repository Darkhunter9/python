import re
import numpy as np

def checkio(text, words):
    key = words.lower().split(' ')
    if '' in key:
        key.remove('')
    for i in range(len(key)):
        for j in '.?!':
            if j in key[i]:
                key[i] = key[i].replace(j, '\\'+j)
    textlist = text.split(' ')

    for i in range(len(textlist)):
        record = []
        for j in key:
            for _ in range(len(textlist[i])):
                match = re.finditer(j, textlist[i][_:].lower())
                for s in match:
                    begin = s.span()[0] + _
                    end = s.span()[1] + _
                    record.append((begin, end))
                    for k in range(len(record)-1):
                        if record[k][1]-record[k][0]+end-begin > \
                        max(record[k][1],record[k][0],begin,end)-min(record[k][1],record[k][0],begin,end):
                            record[k] = (min(record[k][1],record[k][0],begin,end), max(record[k][1],record[k][0],begin,end))
                            if len(record) > 1:
                                record.pop(-1)
                            break
            for k in range(len(record)-1):
                for l in range(k+1,len(record)):
                    if record[k][1]-record[k][0]+record[l][1]-record[l][0] > \
                        max(record[k][1],record[k][0],record[l][1],record[l][0])-min(record[k][1],record[k][0],record[l][1],record[l][0]):
                            record[k] = (min(record[k][1],record[k][0],record[l][1],record[l][0]), max(record[k][1],record[k][0],record[l][1],record[l][0]))
                            record.pop(l)
        
        if record:
            record = sorted(record, reverse=True)
            for j in record:
                textlist[i] = textlist[i][0:j[0]] + '<span>' + textlist[i][j[0]:j[1]] + '</span>' + textlist[i][j[1]:]

    return ' '.join(textlist)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    checkio("abcdefghijklmnopqrstuvwxyz", "z y x w v u t s r q p o n m l k j i h g f e d c b a")
    checkio("aaaa", "aa a")
    checkio("123456789", "3 6")
    assert (checkio("This is only a text example for task example.", "example") ==
            "This is only a text <span>example</span> for task <span>example</span>."), "Simple test"

    assert (checkio("Python is a widely used high-level programming language.", "pyThoN") ==
            "<span>Python</span> is a widely used high-level programming language."), "Ignore letters cases, but keep original"

    assert (checkio("It is experiment for control groups with similar distributions.", "is im") ==
            "It <span>is</span> exper<span>im</span>ent for control groups with s<span>im</span>ilar d<span>is</span>tributions."), "Several subwords"

    assert (checkio("The National Aeronautics and Space Administration (NASA).", "nasa  THE") ==
            "<span>The</span> National Aeronautics and Space Administration (<span>NASA</span>)."), "two spaces"

    assert (checkio("Did you find anything?", "word space tree") ==
            "Did you find anything?"), "No comments"

    assert (checkio("Hello World! Or LOL", "hell world or lo") ==
            "<span>Hello</span> <span>World</span>! <span>Or</span> <span>LO</span>L"), "Contain or intersect"



