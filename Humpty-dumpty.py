import math
def checkio(height, width):
    if height == width:
        S = 4*math.pi*(height/2)**2

    if height < width:
        e = (1-(height/2)**2/(width/2)**2)**0.5
        S = 2*(width/2)**2*math.pi+math.pi*(height/2)**2/e*math.log((1+e)/(1-e))

    elif height > width:
        e = (1-(width/2)**2/(height/2)**2)**0.5
        S = 2*(width/2)**2*math.pi*(1+(height/2)/(width/2)/e*math.asin(e))
    
    V = 4/3*math.pi*(height/2)*(width/2)**2
    return [round(V,2), round(S,2)]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"