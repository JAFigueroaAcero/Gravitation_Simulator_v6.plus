# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 19:50:20 2021

@author: Juan Antonio

Title: Interfaz tkinter Gravitación sim

ver: 1.0
"""

import tkinter as tk
import pandas as pd
import launch as l
class ad():
    def __init__(self,papa,titulo,texto):
        self.root= tk.Toplevel(papa.root)
        self.root.resizable(0,0)
        self.root.geometry('220x100')
        self.root.title(titulo)
        self.a1=tk.Frame(self.root,width=200, height=100)
        self.a1l=tk.Label(self.a1, text=texto, anchor="center")
        self.a1l.grid(row=1,column=0, pady=10)
        self.b1=tk.Button(self.a1, width=3, height=1 ,text='Ok', command= self.root.destroy)
        self.b1.grid(row=3,column=0, sticky='nsew')
        self.a1.pack()
        self.root.transient(papa.root)
        self.root.mainloop()

class main():
    def __init__(self):
        self.listaval = []
        self.listaindex = []
        self.root = tk.Tk()
        self.root.resizable(0,0)
        self.root.geometry('325x280')
        self.root.title('Gravity simulator')
        
        
        self.a1 = tk.Frame(self.root)
        self.a1.grid(row=1, column=0, sticky='nsew', pady=10)
        
        self.a2= tk.Frame(self.root)
        self.a2.grid(row=2, column=0, columnspan = 2, sticky='nsew')
        
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
       #         ad(self,'WARNING', 'Remember to close the sim with the \n stop button')
                self.root.after(2000,l.main())
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
        self.root.mainloop()

main()
        