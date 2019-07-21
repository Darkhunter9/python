num_dict = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',
    10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',
    20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety',
    100:'hundred'}

def num(i):
    if i < 20:
        return num_dict[i]
    elif i < 100:
        if not i//10:
            return num_dict[i]
        else:
            return num_dict[i//10*10]+' '+num_dict[i%10]
    elif i < 1000:
        temp = num_dict[i//100] + ' hundred'
        if not i//100:
            return temp
        else:
            return temp+' '+num(i%100)
    return 'one thousand'


def secret_room(number):
    num_list = []
    goal = num(number)
    for i in range(1,number+1):
        num_list.append(num(i))
    num_list.sort()
    return num_list.index(goal)+1

if __name__ == '__main__':
    secret_room(666)
    print("Example:")
    print(secret_room(5))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert secret_room(5) == 1 #five, four, one, three, two
    assert secret_room(3) == 2 #one, three, two
    assert secret_room(1000) == 551
    print("Coding complete? Click 'Check' to earn cool rewards!")
