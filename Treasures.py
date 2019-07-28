import numpy as np
from math import gcd
# def calculate(l,g,s,r,n1,n2,n3):
#     if g[2]:
#         if l > g[1]:
#             temp_g = [g[0],g[1],g[2]-1]
#             return calculate(l-g[1],temp_g,s,r,n1+1,n2,n3)
#         else:
#             m = n1*g[0] + n2*s[0] + n3*r[0]
#             l2,g2,s2,r2,n1_2,n2_2,n3_2 = 
#     return

def treasures(info, limit):
    l = int(limit*1000)
    g = [info['golden coin']['price'], info['golden coin']['weight'], info['golden coin']['amount']]
    s = [info['silver coin']['price'], info['silver coin']['weight'], info['silver coin']['amount']]
    r = [info['ruby']['price'], info['ruby']['weight'], info['ruby']['amount']]

    d = l
    for i in (g,s,r):
        d = gcd(d,i[1])
    l = int(l/d)
    g[1] = int(g[1]/d)
    s[1] = int(s[1]/d)
    r[1] = int(r[1]/d)

    result = np.zeros((g[2]+s[2]+r[2],l+1,4),dtype=int)
    for i in range(l+1):
        if i >= g[1]:
            result[(0,i,0)] = g[0]
            result[(0,i,1)] = 1

    for i in range(1,g[2]):
        for j in range(1,l+1):
            if j < g[1]:
                result[(i,j)] = result[(i-1,j)]
            elif result[(i-1,j,0)] < result[(i-1,j-g[1],0)]+g[0]:
                result[(i,j)] = result[(i-1,j-g[1])]
                result[(i,j,0)] += g[0]
                result[(i,j,1)] += 1
            else:
                result[(i,j)] = result[(i-1,j)]
    
    for i in range(g[2],g[2]+s[2]):
        for j in range(1,l+1):
            if j < s[1]:
                result[(i,j)] = result[(i-1,j)]
            elif result[(i-1,j,0)] < result[(i-1,j-s[1],0)]+s[0]:
                result[(i,j)] = result[(i-1,j-s[1])]
                result[(i,j,0)] += s[0]
                result[(i,j,2)] += 1
            else:
                result[(i,j)] = result[(i-1,j)]
    
    for i in range(g[2]+s[2],g[2]+s[2]+r[2]):
        for j in range(1,l+1):
            if j < r[1]:
                result[(i,j)] = result[(i-1,j)]
            elif result[(i-1,j,0)] < result[(i-1,j-r[1],0)]+r[0]:
                result[(i,j)] = result[(i-1,j-r[1])]
                result[(i,j,0)] += r[0]
                result[(i,j,3)] += 1
            else:
                result[(i,j)] = result[(i-1,j)]

    n1 = result[(-1,-1,1)]
    n2 = result[(-1,-1,2)]
    n3 = result[(-1,-1,3)]

    result_list = []
    if n1:
        result_list.append('golden coin: '+str(n1))
    if n2:
        result_list.append('silver coin: '+str(n2))
    if n3:
        result_list.append('ruby: '+str(n3))

    return result_list

if __name__ == '__main__':
    print("Example:")
    print(treasures({'golden coin': 
                        {'price': 100, 'weight': 50, 'amount': 200}, 
                     'silver coin': 
                        {'price': 10, 'weight': 20, 'amount': 1000}, 
                     'ruby': 
                        {'price': 1000, 'weight': 200, 'amount': 2}}, 5))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert treasures({'golden coin': 
                         {'price': 100, 'weight': 50, 'amount': 200}, 
                      'silver coin': 
                         {'price': 10, 'weight': 20, 'amount': 1000}, 
                      'ruby': 
                         {'price': 1000, 'weight': 200, 'amount': 2}}, 5) == [
                          'golden coin: 92', 'ruby: 2']
    assert treasures({'golden coin': 
                         {'price': 100, 'weight': 50, 'amount': 100}, 
                      'silver coin': 
                         {'price': 10, 'weight': 20, 'amount': 100}, 
                      'ruby': 
                         {'price': 1000, 'weight': 200, 'amount': 1}}, 7.5) == [
                          'golden coin: 100', 'silver coin: 100', 'ruby: 1']
    print("Coding complete? Click 'Check' to earn cool rewards!")
