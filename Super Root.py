def super_root(number):
    maximum = 10
    minimum = 1
    temp = (maximum+minimum)/2
    while abs(temp**temp-number) > 0.001:
        if temp**temp > number:
            maximum = temp
        else:
            minimum = temp
        temp = (maximum+minimum)/2
        print(temp)
    return temp

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def check_result(function, number):
        result = function(number)
        if not isinstance(result, (int, float)):
            print("The result should be a float or an integer.")
            return False
        p = result ** result
        if number - 0.001 < p < number + 0.001:
            return True
        return False
    assert check_result(super_root, 4), "Square"
    assert check_result(super_root, 9), "Cube"
    assert check_result(super_root, 10**10), "Eighty one"