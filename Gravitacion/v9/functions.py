# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 18:14:38 2021

@author: Juan Antonio

Title: Funciones de Gravitación

ver: 5.0
"""

import numpy as np
rev = 2 * np.pi
G = 6.67 * (10**-11)

def posicionrad_angular_mru(va,t):
    prad = va * t
    return fix2radpi(prad)

def magnitud(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
def fix2radpi(prad):
    if prad >= rev:
        reduc = int(prad/rev)
        return prad - reduc * rev
    else:
        return prad

def posicionxy_angular(posicionrad,r):
    x = r * np.cos(posicionrad)
    y = r * np.sin(posicionrad)
    return (x,y)

def angulo_frac2rad(x,y):
    inc = np.arctan2(y,x)
    if inc >= 0:
        return inc
    else:
        return 2*np.pi+inc
    
    
def posicionxy_angular_mru_cd00_pd00(xc,yc,xi,yi,posicionrad,r):
    return posicionxy_angular(posicionrad + angulo_frac2rad(xi-xc,yi.yc), r)

    


def actvec2(ni,vi,m,r,dt,sincos):
    ni = ni + vi * dt + (G * m * dt**2)/(2 * r**2) * sincos
    vf = vi + (G * m * dt)/(r**2) * sincos
    return ni,vf

def actvecglob2(a1, a2, dt):
    r = magnitud(a2[3],a2[4],a1[3],a1[4])
    x = a2[3] - a1[3]
    y = a2[4] - a1[4]
    prad = angulo_frac2rad(x, y)
    
    xi, vx = actvec2(a1[3], a1[5], a2[1], r, dt, np.cos(prad))
    yi, vy = actvec2(a1[4], a1[6], a2[1], r, dt, np.sin(prad))
    
    return np.array([a1[0],a1[1],a1[2],xi,yi,vx,vy])
    
def vtan(m,r):
    return (G * m / r)**0.5

