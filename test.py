import datetime
import random
import re
from copy import deepcopy
from math import acos, asin, atan, atan2, cos, log, pi, sin, tan

import matplotlib.pyplot as plt
import numpy as np
from pyquaternion import Quaternion


def get_key (dict, value):
    return [k for k, v in dict.items() if v == value]

databook = []
rotation = []
symmetry = []
diad = []

# print(type(databook))
f = open('HW3-quaternions.txt', 'r+')
pattern = r'0.[0-9]+|-0.[0-9]+'

for i in f.readlines():
    temp = []
    temp = re.findall(pattern, i)
    if temp:
        for j in range(4):
            temp[j] = float(temp[j])
        databook.append(temp)

total = len(databook)
print('length:', total)
f.close()

for i in range(total):
    temp = Quaternion(databook[i])
    rotation.append(np.linalg.inv(temp.rotation_matrix))
    # print(np.dot(np.linalg.inv(temp.rotation_matrix), temp.rotation_matrix))

f = open('cubic-matrices.txt')
pattern0 = r'samp\_e\(\:'
pattern1 = r'e\(\:\,'
pattern2 = r'\[.*\]'
for i in f.readlines():
    if re.match(pattern0, i):
        temp = re.search(pattern2, i).group(0)[1:-1]
        diad.append(np.matrix(temp))
    elif re.match(pattern1, i):
        temp = re.search(pattern2, i).group(0)[1:-1]
        symmetry.append(np.matrix(temp))
        # print(symmetry[-1])

# [100]
pole1 = np.matrix([[1],[0],[0]])
polefigure1 = []
for i in range(24):
    pole = np.matmul(symmetry[i], pole1)
    for j in range(total):
        temp = np.matmul(rotation[j], pole)
        hx = temp[0,0]
        hy = temp[1,0]
        hz = temp[2,0]
        theta = acos(hz)
        phi = atan2(hy,hx)
        if (tan(theta/2)*cos(phi))**2 + (tan(theta/2)*sin(phi))**2 <= 1.0:
            polefigure1.append([tan(theta/2)*cos(phi), tan(theta/2)*sin(phi)])

# [110]
pole2 = np.matrix([[1/2**0.5],[1/2**0.5],[0]])
polefigure2 = []
for i in range(24):
    pole = np.matmul(symmetry[i], pole2)
    for j in range(total):
        temp = np.matmul(rotation[j], pole)
        hx = temp[0,0]
        hy = temp[1,0]
        hz = temp[2,0]
        theta = acos(hz)
        phi = atan2(hy,hx)
        if (tan(theta/2)*cos(phi))**2 + (tan(theta/2)*sin(phi))**2 <= 1.0:
            polefigure2.append([tan(theta/2)*cos(phi), tan(theta/2)*sin(phi)])

# [111]
pole3 = np.matrix([[1/3**0.5],[1/3**0.5],[1/3**0.5]])
polefigure3 = []
for i in range(24):
    pole = np.matmul(symmetry[i], pole3)
    for j in range(total):
        temp = np.matmul(rotation[j], pole)
        hx = temp[0,0]
        hy = temp[1,0]
        hz = temp[2,0]
        theta = acos(hz)
        phi = atan2(hy,hx)
        if (tan(theta/2)*cos(phi))**2 + (tan(theta/2)*sin(phi))**2 <= 1.0:
            polefigure3.append([tan(theta/2)*cos(phi), tan(theta/2)*sin(phi)])

# PF
degree = np.linspace(0, 2*np.pi,800)
x,y = np.cos(degree), np.sin(degree)

figure1 = plt.figure(figsize=(6,6))
plt.title('[100]')
plt.axis('equal')
plt.xlabel('p_x')
plt.ylabel('p_y')
plt.scatter([x[0] for x in polefigure1], [x[1] for x in polefigure1], s=2)
plt.plot(x, y, color='black', linewidth=2.0)
plt.show()

figure2 = plt.figure(figsize=(6,6))
plt.title('[110]')
plt.axis('equal')
plt.xlabel('p_x')
plt.ylabel('p_y')
plt.scatter([x[0] for x in polefigure2], [x[1] for x in polefigure2], s=2)
plt.plot(x, y, color='black', linewidth=2.0)
plt.show()

figure2 = plt.figure(figsize=(6,6))
plt.title('[111]')
plt.axis('equal')
plt.xlabel('p_x')
plt.ylabel('p_y')
plt.scatter([x[0] for x in polefigure3], [x[1] for x in polefigure3], s=2)
plt.plot(x, y, color='black', linewidth=2.0)
plt.show()

print('completed')