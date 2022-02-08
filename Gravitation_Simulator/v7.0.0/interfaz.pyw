# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 19:50:20 2021

@author: Juan Antonio

Title: Interfaz tkinter Gravitación sim

ver: 3.0
"""

import tkinter as tk
import pandas as pd
import myapp as m
from os.path import isfile
from tkinter import Tk


defaultconfigs = [60*60*24,60*10,60*60*24*365*2,20,500]

def cbu(text):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(text)
    r.update()
    r.destroy()
def conv(papa,n):
    op = 1
    try:
        while True:
            for mv, el in enumerate(n):
                
                if el == '*':
                    for o, el2 in enumerate(n[mv+1::]):
                        loc = True
                        if el2 == '*' or el2 == 'e':
                            op *= int(n[0:mv]) * int(n[mv+1:mv+o+1])
                            n = str(op) + n[mv+o+1::]
                            loc = False
                    if loc:
                        w = len(str(op))
                        if w == 1:
                            op = int(n[0:mv]) * int(n[mv+1::])
                        else:
                            op = int(n[0:w]) * int(n[w+1::])
                        
                        n = str(op)
                    break
                elif el == 'e':
                    op *= int(n[0:mv]) *(10** int(n[mv+1::]))
                    n = 0
                    break
            try:
                float(n)
                break
            except:
                pass
    except:
        pass
        ad(papa, 'Wrong format', 'The format of the operation \n is incorrect.')
    return op

def empty(val):
    loc = False
    for v in val:
        if v.get() == '':
            loc = True
            break
    return loc
def num(val):
    loc = True
    for v in val:
        try:
            float(v.get())
            
        except:
            loc = False
            break
    return loc


class ad():
    def __init__(self,papa,titulo,texto):
        self.root= tk.Toplevel(papa.root)
        self.root.resizable(0,0)
        self.root.geometry('220x100')
        self.root.title(titulo)
        self.a1 = tk.Frame(self.root, width=200, height=100)
        self.a1l = tk.Label(self.a1, text=texto, anchor="center")
        self.a1l.grid(row=1,column=0, pady=10)
        self.b1 = tk.Button(self.a1, width=3, height=1 ,text='Ok', command= self.root.destroy)
        self.b1.grid(row=3,column=0, sticky='nsew')
        self.a1.pack()
        self.root.transient(papa.root)
        self.root.mainloop()

class conversion():
    def __init__(self,papa):
        self.lista = [
            ['\'*\' symbol','Symbol equivalent to multiply.'],
            ['\'e\' sumbol', 'Symbol equivalent to x * 10 ** n.'],
            ['Limitant 1', 'The operators only work arrange \n in a max of 3 different values.'],
            ['Limitant 2', 'Use \'*\' and \'e\' in different operations.'],
            ['Note', 'This is just a simplifier for the \n interface not a complex calculator.']
            ]
        self.root = tk.Toplevel(papa.root)
        self.root.resizable(0,0)
        self.root.title('Converter')
        self.a1 = tk.Frame(self.root, width = 220, height = 200)
        self.a1.grid(row=1, column=0, sticky='nsew', pady=10)
        
        self.a2 = tk.Frame(self.root)
        self.a2.grid(row=0, column=0, sticky='nsew', pady=0)
        
        self.a3 = tk.Frame(self.root)
        self.a3.grid(row=2, column=0, sticky='nsew', pady=0)
        
        self.op = tk.Entry(self.a1,  width=30)
        self.op.grid(row=2, column=1, padx=5, pady=0)
        
        def convloc():
            x = conv(self, self.op.get())
            if x != None:
               self.op.delete(0,"end")
               self.op.insert(0,x) 
        self.b1 = tk.Button(self.a3, text = 'Copy to c', width=6, padx=5, pady=0, command = lambda: cbu(self.op.get()))
        self.b1.grid(row=0, column=1,padx=5, pady=5)
        
        self.b2 = tk.Button(self.a3, text = 'Convert', width=6, padx=5, pady=0, command = lambda: convloc())
        self.b2.grid(row=0, column=0,padx=5, pady=5)
        
        self.b3 = tk.Button(self.a2, text = '?', width=2, padx=5, pady=0, command = lambda: helpd(self,self.lista))
        self.b3.grid(row=0, column=1,padx=5, pady=5)
        self.root.transient(papa.root)
        self.root.mainloop()
def show(papa):
    if isfile('assets\\data.csv'):
        df = pd.read_csv('assets\\data.csv')
        df = df.values.tolist()
        lista = []
        relative = ['mass','radio','x','y','vel','prad']
        for el in df:
            
            loc = ''
            for n,e in enumerate(el[1::]):
                loc += f'{relative[n]}: {str(e)} \n'
            lista.append([el[0], loc])
        helpd(papa,lista, name = 'Last data')
    else:
        ad(papa, 'Not found', 'There is not last data source')
class helpd():
    def __init__(self,papa,helps, name = None):
        if name == None:
            name = 'Help'
        self.root = tk.Toplevel(papa.root)
        self.root.resizable(0,0)
        self.root.title(name)
        self.a1 = tk.Frame(self.root)
        self.a1.grid(row=0, column=0, sticky='nsew', pady=10)
        for n,h in enumerate(helps):
            tk.Label(self.a1, text = f'{h[0]}:').grid(row = n, column = 0, padx=5, pady=5)
            tk.Label(self.a1, text = h[1]).grid(row = n, column = 1, padx=5, pady=5)
        self.root.transient(papa.root)
        self.root.mainloop()
            
class config():
    def __init__(self,papa):
        self.lista = [
            ['Real ex time per sec','It expresses how much time of simulation is going to be represented \n as a second in real time. \n 60*60*24 is the default.'],
            ['Integral sums interval', 'It expresses the time of simulation that passes between an update of data. \n 60*10 seconds is the default.'],
            ['Total simulation time', 'It expresses the total time that passes in a simulation. \n 60*60*24*365*2 seconds is the default.'],
            ['Iterations per second', 'It expresses the speed of update of the simulation per seconds. \n 20 i/s is the default and the min value accepted.'],
            ['Interval length', 'It expresses how many iterations are going to be shown at the same time. \n  500 is the default, the interval is 1 <= x <= 1000.']
            ]
        self.root = tk.Toplevel(papa.root)
        self.root.resizable(0,0)
        self.root.title('config')
        self.a1 = tk.Frame(self.root, width = 220, height = 200)
        self.a1.grid(row=1, column=0, sticky='nsew', pady=10)
        
        self.a2 = tk.Frame(self.root)
        self.a2.grid(row=0, column=0, sticky='nsew', pady=0)
        
        self.a3 = tk.Frame(self.root)
        self.a3.grid(row=2, column=0, sticky='nsew', pady=0)
        
        tk.Label(self.a1, text = 'Real ex time per sec:').grid(row=0,column=0, padx=5, pady=5)
        self.rtps = tk.Entry(self.a1,  width=30)
        self.rtps.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(self.a1, text = 'Integral sums interval:').grid(row=1,column=0, padx=5, pady=5)
        self.dt = tk.Entry(self.a1,  width=30)
        self.dt.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(self.a1, text = 'Total simulation time').grid(row=2,column=0, padx=5, pady=5)
        self.tst = tk.Entry(self.a1,  width=30)
        self.tst.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(self.a1, text = 'Iterations per second:').grid(row=3,column=0, padx=5, pady=5)
        self.ips = tk.Entry(self.a1,  width=30)
        self.ips.grid(row=3, column=1, padx=5, pady=5)
        
        tk.Label(self.a1, text = 'Interval length:').grid(row=4,column=0, padx=5, pady=5)
        self.il = tk.Entry(self.a1,  width=30)
        self.il.grid(row=4, column=1, padx=5, pady=5)
        
        self.listaentry = [self.rtps, self.dt, self.tst, self.ips, self.il]
        self.listaval = []
        def save():
            if not empty(self.listaentry) and num(self.listaentry):
                if not int(self.ips.get()) < 20:
                    for el in self.listaentry:
                        self.listaval.append(int(el.get()))
                    df = pd.DataFrame([self.listaval], columns = ['rtps','dt','tst','ips', 'il'])
                    df.to_csv('assets\configs.csv', index=False)
                    self.listaval = []
                    ad(self, 'Config updated', 'The configurations have been updated')
                    
                else:
                    ad(self, 'min value passed', 'The data of ips must be higher than 20')
            else:
                ad(self, 'Wrong data', 'Fill data correctly to be able to save')
        def defset():
            global defaultconfigs
            df = pd.DataFrame([defaultconfigs], columns = ['rtps','dt','tst','ips','il'])
            df.to_csv('assets\configs.csv', index=False)
            ad(self, 'Config updated', 'The configurations have been \n set to default')

            
        self.b1 = tk.Button(self.a2, text = '?', width=2, padx=5, pady=0, command = lambda: helpd(self,self.lista))
        self.b1.grid(row=0, column=0,padx=5, pady=5)
        
        self.b2 = tk.Button(self.a3, text = 'Save', width=6, padx=5, pady=0, command = lambda: save())
        self.b2.grid(row=0, column=0,padx=5, pady=5)
        
        self.b3 = tk.Button(self.a3, text = 'Reset', width=6, padx=5, pady=0, command = lambda: defset())
        self.b3.grid(row=0, column=1,padx=5, pady=5)
        
        self.b4 = tk.Button(self.a2, text = 'Converter', width=6, padx=5, pady=0, command = lambda: conversion(self))
        self.b4.grid(row=0, column=2,padx=5, pady=5)
        
        
        self.root.transient(papa.root)
        self.root.mainloop()
class main():
    def __init__(self):
        self.lista = [
            ['Name','It reffers to the numeric index of the object.'],
            ['mass', 'Mass in kg for the gravitational object.'],
            ['radio', 'Radio in meters of the object.'],
            ['x,y', 'Positional coordinates from origin in meters.'],
            ['vel', 'Velocity of the object in m/s.'],
            ['prad', 'Angle of the vector velocity in radians.']
            ]
        self.listaval = []
        self.listaindex = []
        self.root = tk.Tk()
        self.root.resizable(0,0)
        self.root.geometry('325x325')
        self.root.title('Gravity simulator')
        
        
        self.a1 = tk.Frame(self.root)
        self.a1.grid(row=1, column=0, sticky='nsew', pady=10)
        
        self.a2= tk.Frame(self.root)
        self.a2.grid(row=2, column=0, columnspan = 2, sticky='nsew')
        
        
        self.a3 = tk.Frame(self.root)
        self.a3.grid(row=0, column=0, sticky='nsew', pady=0)
        
        tk.Label(self.a1, text = 'name: ').grid(row=0,column=0, padx=5, pady=5)
        self.name = tk.Entry(self.a1,  width=40)
        self.name.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(self.a1, text = 'mass: ').grid(row=1,column=0, padx=5, pady=5)
        self.mass = tk.Entry(self.a1,  width=40)
        self.mass.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(self.a1, text = 'radio: ').grid(row=2,column=0, padx=5, pady=5)
        self.radio = tk.Entry(self.a1,  width=40)
        self.radio.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(self.a1, text = 'x: ').grid(row=3,column=0, padx=5, pady=5)
        self.x = tk.Entry(self.a1,  width=40)
        self.x.grid(row=3, column=1, padx=5, pady=5)
        
        tk.Label(self.a1, text = 'y: ').grid(row=4,column=0, padx=5, pady=5)
        self.y = tk.Entry(self.a1,  width=40)
        self.y.grid(row=4, column=1, padx=5, pady=5)
        
        tk.Label(self.a1, text = 'velocity: ').grid(row=5,column=0, padx=5, pady=5)
        self.vel = tk.Entry(self.a1,  width=40)
        self.vel.grid(row=5, column=1, padx=5, pady=5)
        
        tk.Label(self.a1, text = 'angle: ').grid(row=6,column=0, padx=5, pady=5)
        self.angle = tk.Entry(self.a1,  width=40)
        self.angle.grid(row=6, column=1, padx=5, pady=5)
        
        self.listaentry = [self.name,self.mass,
                           self.radio,self.x,self.y,
                           self.vel,self.angle]
                        
        def run():
            loclen = len(self.listaindex)
            if  loclen < 2:
                ad(self,'No data', 'There must be at least \n 2 objects to graph')
            elif loclen > 2:
                ad(self, 'Sorry', f':( The program currently works only \n for 2 objects please erase {loclen-2}')
            else:
                print(self.listaval)
                df = pd.DataFrame(self.listaval, columns = ['Name','mass','radio','x','y','vel','prad'])
                df.to_csv('assets\data.csv', index=False)
                ad(self,'Data obtained', 'To continue to graph the data press \'Ok\' \n Close the entire tab \n it might take a while')
                m.main()
        def runlast():
            if isfile('assets\\data.csv'):
                df = pd.read_csv('assets\\data.csv')
                df = df.values.tolist()
                if len(df) >= 2:
                    ad(self,'Data obtained', 'To continue to graph the data press \'Ok\' \n Close the entire tab \n it might take a while')
                    m.main()
                else:
                    ad(self,'No data', 'There must be at least \n 2 objects to graph')
            else:
                ad(self,'Not found', 'There is not last data source')
        def save():
            if not empty(self.listaentry) and num(self.listaentry[1::]):
                locname = self.name.get()
                if  locname in self.listaindex:
                    self.listaval.pop(self.listaindex.index(locname))
                    self.listaindex.pop(self.listaindex.index(locname))     
                self.listaval.append(list(v.get() for v in self.listaentry))
                self.listaindex.append(locname)
                ad(self,'Saved', f'"{locname}" saved correctly')
            else:
                ad(self, 'Wrong data', 'Fill data correctly to be able to save')
        def delete():
            locname = self.name.get()
            if  locname in self.listaindex:
                self.listaval.pop(self.listaindex.index(locname))
                self.listaindex.pop(self.listaindex.index(locname)) 
                ad(self, 'Deleted', f'The data of "{locname}" has been deleted')
            else:
                ad(self, 'Not found', f'The name "{locname}" does not exist')
        def clear():
            for v in self.listaentry:
                v.delete(0,"end")
                v.insert(0,'')
        
        self.b1 = tk.Button(self.a2, text = 'Run', width=6,padx=5,pady=0, command = lambda: run())
        self.b1.grid(row=0, column = 4, sticky = 'E',padx=5, pady=5)
        tk.Frame(self.a2, width = 20).grid(row=0, column = 0)
        self.b2 = tk.Button(self.a2, text = 'Save', width=6,padx=5,pady=0, command = lambda: save())
        self.b2.grid(row=0, column=1,padx=5, pady=5)
        
        self.b3 = tk.Button(self.a2, text = 'Delete', width=6,padx=5,pady=0, command = lambda: delete())
        self.b3.grid(row=0, column=2,padx=5, pady=5)
        
        self.b4 = tk.Button(self.a2, text = 'Clear', width=6,padx=5,pady=0, command = lambda: clear())
        self.b4.grid(row=0, column=3,padx=5, pady=5)
        
        self.b5 = tk.Button(self.a3, text = 'C', width=2, padx=5, pady=0, command = lambda: config(self))
        self.b5.grid(row=0, column=0,padx=5, pady=5)
        
        self.b6 = tk.Button(self.a3, text = '?', width=2, padx=5, pady=0, command = lambda: helpd(self,self.lista))
        self.b6.grid(row=0, column=1,padx=5, pady=5)
        
        self.b7 = tk.Button(self.a3, text = 'S', width=2, padx=5, pady=0, command = lambda: show(self))
        self.b7.grid(row=0, column=2,padx=5, pady=5)
        
        self.b8 = tk.Button(self.a3, text = 'Converter', width=6, padx=5, pady=0, command = lambda: conversion(self))
        self.b8.grid(row=0, column=3,padx=5, pady=5)
        
        self.b9 = tk.Button(self.a3, text = 'Run last', width=6, padx=5, pady=0, command = lambda: runlast())
        self.b9.grid(row=0, column=4,padx=5, pady=5)
        self.root.mainloop()

if __name__ == "__main__":
    main()