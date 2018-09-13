def shot(wall1, wall2, shot_point, later_point):
    def line(p1:tuple,p2:tuple):
        A = p2[1]-p1[1]
        B = p1[0]-p2[0]
        C = p1[1]*p2[0]-p1[0]*p2[1]
        return (A,B,C)

    def intersection(line1:tuple,line2:tuple):
        if line1[0]*line2[1] == line1[1]*line2[0]:
            return False
        else:
            A = (line2[2]*line1[1]-line1[2]*line2[1])/(line1[0]*line2[1]-line2[0]*line1[1])
            B = (line2[2]*line1[0]-line1[2]*line2[0])/(line1[1]*line2[0]-line2[1]*line1[0])
            return (A,B)
    
    wall = line(wall1,wall2)
    shoot = line(shot_point,later_point)
    shoot_point = intersection(wall,shoot)
    wall_middle = ((wall1[0]+wall2[0])/2,(wall1[1]+wall2[1])/2)
    if not shoot_point:
        return -1
    else:
        if (shoot_point[0] < min(wall1[0],wall2[0]) or
        shoot_point[0] > max(wall1[0],wall2[0]) or
        shoot_point[1] < min(wall1[1],wall2[1]) or
        shoot_point[1] > max(wall1[1],wall2[1]) or
        later_point[0] < min(shot_point[0],shoot_point[0]) or
        later_point[0] > max(shot_point[0],shoot_point[0])):
            return -1
        else: 
            point = (1-((shoot_point[0]-wall_middle[0])**2+(shoot_point[1]-wall_middle[1])**2)**0.5/((wall1[0]-wall_middle[0])**2+(wall1[1]-wall_middle[1])**2)**0.5)*100
            return int(round(point))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert shot((2, 2), (5, 7), (11, 2), (8, 3)) == 100, "1st case"
    assert shot((2, 2), (5, 7), (11, 2), (7, 2)) == 0, "2nd case"
    assert shot((2, 2), (5, 7), (11, 2), (8, 4)) == 29, "3th case"
    assert shot((2, 2), (5, 7), (11, 2), (9, 5)) == -1, "4th case"
    assert shot((2, 2), (5, 7), (11, 2), (10.5, 3)) == -1, "4th case again"