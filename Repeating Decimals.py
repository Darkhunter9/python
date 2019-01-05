def convert(numerator, denominator):
    integer = numerator // denominator
    numerator -= integer * denominator

    if 0 == numerator:
        return str(integer)+"."
    elif len(str(numerator/denominator)) <= 10:
        return str(integer)+"."+str(numerator/denominator)[2:]
    else:
        dlist = []
        numerator *= 10
        while len(dlist) <= 1000:
            dlist.append(numerator // denominator)
            numerator -= dlist[-1]*denominator
            numerator *= 10

        for i in range(100):
            for j in range(1,500):
                if all(dlist[i+k] == dlist[i+j+k] == dlist[i+2*j+k] for k in range(j)):
                    for l in range(len(dlist)):
                        dlist[l] = str(dlist[l]) 
                    result = str(integer)+"."+ "".join(dlist[:i])+"("+"".join(dlist[i:i+j])+")"
                    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    convert(29,12)
    assert convert(1, 3) == "0.(3)", "1/3 Classic"
    assert convert(5, 3) == "1.(6)", "5/3 The same, but bigger"
    assert convert(3, 8) == "0.375", "3/8 without repeating part"
    assert convert(7, 11) == "0.(63)", "7/11 prime/prime"
    assert convert(29, 12) == "2.41(6)", "29/12 not and repeating part"
    assert convert(11, 7) == "1.(571428)", "11/7 six digits"
    assert convert(0, 117) == "0.", "Zero"
