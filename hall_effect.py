# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 20:12:18 2025

@author: Trisha
HALL EFFECT: here u have to get the calibration curve first, I vs B . 
Then inceasing the current such the magnetic field increases, From known current the unknown magnetic
field can be determined. 3 sets table should be taken.
1. keeping the sample current constant --- increasing magnet current----hall voltage data record.
2. keeping the magnet current constant --- increasing the sample current(2 sets data 
 can be taken by inter-changing the connection )--- hall voltage data record.[changing current direction 
 helps to remove heating errors] 
3.keeping the 
"""
import numpy as np
import matplotlib.pyplot as plt
x=np.array([22.70,73.00,140.55,216.72,292.90,360.45,430.87,504.17,580.34])
y=np.array([6.4,7.2,8.2,9.8,11.0,12.3,13.1,14.0,15.1])
plt.scatter(x,y,marker='o',color='blue',label='data points')
# Linear fit (y = slope*x + intercept)
slope, intercept = np.polyfit(x, y, 1)
y_fit = slope * x + intercept
print(slope)
plt.scatter(x, y, color="blue")
plt.plot(x, y_fit, "r-", label="Fit:y=0.016x")
plt.ylabel("Hall Voltage in mV")
plt.xlabel("Magnetic field in X10 Gauss")
plt.title("Graph between hall voltage and magnetic field")
plt.legend(loc = 'best', prop = {'size':10})
plt.grid()
plt.show()



'''
# Data from the table
x = np.array([0.08,0.14,0.74,1.32,1.86,2.62,3.18,3.82,4.39])
y = np.array([9,12,96,185,265,390,464,555,604])

# Linear fit (y = slope*x + intercept)
slope, intercept = np.polyfit(x, y, 1)
y_fit = slope * x + intercept

# Plotting
plt.figure(figsize=(8,6))
plt.scatter(x, y, color="blue")
plt.plot(x, y_fit, "r-", label=f"Fit: y = {slope:.3f}x + {intercept:.3f}")

plt.xlabel("Current in Amp")
plt.ylabel("Magnetic field in X10 Gauss")
plt.title("Calibration Curve between Current and Magnetic Field")
plt.grid(True)
plt.legend()
plt.show()


print(f"Slope ={slope:.4f}")

# Equation coefficients from fit
m = 143.723
c = -3.174

# Example: new x values
x_new = np.array([0.12, 0.50, 1.02, 1.5,2.01, 2.50, 3.04, 3.53, 4.06 ]) # <-- replace with your values

# Compute y values
y_new = m * x_new + c

# Display results
for xi, yi in zip(x_new, y_new):
    print(f"x = {xi:.2f} -> y = {yi:.2f}")
'''
