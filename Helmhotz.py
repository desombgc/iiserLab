# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 20:29:02 2025

@author: Trisha
"""

import numpy as np
import matplotlib.pyplot as plt
Hx=np.linspace(53,80,28)
AHx=np.linspace(41,66,26)
B_helm= [7.3,8.1,9.0,9.8,10.6,11.3,11.9,12.4,12.7,12.8,12.9,12.9,12.8,12.8,12.8,12.7,12.5,12.2,11.5,11.0,10.2,9.4,8.5,7.5,6.6,5.8,5.0,4.2]
AB_helm=[3.5,4.0,4.5,4.9,5.3,5.5,5.5,5.3,4.8,4.0,3.2,1.9,0.7,-0.3,-1.5,-2.7,-3.8,-4.6,-5.2,-5.5,-5.6,-5.5,-5.2,-4.8,-4.2,-3.6]
I=[0,18,56,108,161,208,258,303,355,403]
B1=[1.0,0.2,-1.0,-2.7,-4.4,-6.0,-7.5,-8.9,-10.3,-11.7]
#B2=[1.2,1.4,1.7,2.0,2.3,2.7,3.1,3.6,4.1,4.8,5.4,6.0,6.7,7.3,8.0,8.9,9.2] #9.1,8.9,8.5,8.4,8.0,7.4,6.7,6.1,5.4,4.8,4.3 ,3.9,3.4,3.0,2.4,2.2,2.0,1.8,1.6,1.5
#X=[1.53,1.58,1.64,1.70,1.76,1.83,1.89,1.97,2.04,2.12,2.26,2.29,2.38,2.48,2.58,2.69,2.81] #2.93,3.05,3.19,3.33,3.49,3.65,3.82,4.00,4.12,4.40,4.62
I2=[0,16,55,110,172,205,253,305,358,405]
b2=[-0.5,0.1,1.4,3.1,5.2,6.3,8.1,9.7,11.3,12.5]
slope1=np.polyfit(I,B1,deg=1)
slope2=np.polyfit(I2,b2,deg=1)
print(slope2)
plt.plot(I2,b2,color='green',marker='o',label='Fit: y=0.033x-0.46')
plt.xlabel('Current in mA')
plt.ylabel('Magnetic field in Gauss')
plt.title("Plot for the Coil 1")
plt.legend(loc = 'best', prop = {'size':10})
plt.grid()
plt.show()
print(slope1)
plt.plot(I,B1,color='magenta',marker='o',label='Fit:y=-0.031x+0.75')
plt.xlabel('Current in mA')
plt.ylabel('Magnetic field in Gauss')
plt.title("Plot for the Coil 2")
plt.legend(loc = 'best', prop = {'size':10})
plt.grid()
plt.show()
#print(len(AHx))
#print(len(AB_helm))
#print(AHx)
plt.scatter(Hx,B_helm,marker='^',color='blue',label='Helmhotz Configurataion')
plt.scatter(AHx,AB_helm,marker='o',color='red',label='Anti-Helmhotz Configurataion')
plt.plot(Hx,B_helm,color="red")
plt.plot(AHx,AB_helm,color="blue")
plt.xlabel('Position of the gauss probe in cm')
plt.ylabel('Magnetic Field in Gauss')
plt.legend(loc = 'best', prop = {'size':10})
plt.xlim(40,85)
plt.ylim(-6,14)
plt.grid()
plt.show()