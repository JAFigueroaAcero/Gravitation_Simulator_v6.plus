# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 18:17:21 2021

@author: Juan Antonio

Title: Gravitación sim

ver: 8.3
"""

import functions as f
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt      

import time

def main():
    df = pd.read_csv('assets//data.csv')
    dfl = df.values.tolist()
    a = np.array([None for n in range(len(dfl))])
    for n,e in enumerate(dfl):
        dfl[n] = dfl[n][:-2] + list(f.positionxy_angle(dfl[n][-1], dfl[n][-2]))
        a[n] = np.array([float(a) for a in dfl[n]])
    
    '''
    name
    mass
    radio
    x
    y
    xvel
    yvel
    '''
    df2 = pd.read_csv('assets//configs.csv')
    dfl2 = df2.values.tolist()[0]
    # variables in seconds
    trps = dfl2[0] # real time per second
    dt = dfl2[1]     # interval number between sums
    t = 0           # initial time
    tts = dfl2[2] # total system time
    frec = dfl2[3]       # frequency in iterations/seconds
    it = tts / dt   # total iterations
    itf = frec * tts / trps # total final iterations
    rel = it / itf  # relation of total iterations over total final iterations
    
    
    
    list_xs = [[] for n in range(len(dfl))]
    list_ys = [[] for n in range(len(dfl))]
    
    musca = time.time()
    while t < tts:
        ac = a.copy()
        
        for n,el in enumerate(a):
            a[n] = f.actvecglob3(ac, dt, n)
        for n, el in enumerate(list_xs):
            el.append(a[n][3])
            list_ys[n].append(a[n][4])
            
        t += dt
    
    misca = time.time()
    mickeymouse = misca-musca
    print(mickeymouse)
    print(len(list_ys[0]))

    list_g= [[list_xs[n],list_ys[n]] for n in range(len(list_xs))]
    list_f = [[[],[]] for n in range(len(list_xs))]
    
    
    for n in range(int(itf)):
        loc = int(n * rel)
        for m, el in enumerate(list_g):
            for o, el2 in enumerate(el):
                list_f[m][o].append(el2[loc])
            
    for el in list_f:
        plt.plot(el[0],el[1])
    plt.show()
        
    return {
        'xs': [list_f[n][0] for n, el in enumerate(list_f)],
        'ys': [list_f[n][1] for n, el in enumerate(list_f)]
        }
    
    

if __name__ == "__main__":
    main()