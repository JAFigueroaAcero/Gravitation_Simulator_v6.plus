# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 20:50:10 2021

@author: Juan Antonio

Title: Gravitación sim

ver: 3.0
"""
import matplotlib.pyplot as plt
import functions as f
import numpy as np
G = 6.67 * (10**-11)
m = 5.972 * (10**24)
t = 0
vi = 11190
vf = 0
a = 2
h = 1
yi = 6371000
y = yi + h
r = 0
dt = 0.001


listay = list()
listav = list()
listat = list()
print(y)
print(np.sin(f.angulo_frac2rad(0, y)))
while y < yi + 35000000:
    r = y
    y = y + vi* dt - (G * m * dt**2)/(2 * r**2)*np.sin(f.angulo_frac2rad(0,y))
    vf = vi - (G*m*dt)/(r**2) * np.sin(f.angulo_frac2rad(0, y))
    vi = vf
    listay.append(y)
    listav.append(vf)
    listat.append(t)
    t += dt
print(np.sin(f.angulo_frac2rad(0, y)))
print(vf)
print(y)


plt.plot(listat,listay)
plt.show()

plt.plot(listat,listav)
plt.show()
