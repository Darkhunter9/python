def escape(jar, fly):
    W, H, d = jar
    x0, y0, vx, vy = fly

    for i in range(20):
        if vx > 0:
            t1 = (W-x0)/vx
            x1 = W
        elif vx < 0:
            t1 = x0/(-vx)
            x1 = 0
        else:
            x1 = x0
            t1 = None
        
        if vy > 0:
            t2 = (H-y0)/vy
            y1 = H
        elif vy < 0:
            t2 = y0/(-vy)
            y1 = 0
        else:
            y1 = y0
            t2 = None

        if t1 != None and t2 != None:
            if t1 < t2:
                y1 = y0+t1*vy
                vx *= -1
            elif t1 > t2:
                x1 = x0+t2*vx
                vy *= -1
            else:
                vx *= -1
                vy *= -1
        elif t2 and x0 > (W-d)/2 and x0 < (W+d)/2:
            return True
        else:
            return False
            


        x0 = x1
        y0 = y1

        if x0 > (W-d)/2 and x0 < (W+d)/2 and y0 == H:
            return True

    return False


if __name__ == '__main__':
    escape([1000,4000,200],[0,0,1333,1250])
    escape([1200,2000,350],[600,2000,600,1])
    escape([1200,2000,400],[0,0,-600,-133])
    print("Example:")
    print(escape([1000, 1000, 200], [0, 0, 100, 0]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert escape([1000, 1000, 200], [0, 0, 100, 0]) == False, "First"
    assert escape([1000, 1000, 200], [450, 50, 0, -100]) == True, "Second"
    assert escape([1000, 1000, 200], [450, 1000, 100, 0]) == False, "Third"
    assert escape([1000, 1000, 200], [250, 250, -10, -50]) == False, "Fourth"
    assert escape([1000, 2000, 200], [20, 35, 100, 175]) == True, "Fifth"
    print("Coding complete? Click 'Check' to earn cool rewards!")