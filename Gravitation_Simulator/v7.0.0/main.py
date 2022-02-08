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
def main():
    df = pd.read_csv('assets\\data.csv')
    dfl = df.values.tolist()
    a = np.array([None,None])
    for n,e in enumerate(dfl):
        dfl[n] = dfl[n][:-2] + list(f.posicionxy_angular(dfl[n][-1], dfl[n][-2]))
        a[n] = np.array([float(a) for a in dfl[n]])
    
    
    
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
    
    listax = []
    listay = []
    listax2 = []
    listay2 = []
    while t < tts:
        ac = a.copy()
        a[0] = f.actvecglob2(ac[0], ac[1], dt)
        a[1] = f.actvecglob2(ac[1], ac[0], dt)
        
        listax.append(ac[1][3])
        listay.append(ac[1][4])
        
        listax2.append(ac[0][3])
        listay2.append(ac[0][4])
        
        t += dt
    
    listag = [listax,listay,listax2,listay2]
    
    listaf = [[],[],[],[]]
     
    a = 0

    
    for n in range(int(itf)):
        loc = int(n * rel)
        for m, el in enumerate(listaf):
            el.append(listag[m][loc])
            
            
    return {
        'xs': [listaf[0],listaf[2]],
        'ys': [listaf[1],listaf[3]]
        }
    
    
    
if __name__ == "__main__":
    main()