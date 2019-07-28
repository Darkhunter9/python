def safe_code(equation):
    temp = equation.replace('=','==')
    # -1~-9
    # for i in range(-9,0):
    #     if temp.index('#') == 0 or temp[temp.index('#')-1] in '+-*=':
    #         try:
    #             temp_1 = temp.replace('#', str(i))
    #             if eval(temp_1):
    #                 return i
    #         except:
    #             pass

    # 0
    if temp.index('#') and equation[equation.index('=')+1] != '#' and '0' not in equation:
        try:
            temp_1 = temp.replace('#', '0')
            if eval(temp_1):
                return 0
        except:
            pass

    # 1-9
    for i in range(1,10):
        if str(i) not in equation:
            try:
                temp_1 = temp.replace('#', str(i))
                if eval(temp_1):
                    return i
            except:
                pass
    return -1

if __name__ == '__main__':
    print("Example:")
    print(safe_code("-5#*-1=5#"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_code("-5#*-1=5#") == 0
    assert safe_code("##*##=302#") == 5
    assert safe_code("19--45=5#") == -1
    assert safe_code("##--11=11") == -1
    assert safe_code("#9+3=22") == 1
    assert safe_code("11*#=##") == 2
    assert safe_code("#9+3=12") == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
