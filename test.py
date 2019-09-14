import numpy as np
from matplotlib import pyplot as plt
from copy import deepcopy
from math import exp,factorial
from scipy.misc import factorial
from scipy.stats import poisson

# generate 1000 pairs of points
a = np.random.uniform(low=0.0, high=10.0, size=(1000,2))

# count the number in each square
b = np.floor(a).astype('int')
count = np.zeros((10,10), dtype=int)
for i in range(len(b)):
    count[(b[(i,0)],b[(i,1)])] += 1

temp = '   \t|'
print('-'*100)
for i in range(10):
    temp += str(i+1)+'\t|'
print(temp)
print('-'*100)
for i in range(10):
    temp = str(i+1)+'\t|'
    for j in range(10):
        temp += str(count[(j,i)]) + '\t|'
    print(temp)
    print('-'*100)

his = np.histogram(count, bins=np.arange(0,np.max(count)+1))
pos = [exp(-2)*2**i/factorial(i) for i in his[1]]
for i in his[1]:
    print(pos[i],poisson.pmf(i,2))


fig = plt.figure()
plt.plot(his[1], np.concatenate((his[0],np.array([0])))/np.sum(his[0]), label='histogram')
plt.plot(his[1], [poisson.pmf(i,10) for i in his[1]], label='poisson')
plt.legend(loc='upper right')
plt.show()

plt.cla()
plt.axis('equal')
plt.scatter(x=a[:,0], y=a[:,1], s=5)
plt.show()