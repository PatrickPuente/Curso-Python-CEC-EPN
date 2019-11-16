# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:54:42 2019

@author: 1-26-PB-L2-13
"""

while True:
    x=input("Ingresar un numero para contar: ")
    if x=='q'or x =='quiet':
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break