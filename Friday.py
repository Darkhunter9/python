import calendar
def friday(day):
    date = day.split(".")
    for i in range(len(date)):
        date[i] = int(date[i])
    temp1 = calendar.weekday(date[2],date[1],date[0])
    if temp1 <= 4:
        return 4-temp1
    else:
        return 11-temp1

if __name__ == '__main__':
    print("Example:")
    print(friday('23.04.2018'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert friday('23.04.2018') == 4
    assert friday('01.01.1999') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
