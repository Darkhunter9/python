import re
import numpy as np
from copy import deepcopy

zero_array = np.zeros((10,), dtype=int)
init_array = np.zeros((10,), dtype=int)
init_array[0] = 1

def dealplus(expr):
    tempexpr = expr
    temp = ''
    calculatelist = []

    while (tempexpr or temp):
        if (not tempexpr) and temp:
            calculatelist.append(temp)
            temp = ''
        elif tempexpr[0] in '-+' and temp and temp.count('(') == temp.count(')'):
            calculatelist.append(temp)
            temp = ''
        else:
            temp += tempexpr[0]
            tempexpr = tempexpr[1:]
        
    for i in range(len(calculatelist)):
        if not calculatelist[i][0] in '-+':
            calculatelist[i] = '+'+calculatelist[i]
    
    return calculatelist

def dealmulti(expr, result):
    MULTI = False
    if expr[0] == '-':
        minus = -1
    else:
        minus = 1

    tempexpr = expr[1:]
    temp = ''
    elements = []
    while (tempexpr or temp):
        if (not tempexpr) and temp:
            elements.append(temp)
            temp = ''
        elif tempexpr[0] == '*' and temp and temp.count('(') == temp.count(')'):
            elements.append(temp)
            temp = ''
            tempexpr = tempexpr[1:]
        else:
            temp += tempexpr[0]
            tempexpr = tempexpr[1:]

    tempresult = deepcopy(result)

    for i in elements:
        if '(' not in i:
            MULTI = True
            if i.isnumeric():
                tempresult *= int(i)
            else:
                tempresult = np.append(np.array([0]), tempresult)[:-1]

    if (not MULTI) and np.array_equal(tempresult,deepcopy(init_array)):
        tempresult = deepcopy(zero_array)
        i = elements.pop()
        elements2 = dealplus(i[1:-1])
        for j in elements2:
            tempresult += dealmulti(j, deepcopy(init_array))

    tempresult2 = deepcopy(zero_array)

    while elements:
        i = elements.pop()
        if '(' in i:
            elements2 = dealplus(i[1:-1])
            for j in elements2:
                tempresult2 += dealmulti(j,tempresult)
            tempresult = deepcopy(tempresult2)
            tempresult2 = deepcopy(zero_array)
    return minus*tempresult

def simplify(expr):
    calculatelist = dealplus(expr)
    # print(calculatelist)
    
    finalresult = deepcopy(zero_array)
    expr_result = ''

    for i in calculatelist:
        finalresult += dealmulti(i, deepcopy(init_array))
        
    for i in range(len(finalresult)-1,1,-1):
        if finalresult[i] == 1:
            expr_result += '+x**' + str(i)
        elif finalresult[i] == -1:
            expr_result += '-x**' + str(i)
        else:
            if finalresult[i] > 0:
                expr_result += '+' + str(finalresult[i]) + '*x**' + str(i)
            elif finalresult[i] < 0:
                expr_result += str(finalresult[i]) + '*x**' + str(i)

    if finalresult[1] == 1:
        expr_result += '+x'
    elif finalresult[1] == -1:
        expr_result += '-x'
    else:
        if finalresult[1] > 0:
            expr_result += '+' + str(finalresult[1]) + '*x'
        elif finalresult[1] < 0:
            expr_result += str(finalresult[1]) + '*x'

    if finalresult[0] > 0:
        expr_result += '+' + str(finalresult[0])
    elif finalresult[0] < 0:
        expr_result += str(finalresult[0])

    if not expr_result:
        return '0'
    if expr_result[0] == '+':
        expr_result = expr_result[1:]
    return expr_result

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # print(simplify(u"98*85*x*(x-x-(x*(x-41-(x)+3-31+(41)*54*13-x+(x))))"))
    assert simplify("(x-1)*(x+1)") == "x**2-1", "First and simple"
    assert simplify("(x+1)*(x+1)") == "x**2+2*x+1", "Almost the same"
    assert simplify("(x+3)*x*2-x*x") == "x**2+6*x", "Different operations"
    assert simplify("x+x*x+x*x*x") == "x**3+x**2+x", "Don't forget about order"
    assert simplify("(2*x+3)*2-x+x*x*x*x") == "x**4+3*x+6", "All together"
    assert simplify("x*x-(x-1)*(x+1)-1") == "0", "Zero"
    assert simplify("5-5-x") == "-x", "Negative C1"
    assert simplify("x*x*x-x*x*x-1") == "-1", "Negative C0"
