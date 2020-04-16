# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 14:56:34 2020

@author: Sudhish Kumar
"""

import os
import matplotlib.pyplot as plt
import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def elliptic_curve(x,a,b):
    try:
        y=[v*math.sqrt(x**3+a*x**2+bx+c) for v in [1,-1]]
    except:
        y=[0,0]
    return y
a=486662
b=1
c=0

x=np.linspace(-100,200,10000)
y1=[elliptic_curve(v,a,b)[0] for v in x]

y2=[elliptic_curve(v,a,b)[1] for v in x]


fig = plt.figure()
plt.plot(x,y1)
plt.plot(x,y2)
#plt.axis([-2, 3,-3,3])
plt.show()
