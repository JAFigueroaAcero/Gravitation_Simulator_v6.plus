# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 18:17:21 2021

@author: Juan Antonio

Title: Gravitación sim

ver: 8.0
"""

import functions as f
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt      

def main():
    df = pd.read_csv('assets\\data.csv')
    dfl = df.values.tolist()
    a = np.array([None for n in range(len(dfl))])
    for n,e in enumerate(dfl):
        dfl[n] = dfl[n][:-2] + list(f.posicionxy_angular(dfl[n][-1], dfl[n][-2]))
        a[n] = np.array([float(a) for a in dfl[n]])
    
    '''
    name
    masa
    radio
    x
    y
    xvel
    yvel
    '''
    df2 = pd.read_csv('assets\\configs.csv')
    dfl2 = df2.values.tolist()[0]
    # variables en segundos
    trps = dfl2[0] # tiempo real por segundo
    dt = dfl2[1]     # numero de intervalo entre sumatorias de integracion
    t = 0           # tiempo inicial
    tts = dfl2[2] # tiempo total de sistema
    frec = dfl2[3]       # frecuencia en iteraciones/segundo
    it = tts / dt   # iteraciones totales
    itf = frec * tts / trps # iteraciones totales finales
    rel = it / itf  # relacion de iteraciones totales  sobre iteraciones totales finales
    
    
    
    listaxs = [[] for n in range(len(dfl))]
    listays = [[] for n in range(len(dfl))]
    
    
    while t < tts:
        ac = a.copy()
        
        for n,el in enumerate(a):

            a[n] = f.actvecglob3(ac, dt, n)
        
        for n, el in enumerate(listaxs):
            el.append(a[n][3])
            listays[n].append(a[n][4])
            
        
        t += dt
    
    listag= [[listaxs[n],listays[n]] for n in range(len(listaxs))]
    listaf = [[[],[]] for n in range(len(listaxs))]
    
    
    for n in range(int(itf)):
        loc = int(n * rel)
        for m, el in enumerate(listag):
            for o, el2 in enumerate(el):
                listaf[m][o].append(el2[loc])
            
    for el in listaf:
        plt.plot(el[0],el[1])
    plt.show()
        
    return {
        'xs': [listaf[n][0] for n, el in enumerate(listaf)],
        'ys': [listaf[n][1] for n, el in enumerate(listaf)]
        }
    
    

if __name__ == "__main__":
    main()