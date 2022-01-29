# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 13:44:51 2021

@author: Juan Antonio
"""


from bokeh.layouts import column
from bokeh.models import Button
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, curdoc
import numpy as np
import functions as f
import matplotlib.pyplot as plt
import cv2 as cv
import time
#graf

print('inicio')
pn = figure()

rn = pn.multi_line(xs=[[],[]], ys=[[],[]], color=['blue','red'],line_color ='blue')


ds = rn.data_source
i = 0
def callback(l1,l2):
    global i
    new_data = dict()
    try:
        new_data['xs'] =[ds.data['xs'][0] + [l1[0]], ds.data['xs'][1] + [l2[0]]]
        new_data['ys'] = [ds.data['ys'][0] + [l1[1]], ds.data['ys'][1] + [l2[1]]]
    except:
        new_data['xs'] =[ds.data['xs'][0][-500:-1] + [l1[0]], ds.data['xs'][1][-500:-1] + [l2[0]]]
        new_data['ys'] = [ds.data['ys'][0][-500:-1] + [l1[1]], ds.data['ys'][1][-500:-1] + [l2[1]]]
    ds.data = new_data
    i+=1
curdoc().add_root(column(pn))

print('ready')

print('starting')
# sim
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
dt = 60

vix1 = f.vtan(m2, y2)/2
viy1 = 0

vix2 = f.vtan(m1, y2)
viy2 = 0

listax1 = [x1]
listavx1 = [vix1]
listay1 =   [y1]
listavy1 = [viy1]

listax2 = [x2]
listavx2 = [vix2]
listay2 = [y2]
listavy2 = [viy2]

listat = [0]

while t < 31536000/(15):
        
        x1,vix1,vfx1, y1,viy1,vfy1,r = f.actvecglob(x1, vix1, y1, viy1, m2, dt, x2, y2)
        x2,vix2,vfx2, y2,viy2,vfy2,r = f.actvecglob(x2, vix2, y2, viy2, m1, dt, x1, y1)
        
        callback([x1,y1],[x2,y2])
        """
        listax1.append(x1)
        listay1.append(y1)
        
        listax2.append(x2)
        listay2.append(y2)
        """
        
        t += dt
print('fin')


"""
plt.plot(listax1,listay1)
plt.plot(listax2,listay2)
plt.show()
"""
