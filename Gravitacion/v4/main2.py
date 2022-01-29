# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 11:21:21 2021

@author: Juan Antonio

Title: Gravitación sim

ver: 3.2
"""

import numpy as np
import functions as f
import matplotlib.pyplot as plt
import cv2 as cv

m1 = 1.989 * (10**30)
r1 = 696340000

x1 = 0
y1 = 0

d = 149597870000

m2 = 5.972 * (10**28)
r2 = 6371000

x2 = 0
y2 = r1+r2+d

t = 0
dt = 60

vix1 = f.vtan(m2, y2)/1.5
viy1 = 0

vix2 = f.vtan(m1, y2)
viy2 = 0

listax1 = [x1]
listavx1 = [vix1]
listay1 =   [y1]
listavy1 = [viy1]

listax2 = [x2]
listavx2 = [vix2]
listay2 = [y2]
listavy2 = [viy2]

listat = [0]
fig,ax = plt.subplots()

while t < 31536000/4:
        x1,vix1,vfx1, y1,viy1,vfy1,r = f.actvecglob(x1, vix1, y1, viy1, m2, dt, x2, y2)
        x2,vix2,vfx2, y2,viy2,vfy2,r = f.actvecglob(x2, vix2, y2, viy2, m1, dt, x1, y1)
        
        
        
        
        listax1.append(x1)
        listavx1.append(vfx1)
        listay1.append(y1)
        listavy1.append(vfy1)
        
        listax2.append(x2)
        listavx2.append(vfx2)
        listay2.append(y2)
        listavy2.append(vfy2)
        
        listat.append(t)
        """
        if t % 60*60*60*24*30 == 0:
            ax.plot([listax1[-2],listax1[-1]],[listay1[-2],listay1[-1]], 'b')
            ax.plot([listax2[-2],listax2[-1]],[listay2[-2],listay2[-1]], 'y')
    
            fig.canvas.draw()
    
            data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
            data = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))
            cv.imshow('v',data)
        """
        t += dt
cv.destroyAllWindows()
plt.show()
plt.plot(listat,listay1)
plt.show()
plt.plot(listat,listavy1)
plt.show()

plt.plot(listat,listax1)
plt.show()
plt.plot(listat,listavx1)
plt.show()


plt.plot(listat,listay2)
plt.show()
plt.plot(listat,listavy2)
plt.show()

plt.plot(listat,listax2)
plt.show()
plt.plot(listat,listavx2)
plt.show()


plt.plot(listax1,listay1)
plt.plot(listax2,listay2)
plt.show()
