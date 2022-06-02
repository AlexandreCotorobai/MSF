# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 02:09:01 2022

@author: Alexandre
"""


import matplotlib.pyplot as plt
import numpy as np

dt = 0.01
g = 9.8
v0 = 100/3.6
ang = 10/180*np.pi
m = 57/1000
t = np.arange(0,10+dt,dt)

x0 = 0
y0 = 0
vx0 = v0*np.cos(ang)
vy0 = v0*np.sin(ang)

Em0 = m*g*y0 + 0.5*m*v0**2

vt = 100/3.6
D = g / vt**2

x = np.zeros(t.size)
y = np.zeros(t.size)
vx = np.zeros(t.size)
vy = np.zeros(t.size)
Em = np.zeros(t.size)
W = np.zeros(t.size)

x[0] = x0
y[0] = y0
vx[0] = vx0
vy[0] = vy0
Em[0] = Em0
W[0] = 0
 
print("No instante: Inicial -> Em: " + str(Em0))
#metodo de Euler
for i in range(0, t.size-1):
    v = np.sqrt(vx[i]**2+vy[i]**2)
    
    ax = - D * vx[i] * v
    ay = - g - D * vy[i] * v
    ay2 = - D * vy[i] * v
    
    vx[i+1] = vx[i] + ax * dt # velocidade no instante
    vy[i+1] = vy[i] + ay * dt # velocidade no instante
    x[i+1] = x[i] + vx[i] * dt # posiçao no instante
    y[i+1] = y[i] + vy[i] * dt # posiçao no instante
    v = np.sqrt(vx[i+1]**2+vy[i+1]**2)
    
    Em[i+1] = m*g*y[i+1] + 0.5*m*v**2
    W[i+1] = 0.5*m*(v-v0)**2 - 
    #print("No instante: " + str(i+1) + " -> Em: " + str(Em[i+1]))
#    if y[i+1] < 0:
#        break
 
t = t[:i+2]
x = x[:i+2]
y = y[:i+2]
vx = vx[:i+2]
vy = vy[:i+2]
Em = Em[:i+2]
 
 
plt.xlim([0,1])
plt.plot(t, W)
plt.xlabel("Tempo")
plt.ylabel("Trabalho")
 
 
print("em t0:", str(W[np.where(t == 0)]))
print("em t1:", str(W[np.where(t == 0.4)]))
print("em t2:", str(W[np.where(t == 0.8)]))
plt.grid()
plt.legend()