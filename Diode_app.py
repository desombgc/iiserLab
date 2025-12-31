# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 20:26:23 2025

@author: Trisha
"""

import numpy as np
import matplotlib.pyplot as plt
pnx=np.array([0.03,0.08,0.10,0.20,0.24,0.26,0.28,0.30,0.32,0.35,0.40])
pny=np.array([0.00,0.00,0.00,0.03,0.07,0.10,0.23,0.53,0.95,1.51,2.82])
plt.xlabel("Voltage in Volts")
plt.ylabel("Current in mA")
plt.scatter(pnx,pny,color="blue", label="data points")
plt.plot(pnx,pny,"r-")
plt.title("p-n diode in Forward Bias Condition")
plt.legend(loc = 'best', prop = {'size':10})
plt.grid()
plt.show()
Zx=np.array([-0.02,-2.50,-3.70,-6.40,-8.30,-10.50,-11.80,-12.25,-12.30,-12.35,-12.50,-12.55,-12.70])
Zy=np.array([-0.00,-0.00,-0.00,-0.00,-0.00,-0.00,-0.00,-0.02,-0.80,-5.30,-12.00,-16.80,-29.30])
plt.xlabel("Voltage in Volts")
plt.ylabel("Current in mA")
plt.scatter(Zx,Zy,color="red",marker='^',label="data points")
plt.plot(Zx,Zy,"b-")
plt.legend(loc = 'best', prop = {'size':10})
plt.title("Zener diode in Reverse Bias Condition")
plt.grid()
plt.show()
Vz=15.0
Vs=np.array([0.01,0.03,1.06,2.12,3.19,5.45,6.82,8.10,9.50,10.60,11.03,12.34,12.86,13.70,14.20])
VL=np.array([0.007,0.018,0.59,1.09,1.63,2.90,3.70,4.20,5.20,5.75,6.03,6.84,7.40,7.50,7.52])
plt.xlabel("Given Voltage in Volts")
plt.ylabel("Load Voltage in Volts")
plt.scatter(Vs,VL,color="red",label="data points")
plt.plot(Vs,VL,"b--")
#plt.axhline(y=6.74, color='r', linestyle='--')
plt.axhline(y=VL[np.argmin(np.abs(Vs - Vz))], color='r', linestyle='-', linewidth=1)
plt.title("Zener diode as a Voltage Regulator")
plt.legend(loc = 'best', prop = {'size':10})
plt.grid()
plt.show()