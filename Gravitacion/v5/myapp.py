# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 08:37:26 2021

@author: Juan Antonio

Title: Interfaz Gravitación sim

ver: 1.0
"""

import main2 as m
from bokeh.layouts import column
from bokeh.plotting import figure, curdoc

df = m.main()
lenbase = len(df['xs'][0])
i = 0
inter = 100

p = figure()

r = p.multi_line(xs=[[],[]], ys=[[],[]], color=['blue','green'],line_color ='blue')

cir = p.circle(x = [], y= [], radius=696340000)
dsc = cir.data_source
ds = r.data_source

def callback():
    global df
    global i
    global lenbase
    global inter
    global ds
    global dsc
    dsc.data = {
        'x': [df['xs'][0][i+inter],df['xs'][1][i+inter]],
        'y': [df['ys'][0][i+inter],df['ys'][1][i+inter]]
        }
    ds.data = {
        'xs': [list(df['xs'])[0][i:i+inter],list(df['xs'])[1][i:i+inter]],
        'ys': [list(df['ys'])[0][i:i+inter],list(df['ys'])[1][i:i+inter]]
        }
    if i >= lenbase - inter - 1:
        i = 0
    i += 1
    
curdoc().add_root(column(p))
curdoc().add_periodic_callback(callback, 0.01)


