import numpy as np
from matplotlib import pyplot as plt
from copy import deepcopy
from math import exp,factorial,pi
from scipy.misc import factorial
from scipy.stats import poisson
from scipy.stats import norm
from scipy.stats import binom
from scipy.stats import chisquare
from scipy.stats import chi2_contingency
import random

a1 = np.array([[180,330],[168,614]])
a = chisquare(a1,ddof=1)
print(chi2_contingency(a1))

x = np.random.normal(0,1,100)
x_bar = np.average(x)
# print(x_bar)
# print(norm.cdf(-8.7,0,1))
# print(norm.ppf(0.05))
print(norm.cdf(-1.645,-5,1))
# print(1-norm.cdf(1.28,1,1))


h = []
for i in range(1000):
        x = abs(10*np.average(np.random.normal(5,1,100)))
        h.append(2*norm.cdf(-x,0,1))
plt.hist(h,density=True)
plt.xlabel('P-value')
plt.ylabel('Density')
plt.show()

# x = np.arange(-5,5,0.1)
# y1 = norm.pdf(x)
# y2 = norm.pdf(x,scale=2**0.5)

# hist1 = []
# hist2 = []
# fig, ax = plt.subplots(3,2)
# for i in range(1000):
#     a = np.random.normal(0,1,10)
#     hist1.append(np.mean(a)*10**0.5)
#     hist2.append((np.sum(np.power(a-np.mean(a),2))/len(a)-1)*10**0.5)
# ax[0][0].hist(hist1,bins=50,normed=True,label='theta1,n=10')
# ax[0][0].plot(x,y1,label='asymptotic')
# ax[0][1].hist(hist2,bins=50,normed=True,label='theta2,n=10')
# ax[0][1].plot(x,y2,label='asymptotic')

# for i in range(1000):
#     a = np.random.normal(0,1,100)
#     hist1.append(np.mean(a)*100**0.5)
#     hist2.append((np.sum(np.power(a-np.mean(a),2))/len(a)-1)*100**0.5)
# ax[1][0].hist(hist1,bins=50,normed=True,label='theta1,n=100')
# ax[1][0].plot(x,y1,label='asymptotic')
# ax[1][1].hist(hist2,bins=50,normed=True,label='theta2,n=100')
# ax[1][1].plot(x,y2,label='asymptotic')

# for i in range(1000):
#     a = np.random.normal(0,1,1000)
#     hist1.append(np.mean(a)*1000**0.5)
#     hist2.append((np.sum(np.power(a-np.mean(a),2))/len(a)-1)*1000**0.5)
# ax[2][0].hist(hist1,bins=50,normed=True,label='theta1,n=1000')
# ax[2][0].plot(x,y1,label='asymptotic')
# ax[2][1].hist(hist2,bins=50,normed=True,label='theta2,n=1000')
# ax[2][1].plot(x,y2,label='asymptotic')

# for i in ax:
#     for j in i:
#         j.legend()

# plt.show()
# a = np.random.uniform(0,10,100)
# a = np.random.uniform(0,10,1000)

# print(binom.cdf(60,100,0.5))
# print(norm.cdf(2.5*12**0.5))
# print(poisson.cdf(950,900))
# result = []
# for j in range(100):
#     a = 0
#     for i in range(1000):
#         a += exp(-random.uniform(0,2)**2/2)
#     result.append((2*pi)**-0.5*2/1000*a)

# fig = plt.figure()
# plt.hist(result)
# plt.show()





'''
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
'''