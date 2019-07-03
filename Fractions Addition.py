def gcd(a,b):  
    a, b = (a, b) if a >=b else (b, a)
    if a%b == 0:  
        return b  
    else :  
        return gcd(b,a%b) 

def lcm(a,b):
    return a*b//gcd(a,b)

def add_fractions(fracts):
    lcm1 = 1
    temp = 0

    for i in fracts:
        lcm1 = lcm(lcm1, i[1])
    for i in fracts:
        temp += i[0]*int(lcm1/i[1])
    
    if not temp%lcm1:
        return int(temp/lcm1)
    else:
        gcd1 = gcd(temp, lcm1)
        temp = int(temp/gcd1)
        lcm1 = int(lcm1/gcd1)
        if temp < lcm1:
            return str(temp) + '/' + str(lcm1)
        else:
            return str(int(temp//lcm1)) + ' and ' + str(int(temp%lcm1)) + '/' + str(int(lcm1))

if __name__ == '__main__':
    print("Example:")
    print(add_fractions(((2, 3), (2, 3))))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert add_fractions(((2, 3), (2, 3))) == "1 and 1/3"
    assert add_fractions(((1, 3), (1, 3))) == "2/3"
    assert add_fractions(((1, 3), (1, 3), (1, 3))) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")