# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:47:17 2019

@author: 1-26-PB-L2-13
"""

x=input("Enter a number to count to: ")
x=int(x)
y=1
while y<=x:
    print(y)
    y=y+1


x=input("Enter a number to count to: ")
x=int(x)
y=1
while True:
    print(y)
    y=y+1
    if y>x:
        break
