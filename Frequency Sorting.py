def frequency_sorting(numbers):
    list1 = list(set(numbers))
    list1.sort()
    list1.sort(key = lambda x: numbers.count(x), reverse = True)
    result = []
    for i in list1:
        for j in range(numbers.count(i)):
            result.append(i)
    return result

if __name__ == '__main__':
    print("Example:")
    print(frequency_sorting([1, 2, 3, 4, 5]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert frequency_sorting([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Already sorted"
    # assert frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]) == [4, 4, 4, 3, 3, 11, 11, 7, 13], "Not sorted"
    assert frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10]) == [10, 10, 21, 21, 55, 55, 99, 99], "Reversed"
    