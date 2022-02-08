# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 14:30:37 2021

@author: Juan Antonio
"""

lista = []
listab = []
listac = []
'''
for a in range(52560):
    n = float(a)
    loc = float(a) / 7.2
    if loc % 1 == 0:
        lista.append(n)
        listac.append(n)
    elif loc % 1 < 0.12:
        listab.append(n)
        listac.append(n)
print(len(lista))
print(len(listab))
'''

for a in range(105120):
    n = float(a)
    loc = float(a) / 57.6
    if loc % 1 == 0:
        lista.append(n)
        listac.append(n)
    elif loc % 1 < 0.015:
        listab.append(n)
        listac.append(n)
print(len(lista))
print(len(listab))
print(len(listac))
print('meta 1825')
for n in range(len(listac)-1):
    '''
    print(listac[n+1], listac[n])
    
    print(listac[n+1] - listac[n])
    '''
    pass
    if listac[n+1] - listac[n] > 8:
        pass
