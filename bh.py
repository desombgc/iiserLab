# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 15:15:19 2025

@author: SOMNATH
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# --- Experimental data ---
B = np.array([0,59, 95, 136, 177, 223, 268, 311, 348])  # Magnetic Field (gauss)
W = np.array([0,8, 10, 12, 14, 16, 18, 18, 20])          # Loop Width (mm)

# --- Nonlinear model (saturation-type) ---
def saturation_model(B, a, b, c):
    return a * (1 - np.exp(-B / b)) + c

# Fit the data
popt, _ = curve_fit(saturation_model, B, W, p0=[15, 100, 0])

# --- Linear fit for higher field region (roughly B > 150 gauss) ---
mask = B > 150
coeffs = np.polyfit(B[mask], W[mask], 1)
linear_fit = np.poly1d(coeffs)
# --- Extrapolate linear fit back to B = 0 ---
B_lin_ext = np.linspace(0, max(B), 200)   # full x-range
W_lin_ext = linear_fit(B_lin_ext)

# --- Plot ---
plt.figure(figsize=(7, 5))
plt.scatter(B, W, color='k', label='Experimental Data', zorder=5)
plt.plot(B, saturation_model(B, *popt), 'b-', lw=2, label='Nonlinear Fit')
#plt.plot(B[mask], linear_fit(B[mask]), 'r--', lw=2, label='Linear Fit (High Field)')
plt.plot(B_lin_ext, W_lin_ext, 'r--', lw=2,label='Linear Fit (Extrapolated)')

# --- Labels and style ---
plt.xlabel('Magnetic Field (gauss)', fontsize=12)
plt.ylabel('Loop Width (mm)', fontsize=12)
plt.title('Dependence of Loop Width on Magnetic Field', fontsize=13)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()


# --- Experimental data ---
B = np.array([59, 95, 136, 177, 223, 268, 311, 348])  # Magnetic Field (gauss)
Intercept_2x = np.array([8, 8, 10, 10, 12, 12, 12, 12])  # (a) 2× Intercept (mV)
TipToTip = np.array([8, 10, 12, 14, 15, 18, 18, 20])     # (b) Tip-to-Tip Height (mV)

# --- Saturation-type model function ---
def sat_model(B, a, b, c):
    return a * (1 - np.exp(-B / b)) + c

# Fit both data sets
popt_a, _ = curve_fit(sat_model, B, Intercept_2x, p0=[15, 100, 0])
popt_b, _ = curve_fit(sat_model, B, TipToTip, p0=[20, 100, 0])

# Smooth field values for fitted curves
B_fit = np.linspace(0, 360, 300)

# --- Plot ---
plt.figure(figsize=(7, 5))

# (a) 2× Intercept
plt.scatter(B, Intercept_2x,color="blue", label='2× Intercept (a)')
plt.plot(B_fit, sat_model(B_fit, *popt_a), 'k-', lw=2)

# (b) Tip-to-Tip Height
plt.scatter(B, TipToTip,color="blue", label='Tip-to-Tip Height (b)')
plt.plot(B_fit, sat_model(B_fit, *popt_b), 'k-', lw=2)

# Labels (a) and (b)
plt.text(340, 13, '(a)', fontsize=12)
plt.text(340, 21, '(b)', fontsize=12)

# --- Axes and formatting ---
plt.xlabel('Magnetic Field (gauss)', fontsize=12)
plt.ylabel('BH Loop Parameters (mV)', fontsize=12)
plt.title('Dependence of (a) Twice the Intercept and (b) Tip-to-Tip Height\non Magnetic Field', fontsize=12)
plt.xlim(0, 360)
plt.ylim(0, 22)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

plt.show()
