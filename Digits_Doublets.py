import copy

def findnumber(number,numlist):
        answer = []
        for i in numlist:
            A = str(i)
            B = str(number)
            n = 0
            for j in range(len(A)):
                if A[j] != B[j]:
                    n += 1
            if n == 1:
                answer.append(i)
        return answer

def checkio(numbers):
    list1 = copy.deepcopy(numbers)
    list1.remove(numbers[0])
    result = []

    def findanswer(prelist,numlist):
        for k in findnumber(prelist[-1],numlist):
            if k == numbers[-1]:
                result.append(prelist+[numbers[-1]])
            else:
                templist = copy.deepcopy(numlist)
                templist.remove(k)
                findanswer(prelist+[k],templist)

    findanswer([numbers[0]],list1)
    return min(result, key = lambda x: len(x))


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999], "First"
    assert checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777], "Second"
    assert checkio([456, 455, 454, 356, 656, 654]) == [456, 454, 654], "Third, [456, 656, 654] is correct too"