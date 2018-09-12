from numpy import *
from math import *
a1 = mat([1,0,1])
a2 = mat([[1.807,0,0],[0,1.094,0],[0,0,2.082]])
a3 = mat([[-1],[0],[1]])
print(transpose(a1))
print(transpose(a3)*(a2*a3))
print(acos(0.275/3.889)/pi*180)