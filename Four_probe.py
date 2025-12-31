# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 20:25:36 2025

@author: SOMNATH 
"""

import numpy as np
import matplotlib.pyplot as plt
Y=[0.103,0.200,0.310,0.434,0.543,0.690,0.810,0.930,1.04,1.134,1.210,1.231,1.244]
X=[2.392,2.451,2.513,2.577,2.646,2.717,2.793,2.874,2.959,3.049,3.145,3.247,3.356]
s1=np.gradient(Y,X)
#print(s1)
R=[78,75.2,70.0,60.0,48.0,37.2,28.2,21.4,15.4,12.0,9.0,7.0,5.6]
T=[298,308,318,328,338,348,358,368,378,388,398,408,418]
#print(slope)
plt.xlim(2,4)
plt.ylim(0,1.5)
plt.scatter(X,Y, marker='o',color='red',label='Data Points')
plt.xlabel("$T^{-1}$ X 1000")
plt.ylabel("$log_{10}(ρ)$")
plt.title("Graph between $T^{-1}$ and $log_{10}(ρ)$")
plt.plot(X,Y,label='For the linear region slope is 1.76')
plt.legend(loc = 'best', prop = {'size':10})
plt.grid()
plt.show()
plt.plot(T,R,marker='*',markersize='5',ls='-',label='Data Points')
plt.xlabel("Temperature in Kelvin",fontsize=10)
plt.ylabel("Resistance in Ohm",fontsize=10)
plt.title("Resistance Vs Temperature")
plt.grid()

plt.show()
