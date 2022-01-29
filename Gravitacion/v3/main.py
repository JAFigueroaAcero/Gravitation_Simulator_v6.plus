# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 10:04:30 2021

@author: Juan Antonio

Title: Gravitación sim

ver: 3.1
"""

import numpy as np
import functions as f
import matplotlib.pyplot as plt
xi = 0
yi = 6371000
vix = 0
vfx= 0
viy = 11190
vfy = 0
m = 5.972 * (10**24)
r = 6371000
dt = 0.01
prad = 0
t = 0
xo = 0
yo = 0

ymark = yi-1
listax = list()
listavx = list()
listay = list()
listavy = list()
listat = list()
while t < 60*100:
    xi,vix,vfx, yi,viy,vfy,r = f.actvecglob(xi, vix, yi, viy, m, dt, xo, yo)
    listax.append(xi)
    listavx.append(vfx)
    listay.append(yi)
    listavy.append(vfy)
    listat.append(t)
    t += dt

plt.plot(listat,listay)
plt.show()
plt.plot(listat,listavy)
plt.show()

plt.plot(listat,listax)
plt.show()
plt.plot(listat,listavx)
plt.show()

plt.plot(listax,listay)
plt.show()
"""
print(np.arctan2(-yi,-xi))

print(f.angulo_frac2rad(-xi,-yi))
"""