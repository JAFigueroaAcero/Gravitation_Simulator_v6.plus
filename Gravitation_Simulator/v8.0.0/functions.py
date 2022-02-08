# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 22:11:22 2021

@author: Juan Antonio

Title: Funciones de Gravitación

Ver: 6.0
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

'''
name
masa
radio
x
y
xvel
yvel
'''

def masspoint(a, eje, passing):
    num = 0
    den = 0
    ac = a.copy()
    ac = np.delete(ac, passing)
    
    for n in ac:
        num += (n[1]*n[3+eje])
        den += n[1]
    return num/den, den

def actvec2(ni,vi,m,r,dt,sincos):
    ni = ni + vi * dt + (G * m * dt**2)/(2 * r**2) * sincos
    vf = vi + (G * m * dt)/(r**2) * sincos
    return ni,vf

def actvecglob3(a, dt, using):
    ac = a.copy()
    ac = np.delete(ac, using)
    
    
    x,den = masspoint(a, 0, using)
    y, _ = masspoint(a, 1, using)
    
    r = magnitud(x, y, a[using][3], a[using][4])
    x = x - a[using][3]
    y = y - a [using][4]
    prad = angulo_frac2rad(x, y)
    
    xi, vx = actvec2(a[using][3], a[using][5], den, r, dt, np.cos(prad))
    yi, vy = actvec2(a[using][4], a[using][6], den, r, dt, np.sin(prad))
    
    return np.array([a[using][0],a[using][1],a[using][2],xi,yi,vx,vy])
    
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
