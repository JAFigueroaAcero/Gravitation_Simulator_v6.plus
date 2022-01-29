# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 20:36:03 2021

@author: Juan Antonio

Title: Gravitación sim

ver: 2.0
"""

import functions as f

ti = 100

m1 = 5.972 * (10**24)
m2 = 5000
rt = 6.371 * (10**3)
coords = []
t = 0

xt = 0
yt = 0
vt = 0

xo = rt + 400 * (10**3)
yo = 0
vo = 7660

poso = list()
post = list()
while t < 10000000:
        r = f.magnitud(xt,yt,xo, yo)
        
        ago = f.aceleracionG(m1, r)
        radao = f.rad180(f.incr(xo-xt, yo-yt))
        radvo = f.rad90(f.incr(xo-xt,yo-yt))
        
        agt = f.aceleracionG(m2, r)
        radat = f.rad180(f.incr(xt-xo, yt-yo))
        radvt = f.rad90(f.incr(xt-xo, yt-yo))
        xo, yo, vo = f.act(xo, yo, ago, radao, vo, radvo, ti)
        xt, yt, vt = f.act(xt, yt, agt, radat, vt, radvt, ti)
        
        
        poso.append([xo,yo,vo,t])
        post.append([xt,yt,vt,t])
        print(t)
        t += ti

f.graph(poso)

f.graph(post)
