# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 20:35:26 2021

@author: Juan Antonio

Title: Funciones de Gravitación

ver: 2.0
"""

import numpy as np
import matplotlib.pyplot as plt

GRAVITACION = 6.67 * (10**-11)

def fuerzaG(m1,m2,r):
    return GRAVITACION * m1 * m2 // r**2

def aceleracionG(m,r):
    return GRAVITACION * m // r**2

def magnitud(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def pmasa(x1,y1,x2,y2,m1,m2):
    rel = m1 + m2
    x = (m1*x1+m2*x2)/(rel)
    y = (m1*y1+m2*y2)/(rel)
    return x,y

def velTan(G,r):
    return (G * r)**0.5

def incr(x,y):
    inc = np.arctan2(y,x)
    if inc >= 0:
        return inc
    else:
        return 2*np.pi+inc

def magrad_comp(mag,rad):
    x = mag * np.cos(rad)
    y = mag * np.sin(rad)
    return x,y

def ace_vel(a,v,ti):
    return a*ti + v

def ace_pos(n,a,v,ti):
    return n + v*ti + (a * ti**2)//2

def rad180(rad):
    rad = rad + np.pi/2
    if rad >= 2*np.pi:
        return 2*np.pi - rad
    else:
        return rad

def rad90(rad):
    rad = rad + np.pi/4
    if rad >= 2*np.pi:
        return 2*np.pi - rad
    else:
        return rad
    
def act(x,y,a,rada,v,radv,ti):
    ax, ay = magrad_comp(a, rada)
    vx, vy = magrad_comp(v, radv)
    xvel = ace_vel(ax,vx,ti)
    yvel = ace_vel(ay,vy,ti)
    xpos = ace_pos(x, ax, vx, ti) 
    ypos = ace_pos(y, ay, vy, ti)
    
    v = (xvel**2 + yvel**2)**0.5
    
    return xpos,ypos,v
    
    
    
def graph(lista):
    x = [i[0] for i in lista]
    t = [i[1] for i in lista]
    v = [i[2] for i in lista]
    y = [i[3] for i in lista]
    
    plt.plot(x,t)
    plt.show()
    
    plt.plot(y,t)
    plt.show()
    
    plt.plot(v,t)
    plt.show()
    
    