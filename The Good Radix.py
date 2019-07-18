def checkio(number):
    def radix(n,k):
        result = 0
        for i in range(len(k)):
            if k[i].isdigit():
                result += int(k[i])*n**(len(k)-1-i)
            else:
                result += (ord(k[i])-55)*n**(len(k)-1-i)
        return result
        
    n = max(number)
    if n.isdigit():
        n = int(n)+1
    else:
        n = ord(n) - 54
    n = max(n,2)
    
    while n<37:
        if not radix(n,number)%(n-1):
            return n
        else:
            n += 1
    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("18") == 10, "Simple decimal"
    assert checkio("1010101011") == 2, "Any number is divisible by 1"
    assert checkio("222") == 3, "3rd test"
    assert checkio("A23B") == 14, "It's not a hex"
    assert checkio("IDDQD") == 0, "k is not exist"
    print('Local tests done')
