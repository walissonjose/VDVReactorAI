# This code implements a numerical solution to the system of differential equations
# that describe the chemical kinetics of the van der Vusse reaction in a chemical reactor. 
# The chemical reaction is given by:
# 2 A --> B
# B + C --> 2 C
# A --> D
# The code uses numerical finite difference solution to calculate the concentrations 
# of reactants and products as a function of time. The reaction rate constants and 
# other properties of the system are defined at the beginning of the code, along with 
# the initial conditions for the concentrations and reactor volume.
# The final result is a plot of the evolution of the concentrations of each chemical 
# species as a function of time, using the matplotlib library for data visualization. 
# The concentrations are plotted in different colors to facilitate distinction.

import matplotlib.pyplot as plt

import pandas as pd

plt.style.use('seaborn-poster')

# Constants
k1 = 10
k2 = 1
k3 = 0.5
A = 5
Cv = 7 

# Start concentrations of components 
Ca0 = 0.6
Cb0 = 0
Cc0 = 0 
Cd0 = 0 

# Volumetric flow rate
Fvol0 = 0.00278 #m^3/s

# Isothermic and isobaric
T = 550
P = 1

# Reactor level
h0 = 0.5 

# Definition of steps
ts = 0.001
te = 10

tf = 8000
V = []
h = []
Ca = []
Cb = []
Cc = []
Cd = []
time = []

V.append(h0*A)
h.append(h0)
Ca.append(Ca0)
Cb.append(Cb0)
Cc.append(Cc0)
Cd.append(Cd0)
time.append(0)

# Equations Iteration
for t in range(tf-1):
    Ca.append(Ca[t] + ts*((Fvol0*Ca0)/V[t] - (Fvol0*Ca[t])/V[t] - k1*Ca[t] - (2*k3*(Ca[t])**2)))
    Cb.append(Cb[t] + ts*((Fvol0*Cb0)/V[t] - (Fvol0*Cb[t])/V[t] + (k1*Ca[t]) - (k2*Cb[t])))
    Cc.append(Cc[t] + ts*((Fvol0*Cc0)/V[t] - (Fvol0*Cc[t])/V[t] + (k2*Cb[t])))
    Cd.append(Cd[t] + ts*((Fvol0*Cd0)/V[t] - (Fvol0*Cd[t])/V[t] + (k3*Ca[t]**2)))
    h.append(h[t] + ts*(Fvol0/A - Cv*(h[t])**1.5/A))
    V.append(h[t]*A)
    time.append(time[t] + ts)
    
plt.figure(figsize = (12, 8))
plt.plot(time, Ca, 'bo--', label='Approximate', color = 'green')
plt.plot(time, Cb, 'bo--', label='Approximate', color = 'purple')
plt.plot(time, Cc, 'bo--', label='Approximate', color = 'blue')
plt.plot(time, Cd, 'bo--', label='Approximate', color = 'orange')
plt.show()

# Create dataframe with the variables of interest
df = pd.DataFrame({'time': time, 'Ca': Ca, 'Cb': Cb, 'Cc': Cc, 'Cd': Cd})

# Save data frame to a .csv file
df.to_csv('registros.csv', index=False)
