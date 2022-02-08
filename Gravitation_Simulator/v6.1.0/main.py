# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 18:17:21 2021

@author: Juan Antonio

Title: Gravitación sim

ver: 6.0
"""

import functions as f
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('assets\\data.csv')
    dfl = df.values.tolist()
    a = np.array([None,None])
    for n,e in enumerate(dfl):
        dfl[n] = dfl[n][:-2] + list(f.posicionxy_angular(dfl[n][-1], dfl[n][-2]))
        a[n] = np.array([float(a) for a in dfl[n]])
    
    
    
    dt = 60*10
    t = 0
    tt = 60*60*24*365*2
    
    listax = []
    listay = []
    listax2 = []
    listay2 = []
    while t < tt:
        ac = a.copy()
        a[0] = f.actvecglob2(ac[0], ac[1], dt)
        a[1] = f.actvecglob2(ac[1], ac[0], dt)
        
        listax.append(ac[1][3])
        listay.append(ac[1][4])
        
        listax2.append(ac[0][3])
        listay2.append(ac[0][4])
        
        t += dt
    
    plt.plot(listax,listay)
    plt.plot(listax2,listay2)
    plt.show()
    
    return {
        'xs': [listax,listax2],
        'ys': [listay,listay2]
        }
    
    
    
if __name__ == "__main__":
    main()