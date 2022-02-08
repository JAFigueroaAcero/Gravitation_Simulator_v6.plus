# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 08:02:06 2021

@author: Juan Antonio

Title: Graficación en vivo

Ver: 1.0
"""

from tornado.ioloop import IOLoop

import main as m
from bokeh.layouts import column
from bokeh.models.widgets import Button
from bokeh.plotting import figure
import sys
from bokeh.application.handlers import FunctionHandler
from bokeh.application import Application
from bokeh.server.server import Server
import pandas as pd

def md(doc):
    global lenbase
    global i
    global inter
    global dsc
    global ds
    global df
    df = m.main()
    df2 = pd.read_csv('assets\\configs.csv')
    dfl2 = df2.values.tolist()[0]
    lenbase = len(df['xs'][0])
    i = 0
    inter = dfl2[4]
    itime = 1000/dfl2[3]
    
    p = figure()
    
    r = p.multi_line(xs=[[],[]], ys=[[],[]], color=['blue','green'],line_color ='blue')
    
    cir = p.circle(x = [], y= [], radius=696340000)
    dsc = cir.data_source
    ds = r.data_source
    
    doc.add_root(column([p, button]))
    doc.add_periodic_callback(callback, itime)

def button_callback():
    sys.exit()

button = Button(label="Stop", button_type="success")
button.on_click(button_callback)


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

def main():
    """Launch the server and connect to it.
    """
    print("Preparing a bokeh application.")
    io_loop = IOLoop.current()
    bokeh_app = Application(FunctionHandler(md))

    server = Server({"/": bokeh_app}, io_loop=io_loop)
    server.start()
    print("Opening Bokeh application on http://localhost:5006/")

    io_loop.add_callback(server.show, "/")
    io_loop.start()

if __name__ == "__main__":
    main()