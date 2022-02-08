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


def main():
    lista = f.csv2list('assets\data.csv')
    for el in lista:
        for e in range(len(el[1::])):
            el.append(float(el.pop(1)))     
            
    for el in lista:

        vec = f.posicionxy_angular(el[-1],el[-2])
        el.pop(-1)
        el.pop(-1)
        el.append(vec[0])
        el.append(vec[1])
        
    ar = np.array(lista)
    dt = 60*10
    t = 0
    
    x1 = list()
    y1 = list()
    
    x2 = list()
    y2 = list()
    
    while t < 31536000:
        el1 = f.actvecglob2(ar[0], ar[1], dt)
        el2 = f.actvecglob2(ar[1], ar[0], dt)
        ar = np.array([el1,el2])
        
        x1.append(ar[0][3])
        y1.append(ar[0][4])
        
        x2.append(ar[1][3])
        y2.append(ar[1][4])
        t+= dt
    
    plt.plot(x1,y1)
    plt.plot(x2,y2)
    plt.show()
    return {
        'xs': [x1,x2],
        'ys': [y1,y2]
        }
    # antes de iniciar con el proceso obtener el vx y vy con v y alfa
    # Pasar todas las funciones para funcionar en array con el formato
    # name, mass, radio, x, y, vx, vy
    
    # trabajar con while principal y nueva funcion actvecglob
def mainprueba():
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
    '''
    while t < 31536000/4:
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
    '''
    print(f.vtan(m1, r1))
    return{
        'xs': [listax1,listax2],
        'ys': [listay1,listay2]
        }


main()