def checkio(data):
    map_point = {"0":"0","1":"2","2":"4","3":"6","4":"8","5":"1","6":"3","7":"5","8":"7","9":"9"}
    tempdata1 = ""
    for i in data[::-1]:
        if i.isalnum():
            tempdata1 += i
    tempdata2 = []
    tempsum1 = 0

    for i in range(len(tempdata1)):
        if tempdata1[i].isalpha():
            templetter = ord(tempdata1[i])-48
            if i%2 == 0:
                templetter *= 2
                if templetter > 9:
                    templetter = (templetter)//10+(templetter)%10
            tempdata2.append(str(templetter))
        
        else:
            if i%2 == 0:
                tempdata2.append(map_point[tempdata1[i]])
            else:
                tempdata2.append(tempdata1[i])

    for i in tempdata2:
        tempsum1 += int(i)
    if not tempsum1%10:
        return(["0", tempsum1])
    else:
        return([str(10-(tempsum1%10)), tempsum1])


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio("799 273 9871") == ["3", 67]), "First Test"
    assert (checkio("139-MT") == ["8", 52]), "Second Test"
    assert (checkio("123") == ["0", 10]), "Test for zero"
    assert (checkio("999_999") == ["6", 54]), "Third Test"
    assert (checkio("+61 820 9231 55") == ["3", 37]), "Fourth Test"
    assert (checkio("VQ/WEWF/NY/8U") == ["9", 201]), "Fifth Test"

    print("OK, done!")
