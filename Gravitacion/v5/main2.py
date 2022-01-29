# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 11:21:21 2021

@author: Juan Antonio

Title: Gravitación sim

ver: 5.0
"""

import numpy as np
import functions as f
import matplotlib.pyplot as plt
import cv2 as cv

def main():
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
    dt = 60*10
    
    vix1 = f.vtan(m2, y2)/1.5
    viy1 = 0
    
    vix2 = f.vtan(m1, y2)
    viy2 = 0
    
    listax1 = [x1]
    listay1 =   [y1]
    
    listax2 = [x2]
    listay2 = [y2]
    
    listat = [0]
    
    while t < 31536000*3/3 * 0.5:
            x1,vix1,vfx1, y1,viy1,vfy1,r = f.actvecglob(x1, vix1, y1, viy1, m2, dt, x2, y2)
            x2,vix2,vfx2, y2,viy2,vfy2,r = f.actvecglob(x2, vix2, y2, viy2, m1, dt, x1, y1)
            
            
            
            listax1.append(x1)
            listay1.append(y1)
            
            listax2.append(x2)
            listay2.append(y2)
            
            listat.append(t)
            t += dt
    
    
    plt.plot(listax1,listay1)
    plt.plot(listax2,listay2)
    plt.show()
    
    return{
        'xs': [listax1,listax2],
        'ys': [listay1,listay2]
        }