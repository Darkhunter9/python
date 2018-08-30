import copy
def checkio(bunker):
    def distance(k1,k2):
        [x1,y1] = k1
        [x2,y2] = k2
        for i in range(min(x1,x2),max(x1,x2)+1):
            for j in range(min(y1,y2),max(y1,y2)+1):
                if bunker[i][j] == "W":
                    if x1 == x2 or y1 == y2:
                        return 999
                    else:
                        k = ((y2-y1)/(x2-x1))
                        d = abs(k*i-j-k*x1+y1)/(k**2+1)**0.5
                        if d <= 2**0.5/2:
                            return 999
        return ((y2-y1)**2+(x2-x1)**2)**0.5

    if bunker[0][0] == "A":
        return 0
    batlist = []
    for i in range(len(bunker)):
        for j in range(len(bunker[0])):
            if bunker[i][j] == "B":
                batlist.append([i,j])
            if bunker[i][j] == "A":
                batlist.append([i,j])
                [Arow, Acolumn] = [i,j]
    batlist = list(enumerate(batlist))
    for i in batlist:
        if [Arow, Acolumn] == i[1]:
            Adot = i[0]
    
    distancelist = []
    for i in range(len(batlist)):
        for j in range(i+1,len(batlist)):
            distancelist.append([batlist[i][0],batlist[j][0],distance(batlist[i][1],batlist[j][1])])
    
    unvisited = [i for i in range(1, len(batlist))]
    while unvisited:
        dot = min(unvisited, key = lambda x: distancelist[x-1][2])
        unvisited.remove(dot)
        for i in unvisited:
            for j in distancelist:
                if [dot,i] == [j[0],j[1]] or [dot,i] == [j[1],j[0]]:
                    extradistance = j[2]
                    break
            distancelist[i-1][2] = min(distancelist[i-1][2],distancelist[dot-1][2]+extradistance)
    
    if distancelist[Adot-1][2] == 999:
        return None
    else:
        return round(distancelist[Adot-1][2],2)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    # checkio(["B-B--B-","-W-W-W-","--B---B","BW-W-W-","----A--","BW-W-W-","-B--B-B"])
    assert almost_equal(checkio([
        "B--",
        "---",
        "--A"]), 2.83), "1st example"
    assert almost_equal(checkio([
        "B-B",
        "BW-",
        "-BA"]), 4), "2nd example"
    assert almost_equal(checkio([
        "BWB--B",
        "-W-WW-",
        "B-BWAB"]), 12), "3rd example"
    assert almost_equal(checkio([
        "B---B-",
        "-WWW-B",
        "-WA--B",
        "-W-B--",
        "-WWW-B",
        "B-BWB-"]), 9.24), "4th example"
