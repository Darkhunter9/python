def convert(numerator, denominator):
    integer = numerator // denominator 
    result = [integer, "."]
    numerator = numerator - denominator * integer
    memory = dict()
    while True:
        if numerator == 0:
            break
        if numerator in memory:
            index = memory[numerator]
            result.insert(index, "(")
            result.append(")")
            break
        memory[numerator] = len(result)
        numerator *= 10
        number = numerator // denominator
        result.append(number)
        numerator = numerator - number * denominator
    return "".join(map(str, result))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # convert(29,12)
    assert convert(1, 3) == "0.(3)", "1/3 Classic"
    assert convert(5, 3) == "1.(6)", "5/3 The same, but bigger"
    assert convert(3, 8) == "0.375", "3/8 without repeating part"
    assert convert(7, 11) == "0.(63)", "7/11 prime/prime"
    assert convert(29, 12) == "2.41(6)", "29/12 not and repeating part"
    assert convert(11, 7) == "1.(571428)", "11/7 six digits"
    assert convert(0, 117) == "0.", "Zero"