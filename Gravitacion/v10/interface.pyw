# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 19:50:20 2021

@author: Juan Antonio

Title: Interfaz tkinter Gravitación sim

ver: 2.0
"""

import tkinter as tk
import pandas as pd
import myapp as m
from os.path import isfile
from tkinter import Tk
from tkinter import ttk


defaultconfigs = [60*60*24,60*10,60*60*24*365*2,20,500]

def cbu(text):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(text)
    r.update()
    r.destroy()
def conv(papa,n):
    try:
        lista = n.split('*')
        loc = lista[-1]
        exp = None
        if 'e' in loc:
            lista.pop(-1)
            lista.append(loc[0:loc.index('e')])
            exp = loc[loc.index('e')+1::]
        mult = 1
        for n in lista:
            mult *= float(n)
        if exp != None:
            return mult * (10**int(exp))
        else:
            return mult
    except:
        ad(papa, 'Wrong format', 'The format of the operation \n is incorrect.')
        return None
    
def clear(lista):
    for v in lista:
        v.delete(0,"end")
        v.insert(0,'')
        
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
        self.root.iconbitmap('assets\logo.ico')
        
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
        self.listahelp = [
            ['VARIABLES', None],
            ['\'*\' symbol','Symbol equivalent to multiply.'],
            ['\'e\' symbol', 'Symbol equivalent to x * 10 ** n.'],
            ['BUTTONS', None],
            ['Conv to cboard', 'Copies the operation to the clipboard'],
            ['Conv to empty', 'Copies the operation to the next empty \n entry of the converter opener.']
            ]
        
        self.root = tk.Toplevel(papa.root)
        self.root.resizable(0,0)
        self.root.title('Converter')
        self.root.iconbitmap('assets\logo.ico')
        
        self.a1 = tk.Frame(self.root, width = 220, height = 200)
        self.a1.grid(row=1, column=0, sticky='nsew', pady=10)
        
        self.a2 = tk.Frame(self.root)
        self.a2.grid(row=0, column=0, sticky='nsew', pady=0)
        
        self.a3 = tk.Frame(self.root)
        self.a3.grid(row=2, column=0, sticky='nsew', pady=0)
        
        self.op = tk.Entry(self.a1,  width=30)
        self.op.grid(row=2, column=1, padx=5, pady=0)
        self.lista = papa.listaentry
        
        
        def convloc():
            d = conv(self, self.op.get())
            if d != None:
                self.op.delete(0,"end")
                self.op.insert(0,d) 
        def copy():
            d = conv(self, self.op.get())
            if d != None:
                self.op.delete(0,"end")
                self.op.insert(0,d) 
                loc = True
                for el in self.lista:
                    if el.get() == '':
                        el.insert(0,self.op.get())
                        loc = False
                        break
                if loc:
                    ad(self,'No empty fields', 'There is no empty entry to copy.')
        def cbuloc():
            convloc()
            cbu(self.op.get())
            
        self.b1 = tk.Button(self.a2, text = 'Conv to cboard', width=10, padx=5, pady=0, command = lambda: cbuloc())
        self.b1.grid(row=0, column=1,padx=5, pady=5)
        
        
        self.b2 = tk.Button(self.a2, text = '?', width=2, padx=5, pady=0, command = lambda: helpd(self,self.listahelp))
        self.b2.grid(row=0, column=0,padx=5, pady=5)
        
        self.b3 = tk.Button(self.a3, text = 'Conv to empty', width=10, padx=5, pady=0, command = lambda: copy())
        self.b3.grid(row=0, column=0,padx=5, pady=5)
        
        self.b4 = tk.Button(self.a3, text = 'Clear', width=10, padx=5, pady=0, command = lambda: clear([self.op]))
        self.b4.grid(row=0, column=1,padx=5, pady=5)
        
        self.b5 = tk.Button(self.a2, text = 'Op', width=2, padx=5, pady=0, command = lambda: convloc())
        self.b5.grid(row=0, column=2,padx=5, pady=5)
        self.root.transient(papa.root)
        self.root.mainloop()
def show(papa, lista = None):
    if lista == None:
        if isfile('assets\\data.csv') :
            
            df = pd.read_csv('assets\\data.csv')
            df = df.values.tolist()
            t = 'Last data'
        else: 
            ad(papa, 'Not found', 'There is not last data source.')
            
    else:
        df = lista
        t = 'Current data'
    lista = []
    relative = ['mass','radio','x','y','vel','prad']
    if lista == None and not isfile('assets\\data.csv'):
        pass
    else:
        if df == []:
            ad(papa, 'No data yet', 'Fill the data to see the current.')
        else:
            for el in df:
                loc = ''
                for n,e in enumerate(el[1::]):
                    loc += f'{relative[n]}: {str(e)} \n'
                lista.append([el[0], loc])
            lista = [['VALUES', None]] + lista
            helpd(papa,lista, name = t)
             
class helpd():
    def __init__(self,papa,helps,name = None):
        if name == None:
            name = 'Help'
        self.root = tk.Toplevel(papa.root)
        self.root.resizable(0,0)
        self.root.title(name)
        self.root.iconbitmap('assets\logo.ico')
        
        self.alist = [tk.Frame(self.root)]
        loc = 0
        setv = 0
        listac = 0
        for n,h in enumerate(helps):
            if h[1] == None:
                setv = 2
                loc += 1
                listac += 1
                ttk.Separator(self.root, orient=tk.VERTICAL).grid(row = 0, column = loc, rowspan=20, sticky='ns')
                loc += 1
                self.alist.append(tk.Frame(self.root))
                self.alist[listac].grid(row = 0, column = loc, sticky='nsew', pady=5)
                tk.Label(self.alist[listac], text = f'{h[0]}').grid(row = 0, column = 0,columnspan = 2, padx=5, pady=5)
                ttk.Separator(self.alist[listac], orient=tk.HORIZONTAL).grid(row = 1, column = 0, columnspan=2, sticky='we')
            else:
                tk.Label(self.alist[listac], text = f'{h[0]}:').grid(row = setv, column = 0, padx=5, pady=5)
                tk.Label(self.alist[listac], text = h[1]).grid(row = setv, column = 1, padx=5, pady=5)
                setv += 1
class config():
    def __init__(self,papa):
        self.lista = [
            ['VARIABLES', None],
            ['Real ex time per sec','It expresses how much time of simulation is going to be represented \n as a second in real time. \n 60*60*24 is the default.'],
            ['Integral sums interval', 'It expresses the time of simulation that passes between an update of data. \n 60*10 seconds is the default.'],
            ['Total simulation time', 'It expresses the total time that passes in a simulation. \n 60*60*24*365*2 seconds is the default.'],
            ['Iterations per second', 'It expresses the speed of update of the simulation per seconds. \n 20 i/s is the default and the min value accepted.'],
            ['Interval length', 'It expresses how many iterations are going to be shown at the same time. \n  500 is the default, the interval is 1 <= x <= 1000.'],
            ['Conversions', 'To see the conversion operators go to \'?\' \n in the section of \'converter\'.'],
            ['Note', 'The user can use conversion operators directly \n inside the entry sets.'],
            ['BUTTONS', None],
            ['Converter', 'Opens a exponential an multiplication converter.'],
            ['Save', 'Updates the local database of configs \n with the current entries.'],
            ['Reset', 'Set the configurations to it default value.'],
            ['Clear', 'Clears the entry sets.']
            ]
        self.root = tk.Toplevel(papa.root)
        self.root.resizable(0,0)
        self.root.title('config')
        self.root.iconbitmap('assets\logo.ico')
        
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
        
        if isfile('assets\\configs.csv'):
            df = pd.read_csv('assets\\configs.csv')
            dfl = df.values.tolist()[0]
            for n,el in enumerate(dfl):
                self.listaentry[n].insert(0,el)
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
        
        self.b5 = tk.Button(self.a3, text = 'Clear', width=6, padx=5, pady=0, command = lambda: clear(self.listaentry))
        self.b5.grid(row=0, column=2,padx=5, pady=5)
        
        self.root.transient(papa.root)
        self.root.mainloop()
class main():
    def __init__(self):
        self.lista = [
            ['VARIABLES', None],
            ['Name','It reffers to the numeric index of the object.'],
            ['Mass', 'Mass in kg for the gravitational object.'],
            ['Radio', 'Radio in meters of the object.'],
            ['x,y', 'Positional coordinates from origin in meters.'],
            ['Vel', 'Velocity of the object in m/s.'],
            ['Angle', 'Angle of the vector velocity in radians.'],
            ['Conversions', 'To see the conversion operators go to \'?\' \n in the section of \'converter\'.'],
            ['Note', 'The user can use conversion operators directly \n inside the entry sets.'],
            ['BUTTONS', None],
            ['C', 'Opens the initial configs modifier.'],
            ['Converter', 'Opens a exponential an multiplication converter.'],
            ['Last', 'Opens a view of the last data simulated.'],
            ['Load', 'Updates the local database with the values of \n the last simulations.'],
            ['Run last', 'Runs a simulations with the last values used.'],
            ['Save', 'Updates the local database with the current entries.'],
            ['Delete', 'Erases, if exists, the values of the data base \n with the index of \'Name\'.'],
            ['Clear', 'Clears the entry sets.'],
            ['Current', 'Oopens a view of the current local database.'],
            ['Run', 'Runs a simulation with the current values of the local \n database.']
            ]
        self.listaval = []
        self.listaindex = []
        self.root = tk.Tk()
        self.root.resizable(0,0)
        self.root.title('Gravity simulator')
        self.root.iconbitmap('assets\logo.ico')
        
        self.a1 = tk.Frame(self.root)
        self.a1.grid(row=1, column=0, sticky='nsew', pady=10)
        
        self.a2= tk.Frame(self.root)
        self.a2.grid(row=2, column=0, columnspan = 2, sticky='nsew')
        
        
        self.a3 = tk.Frame(self.root)
        self.a3.grid(row=0, column=0, sticky='nsew', pady=0)
        
        tk.Label(self.a1, text = 'Name: ').grid(row=0,column=0, padx=5, pady=5)
        self.name = tk.Entry(self.a1,  width=40)
        self.name.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(self.a1, text = 'Mass: ').grid(row=1,column=0, padx=5, pady=5)
        self.mass = tk.Entry(self.a1,  width=40)
        self.mass.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(self.a1, text = 'Radio: ').grid(row=2,column=0, padx=5, pady=5)
        self.radio = tk.Entry(self.a1,  width=40)
        self.radio.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(self.a1, text = 'x: ').grid(row=3,column=0, padx=5, pady=5)
        self.x = tk.Entry(self.a1,  width=40)
        self.x.grid(row=3, column=1, padx=5, pady=5)
        
        tk.Label(self.a1, text = 'y: ').grid(row=4,column=0, padx=5, pady=5)
        self.y = tk.Entry(self.a1,  width=40)
        self.y.grid(row=4, column=1, padx=5, pady=5)
        
        tk.Label(self.a1, text = 'Velocity: ').grid(row=5,column=0, padx=5, pady=5)
        self.vel = tk.Entry(self.a1,  width=40)
        self.vel.grid(row=5, column=1, padx=5, pady=5)
        
        tk.Label(self.a1, text = 'Angle: ').grid(row=6,column=0, padx=5, pady=5)
        self.angle = tk.Entry(self.a1,  width=40)
        self.angle.grid(row=6, column=1, padx=5, pady=5)
        
        self.listaentry = [self.name,self.mass,
                           self.radio,self.x,self.y,
                           self.vel,self.angle]
                        
        def run():
            loclen = len(self.listaindex)
            if  loclen < 2:
                ad(self,'No data', 'There must be at least \n 2 objects to graph')
            else:
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
            if not empty(self.listaentry):
                locname = self.name.get()
                if  locname in self.listaindex:
                    self.listaval.pop(self.listaindex.index(locname))
                    self.listaindex.pop(self.listaindex.index(locname))  
                    
                updatelist = []
                
                for n in self.listaentry[1::]:
                    updatelist.append(conv(self,n.get()))
                if not None in updatelist:
                    self.listaval.append(list(v for v in [self.listaentry[0].get()] + updatelist))
                    self.listaindex.append(locname)
                    ad(self,'Saved', f'"{locname}" saved correctly')
            else:
                ad(self, 'Wrong data', 'Fill data correctly to be able to save')
                
        def loadlast():
            if isfile('assets\\data.csv'):
                df = pd.read_csv('assets\\data.csv')
                df = df.values.tolist()
                self.listaval = df
                self.listaindex = []
                for el in self.listaval:
                    self.listaindex.append(el[0])
                ad(self,'Data loaded', 'The last data source has been set \n as current.')
            else:
                ad(self,'Not found', 'There is not last data source')
            
        def delete():
            locname = self.name.get()
            if  locname in self.listaindex:
                self.listaval.pop(self.listaindex.index(locname))
                self.listaindex.pop(self.listaindex.index(locname)) 
                ad(self, 'Deleted', f'The data of "{locname}" has been deleted')
            else:
                ad(self, 'Not found', f'The name "{locname}" does not exist')
        
        self.b1 = tk.Button(self.a2, text = 'Run', width=6,padx=5,pady=0, command = lambda: run())
        self.b1.grid(row=0, column = 4, sticky = 'E',padx=5, pady=5)
        tk.Frame(self.a2, width = 20).grid(row=0, column = 0)
        self.b2 = tk.Button(self.a2, text = 'Save', width=6,padx=5,pady=0, command = lambda: save())
        self.b2.grid(row=0, column=0,padx=5, pady=5)
        
        self.b3 = tk.Button(self.a2, text = 'Delete', width=6,padx=5,pady=0, command = lambda: delete())
        self.b3.grid(row=0, column=1,padx=5, pady=5)
        
        self.b4 = tk.Button(self.a2, text = 'Clear', width=6,padx=5,pady=0, command = lambda: clear(self.listaentry))
        self.b4.grid(row=0, column=2,padx=5, pady=5)
        
        self.b5 = tk.Button(self.a3, text = 'C', width=2, padx=5, pady=0, command = lambda: config(self))
        self.b5.grid(row=0, column=0,padx=5, pady=5)
        
        self.b6 = tk.Button(self.a3, text = '?', width=2, padx=5, pady=0, command = lambda: helpd(self,self.lista))
        self.b6.grid(row=0, column=1,padx=5, pady=5)
        
        self.b7 = tk.Button(self.a3, text = 'Last', width=2, padx=5, pady=0, command = lambda: show(self))
        self.b7.grid(row=0, column=3,padx=5, pady=5)
        
        self.b8 = tk.Button(self.a3, text = 'Converter', width=6, padx=5, pady=0, command = lambda: conversion(self))
        self.b8.grid(row=0, column=2,padx=5, pady=5)
        
        self.b9 = tk.Button(self.a3, text = 'Run last', width=6, padx=5, pady=0, command = lambda: runlast())
        self.b9.grid(row=0, column=5,padx=5, pady=5)
        
        self.b10 = tk.Button(self.a3, text = 'Load last', width=6, padx=5, pady=0, command = lambda: loadlast())
        self.b10.grid(row=0, column=4,padx=5, pady=5)
        
        self.b11 = tk.Button(self.a2, text = 'Current', width=6, padx=5, pady=0, command = lambda: show(self, lista = self.listaval))
        self.b11.grid(row=0, column=3,padx=5, pady=5)
        self.root.mainloop()

if __name__ == "__main__":
    main()