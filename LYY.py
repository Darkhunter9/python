"""
6万本金
X = 3, 3.5, 4, 4.5, 5, 5.5 
2万保证金
连跌3天买入一半
连跌5天买入另外一半
360days
连涨3天，取出一半
6个随机涨幅：-0.8, -1.5, -3.5, +1.2, +1.9, +4.0%
"""

from random import randint

time = 1000
result = [0,0,0,0]
for k in range(time):
    # stock record for 360 days
    plist = [-3.5, -1.5, -0.8, 1.2, 1.9, 4.0]
    stock = []
    for i in range(360):
        stock.append(plist[randint(0,len(plist)-1)])
    # print(stock)

    #strategy 1
    s1 = [60000]
    for i in range(360):
        temp = s1[-1]*(1+stock[i]/100.0)
        s1.append(temp)
    # print(s1)

    # strategy 2
    X = 30000
    deposit_0 = 60000-X
    deposit = 60000-X
    amount = deposit_0/2.0
    s2 = [X+deposit]
    for i in range(360):
        temp = (s2[-1]-deposit)*(1+stock[i]/100.0)
        #judge whether to deposit or withdraw
        if (i >= 2 and all(stock[j] < 0 for j in [i,i-1,i-2])):
            if deposit > 0:
                deposit -= amount
                temp += amount
        if (i >= 2 and all(stock[j] > 0 for j in [i,i-1,i-2])):
            if deposit < deposit_0:
                deposit += amount
                temp -= amount
        s2.append(temp+deposit)
    # print(s2)

    # strategy 3
    X = 35000
    deposit_0 = 60000-X
    deposit = 60000-X
    amount = deposit_0/2.0
    s3 = [X+deposit]
    for i in range(360):
        temp = (s3[-1]-deposit)*(1+stock[i]/100.0)
        #judge whether to deposit or withdraw
        if (i >= 2 and all(stock[j] < 0 for j in [i,i-1,i-2])):
            if deposit > 0:
                deposit -= amount
                temp += amount
        if (i >= 2 and all(stock[j] > 0 for j in [i,i-1,i-2])):
            if deposit < deposit_0:
                deposit += amount
                temp -= amount
        s3.append(temp+deposit)
    # print(s3)

    # strategy 4
    X = 40000
    deposit_0 = 60000-X
    deposit = 60000-X
    amount = deposit_0/2.0
    s4 = [X+deposit]
    for i in range(360):
        temp = (s4[-1]-deposit)*(1+stock[i]/100.0)
        #judge whether to deposit or withdraw
        if (i >= 2 and all(stock[j] < 0 for j in [i,i-1,i-2])):
            if deposit > 0:
                deposit -= amount
                temp += amount
        if (i >= 2 and all(stock[j] > 0 for j in [i,i-1,i-2])):
            if deposit < deposit_0:
                deposit += amount
                temp -= amount
        s4.append(temp+deposit)
    # print(s4)

    # strategy 5
    X = 45000
    deposit_0 = 60000-X
    deposit = 60000-X
    amount = deposit_0/2.0
    s5 = [X+deposit]
    for i in range(360):
        temp = (s5[-1]-deposit)*(1+stock[i]/100.0)
        #judge whether to deposit or withdraw
        if (i >= 2 and all(stock[j] < 0 for j in [i,i-1,i-2])):
            if deposit > 0:
                deposit -= amount
                temp += amount
        if (i >= 2 and all(stock[j] > 0 for j in [i,i-1,i-2])):
            if deposit < deposit_0:
                deposit += amount
                temp -= amount
        s5.append(temp+deposit)
    # print(s5)

    # strategy 6
    X = 50000
    deposit_0 = 60000-X
    deposit = 60000-X
    amount = deposit_0/2.0
    s6 = [X+deposit]
    for i in range(360):
        temp = (s6[-1]-deposit)*(1+stock[i]/100.0)
        #judge whether to deposit or withdraw
        if (i >= 2 and all(stock[j] < 0 for j in [i,i-1,i-2])):
            if deposit > 0:
                deposit -= amount
                temp += amount
        if (i >= 2 and all(stock[j] > 0 for j in [i,i-1,i-2])):
            if deposit < deposit_0:
                deposit += amount
                temp -= amount
        s6.append(temp+deposit)
    # print(s6)

    # strategy 7
    X = 55000
    deposit_0 = 60000-X
    deposit = 60000-X
    amount = deposit_0/2.0
    s7 = [X+deposit]
    for i in range(360):
        temp = (s7[-1]-deposit)*(1+stock[i]/100.0)
        #judge whether to deposit or withdraw
        if (i >= 2 and all(stock[j] < 0 for j in [i,i-1,i-2])):
            if deposit > 0:
                deposit -= amount
                temp += amount
        if (i >= 2 and all(stock[j] > 0 for j in [i,i-1,i-2])):
            if deposit < deposit_0:
                deposit += amount
                temp -= amount
        s7.append(temp+deposit)
    # print(s7)

    result[0] += s1[-1]
    result[1] += s2[-1]
    result[2] += s4[-1]
    result[3] += s6[-1]

for i in range(len(result)):
    result[i] /= time
print(result)

'''
# output
print("days","\t", "s1", "\t\t","s2")
for i in range(361):
    # print(i,"\t",round(s1[i]),"\t",round(s2[i]),"\t",round(s3[i]),"\t",round(s4[i]),"\t",round(s5[i]),"\t",round(s6[i]),"\t",round(s7[i]))
    print(i,"\t",round(s1[i]),"\t",round(s2[i]),"\t",round(s4[i]),"\t",round(s6[i]))
'''