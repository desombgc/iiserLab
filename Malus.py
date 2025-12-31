# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 20:05:26 2025

@author: SOMNATH
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.array([0.000,0.030,0.116,0.250,0.413,0.586,0.750,0.883,0.969,1.000])
y=np.array([0.2,0.7,1.5,4.3,7.6,10.8,12.8,13.5,14.2,14.8])
Y=np.array([0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360])
X=np.array([14.8,14.2,13.5,12.8,10.8,7.6,4.3,1.5,0.7,0.2,1.7,4.8,8.5,10.7,12.8,13.5,13.9,14.2,14.6,14.1,13.8,13.2,12.1,9.2,5.0,1.7,0.1,0.3,2.2,5.8,9.5,12.0,13.3,13.9,14.2,14.3,14.8])
# Linear fit (y = slope*x + intercept)
slope, intercept = np.polyfit(x, y, 1)
plt.xlabel("$cos^2(θ)$")
plt.ylabel("Intensity")
plt.scatter(x, y, color="blue", label="data points")
y_fit = slope * x + intercept
plt.plot(x, y_fit, "r-",)
plt.title("Intensity vs $cos^2(θ)$")
plt.legend(loc = 'best', prop = {'size':10})
plt.grid()
#plt.plot(X,Y)
plt.show()
plt.xlabel("angle$(θ)$")
plt.ylabel("Intensity")
plt.scatter(Y,X ,color="blue", label="data points")
#y_fit = slope * x + intercept
plt.plot(Y,X, "r-",)
plt.title("Intensity vs angle$(θ)$")
plt.legend(loc = 'best', prop = {'size':10})
plt.grid()
plt.show()

