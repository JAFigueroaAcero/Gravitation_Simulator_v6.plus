# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 14:39:58 2021

@author: Juan Antonio

Title: Funciones de Gravitación

ver: 4.0
"""
import numpy as np
import pandas as pd
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


    
    # Pasar todas las funciones para funcionar en array con el formato
    # name, mass, radio, x, y, vx, vy
    
    # trabajar con while principal y nueva funcion actvecglob
    
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


def actvec2(ni,vi,m,r,dt,sincos):
    ni = ni + vi * dt + (G * m * dt**2)/(2 * r**2) * sincos
    vf = vi + (G * m * dt)/(r**2) * sincos
    return ni,vf

def actvecglob2(a1, a2, dt):
    r = magnitud(a2[3],a2[4],a1[3],a1[4])
    x = a2[3] - a1[3]
    y = a2[4] - a1[4]
    prad = angulo_frac2rad(x, y)
    
    xi, vx = actvec2(a1[3], a1[5], a1[1], r, dt, np.cos(prad))
    yi, vy = actvec2(a1[4], a1[6], a1[1], r, dt, np.sin(prad))
    
    return np.array([a1[0],a1[1],a1[2],xi,yi,vx,vy])
    
def vtan(m,r):
    return (G * m / r)**0.5




def csv2list(csv):
    df = pd.read_csv(csv)
    lista = []
    for index, row in df.iterrows():
        locl = list()
        for el in row:
            locl.append(el)
        locl.pop(0)
        lista.append(locl)
    return lista




