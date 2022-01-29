# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 14:39:58 2021

@author: Juan Antonio

Title: Funciones de Gravitación

ver: 3.0
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

def resize(x,y,alfa):
    return alfa * x, alfa * y
"""
xi = 400
yi = 0
vix = 0
vfx= 0
viy = 7660
vfy = 0
m = 5.972 * (10**24)
r = 6371000
dt = 0.1
prad = 0
t = 0
"""
"""
    r = y
    y = y + vi* dt - (G * m * dt**2)/(2 * r**2)*np.sin(f.angulo_frac2rad(0,y))
    vf = vi - (G*m*dt)/(r**2) * np.sin(f.angulo_frac2rad(0, y))
    vi = vf
    listay.append(y)
    listav.append(vf)
    listat.append(t)
    t += dt
"""
def actvec(ni,vi,m,r,dt,sincos):
    ni = ni + vi * dt + (G * m * dt**2)/(2 * r**2) * sincos
    vf = vi + (G * m * dt)/(r**2) * sincos
    vi = vf
    return ni, vi, vf

def actvecglob(xi,vix,yi,viy,m,dt,xo,yo):
    r = magnitud(xo,yo,xi,yi)
    x = xo-xi
    y = yo-yi
    prad = angulo_frac2rad(x,y)
    xi, vix, vfx = actvec(xi,vix,m,r,dt,np.cos(prad))
    yi, viy, vfy =  actvec(yi,viy,m,r,dt,np.sin(prad))
    return xi,vix,vfx, yi,viy,vfy,r

def vtan(m,r):
    return (G * m / r)**0.5


def array(lista1, lista2, dt, inter):
    lista1x = sorted(lista1[0])
    lista1y = sorted(lista1[1])
    
    lista2x = sorted(lista2[0])
    lista2y = sorted(lista2[1])
    
    maxx = max(lista1x[-1],lista2x[-1])
    minx = min(lista1x[0],lista2x[0])
    
    maxy = max(lista1y[-1],lista2y[-1])
    miny = min(lista1y[0],lista2y[0])
    
    return np.zeros((maxx-minx,maxy-miny,3), dtype = 'uint8')

