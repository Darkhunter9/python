def steps_to_convert(line1,line2):
    def compare(line1,line2,i):
        tempdict = {}
        for j in range(len(line1)):
            if line1[j] in line2:
                try:
                    tempdict[i+j] = line2.index(line1[j],max(tempdict.values()) if tempdict else 0)
                except Exception:
                    continue
        return tempdict

    def calculate(line1,line2,similardict):
        result = 0
        temp3 = -1
        temp4 = -1
        while similardict:
            result += max(min(similardict.keys())-1-temp3,similardict[min(similardict.keys())]-temp4-1)
            temp3 = min(similardict.keys())
            temp4 = similardict[min(similardict.keys())]
            similardict.pop(min(similardict.keys()))
        result += max(len(line1)-temp3-1,len(line2)-temp4-1) 
        return result

    result = None
    for i in range(len(line1)):
        tempdict = {}
        tempdict = compare(line1[i:],line2,i)
        if result == None:
            result = calculate(line1,line2,tempdict)
        else:
            result = min(result,calculate(line1,line2,tempdict))
    for i in range(len(line2)):
        tempdict = {}
        tempdict = compare(line2[i:],line1,i)
        if result == None:
            result = calculate(line2,line1,tempdict)
        else:
            result = min(result,calculate(line2,line1,tempdict))
        
    if result == None:
        return 0
    else:
        return result


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert steps_to_convert('line1', 'line1') == 0, "eq"
    assert steps_to_convert('line1', 'line2') == 1, "2"
    assert steps_to_convert('line', 'line2') == 1, "none to 2"
    assert steps_to_convert('ine', 'line2') == 2, "need two more"
    assert steps_to_convert('line1', '1enil') == 4, "everything is opposite"
    assert steps_to_convert('', '') == 0, "two empty"
    assert steps_to_convert('l', '') == 1, "one side"
    assert steps_to_convert('', 'l') == 1, "another side"
    print("You are good to go!")
