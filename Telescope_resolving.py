# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 20:09:26 2025

@author: SOMNATH
"""
import numpy as np
import matplotlib.pyplot as plt

# Data from the table
x = np.array([2.5, 3.3, 3.3, 5.0, 6.6, 10.0, 13.3])
y = np.array([0.00025, 0.00027, 0.00035, 0.00039, 0.00049, 0.00065, 0.00074])

# Linear fit (y = slope*x + intercept)
slope, intercept = np.polyfit(x, y, 1)
y_fit = slope * x + intercept
print(slope)
# Plotting
plt.figure(figsize=(8,6))
plt.xlabel("g/D")
plt.ylabel("λ/A")
plt.title("Resolving Power of Telescope")
plt.scatter(x, y, color="blue")
plt.plot(x, y_fit, "r-", label="Fit y=0.50x")
plt.legend(loc = 'best', prop = {'size':10})
plt.grid()

plt.show()
