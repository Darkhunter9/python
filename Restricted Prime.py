def checkio(number):
    '''
    that negative numbers are stored as the two's complement of the positive counterpart
    ~2 = -3
    +2: 0000 0010
    ~2: 1111 1101
    '''
    return all(i==number or pow(i,number+~False,number)==True for i in map('   , . "'.index,',."'))
    
