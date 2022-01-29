# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 07:34:50 2021

@author: Juan Antonio

Title: Gravitación sim

ver: 1.0
"""

import functions as f


r = 6371*(10**3)+ 400*(10**3)
masaT = 5.972 * (10**24)
masa2 = 1
aceT = f.aceleraciong(masaT, r)

print(aceT)

print(f.vtan(aceT,r))
