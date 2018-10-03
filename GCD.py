import math
def greatest_common_divisor(*args):
    """
        Find the greatest common divisor
    """
    temp1 = list(args)
    while len(temp1) > 1:
        temp2 = math.gcd(temp1[0],temp1[1])
        temp1.pop(0)
        temp1[0] = temp2
    return temp2

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"
