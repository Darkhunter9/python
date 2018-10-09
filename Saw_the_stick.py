def checkio(number):
    stop = int((2*number)**0.5)
    for i in range(1,stop):
        sum0 = 0
        list0 = []
        while i > 0:
            sum0 += i*(i+1)/2
            list0.append(i*(i+1)/2)
            if number == sum0:
                return list0
            elif sum0 > number:
                break
            i += 1
    return []


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"
