# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 21:43:34 2021

@author: Juan Antonio

Title: Funciones de Gravitación

ver: 1.0
"""
import numpy as np

C_GRAVITACION = 6.67*(10**(-11))
lim = 9999999999999999
radpi = 180/np.pi
def fuerzag(m1,m2,r):
    return C_GRAVITACION * (m1*m2)/(r**2)

def aceleraciong(m,r):
    return C_GRAVITACION * m/(r**2)

def mag(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def pmasa(x1,y1,x2,y2,m1,m2):
    rel = m1 + m2
    x = (m1*x1+m2*x2)/(rel)
    y = (m1*y1+m2*y2)/(rel)
    return x,y

# Funciones ver 1
def inc_f(x1,y1,x2,y2,m1=None,m2=None):
    try:
        if m1 == None or m2 == None:
            x = x2-x1
            y = y2-y1
        else:
            centro = pmasa(x1,y1,x2,y2,m1,m2)
            x = x2 - centro[0]
            y = y2 - centro[1]
        if x >= 0 and y >= 0:
            return y/x, 1, (x,y)
        elif x <= 0 and y >= 0:
            return abs(y/x), 2, (x,y)
        elif x <= 0 and y <= 0:
            return abs(y/x), 3,(x,y)
        else:
            return y/x, 4, (x,y)
    except:
        if x == 0 and y > 0:
            return lim, 2, (x,y)
        else:
            return lim, 4,(x,y)
def inc_r(x1,y1,x2,y2, m1 = None, m2 = None):
    if m1 == None or m2 == None:
        v = inc_f(x1,y1,x2,y2)
    else:
        v = inc_f(x1,y1,x2,y2,m1,m2)
    if v[1] == 1:
        return np.arctan(v[0])
    elif v[1] == 2:
        return np.pi - np.arctan(v[0])
    elif v[1] == 3:
        return np.pi + np.arctan(v[0])
    else:
        return 2*np.pi - np.arctan(v[0])

def inc_g(x1,y1,x2,y2,m1 = None,m2 = None):
    if m1 == None or m2 == None:
        return inc_r(x1,y1,x2,y2)* radpi
    else:
        return inc_r(x1,y1,x2,y2,m1,m2)* radpi
    
# Funciones ver 2

def inc_r2(x1,y1,x2,y2, m1= None, m2 = None):
    if m1 == None or m2 == None:
            x = x2-x1
            y = y2-y1
    else:
        centro = pmasa(x1,y1,x2,y2,m1,m2)
        x = x2 - centro[0]
        y = y2 - centro[1]
    inc = np.arctan2(y,x)
    if inc >= 0:
        return inc
    else:
        return 2*np.pi+inc

def inc_g2(x1,y1,x2,y2, m1 = None, m2 = None):
    if m1 == None or m2 == None:
        return inc_r2(x1,y1,x2,y2) * radpi
    else:
        return inc_r2(x1,y1,x2,y2,m1,m2) * radpi
    
def inc_f2(x1,y1,x2,y2,m1 = None,m2 = None):
    if m1 == None or m2 == None:
        x = x2-x1
        y = y2-y1
    else:
        centro = pmasa(x1,y1,x2,y2,m1,m2)
        x = x2 - centro[0]
        y = y2 - centro[1]
    try:
        return y/x, (x,y)
    except:
        return lim, (x,y)

def mag_pm(x1,y1,x2,y2,m1,m2):
    centro = pmasa(x1,y1,x2,y2,m1,m2)
    return mag(centro[0],centro[1],x2,y2)


def suma_vec(cords1,cords2):
    x = cords1[0]+cords2[0]
    y = cords2[1]+cords2[1]
    return (x,y)


def vtan(ag,r):
    return (ag*r)**0.5


