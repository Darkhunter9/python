import copy
GOAL =  (1, 2, 1, 0, 2, 0, 0, 3, 0, 4, 3, 4)

def first(list1):
    templist = copy.deepcopy(list1)
    temp0 = templist[0]
    temp1 = templist[3]
    temp2 = templist[5]
    temp3 = templist[2]
    templist[0] = temp3
    templist[3] = temp0
    templist[5] = temp1
    templist[2] = temp2
    return templist

def second(list1):
    templist = copy.deepcopy(list1)
    temp0 = templist[1]
    temp1 = templist[4]
    temp2 = templist[6]
    temp3 = templist[3]
    templist[1] = temp3
    templist[4] = temp0
    templist[6] = temp1
    templist[3] = temp2
    return templist

def third(list1):
    templist = copy.deepcopy(list1)
    temp0 = templist[5]
    temp1 = templist[8]
    temp2 = templist[10]
    temp3 = templist[7]
    templist[5] = temp3
    templist[8] = temp0
    templist[10] = temp1
    templist[7] = temp2
    return templist

def fourth(list1):
    templist = copy.deepcopy(list1)
    temp0 = templist[6]
    temp1 = templist[9]
    temp2 = templist[11]
    temp3 = templist[8]
    templist[6] = temp3
    templist[9] = temp0
    templist[11] = temp1
    templist[8] = temp2
    return templist

goal = list(GOAL)
operatelist = [first, second, third, fourth]

def puzzle88(state):
    templist = list(state)
    task=[[templist,"1"],[templist,"2"],[templist,"3"],[templist,"4"]]
    while True:
        tempchoice = task.pop(0)
        if operatelist[int(tempchoice[-1][-1])-1](tempchoice[0]) == goal:
            return tempchoice[-1]
        else:
            part1 = operatelist[int(tempchoice[-1][-1])-1](tempchoice[0])
            part2 = tempchoice[-1]
            task.append([part1,part2+"1"])
            task.append([part1,part2+"2"])
            task.append([part1,part2+"3"])
            task.append([part1,part2+"4"])



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert puzzle88((0, 2, 1, 3, 2, 1, 4, 0, 0, 4, 0, 3)) in ('1433', '4133'), "Example"
    assert puzzle88((0, 2, 1, 2, 0, 0, 4, 1, 0, 4, 3, 3)) in ('4231', '4321'), "Rotate all"
    assert puzzle88((0, 2, 1, 2, 4, 0, 0, 1, 3, 4, 3, 0)) in ('2314', '2341', '3214', '3241'), "Four paths"
