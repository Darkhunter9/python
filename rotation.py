from numpy import *
from math import *
x = 0
y = 0
z = 1
an = 2*pi*3/4
mat1 = mat([[cos(an)+(1-cos(an))*x**2, (1-cos(an))*x*y-sin(an)*z,(1-cos(an))*x*z+sin(an)*y],
    [(1-cos(an))*x*y+sin(an)*z,cos(an)+(1-cos(an))*y**2,(1-cos(an))*y*z-sin(an)*x],
    [(1-cos(an))*x*z-sin(an)*y,(1-cos(an))*z*y+sin(an)*x,cos(an)+(1-cos(an))*z**2]])
print(mat1)
mat2 = mat([[1,0,0],[0,-1,0],[0,0,1]])
print(mat1*mat2)