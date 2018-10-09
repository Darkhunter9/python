def aline(A,B,C):
    return (C[1]-B[1])*(B[0]-A[0]) == (B[1]-A[1])*(C[0]-B[0])

def eigen(A,B):
    return [B[1]-A[1],A[0]-B[0],B[0]*A[1]-A[0]*B[1]]

def checkio(cakes):
    result = []
    for i in range(0,len(cakes)-2):
        for j in range(i+1,len(cakes)-1):
            for k in range(j+1,len(cakes)):
                if aline(cakes[i],cakes[j],cakes[k]):
                    result.append(eigen(cakes[i],cakes[j]))
    
    for i in range(len(result)):
        if result[i][0] != 0:
            result[i] = [1,result[i][1]/result[i][0],result[i][2]/result[i][0]]
        else:
            result[i] = [0,1,result[i][2]/result[i][1]]
    
    finalresult = []
    for i in result:
        if i not in finalresult:
            finalresult.append(i)
    return len(finalresult)
            


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2
    assert checkio(
        [[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2],
         [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6