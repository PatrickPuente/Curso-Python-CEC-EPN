# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 19:19:51 2019

@author: CEC
"""

print("Serie De Fibonacci\n")
#a = int(input("Ingrese un numero: "))
#b = int(input("Ingrese otro numero: "))

def fib(n):
    a, b = 0, 1
    while a<n:
        print(a, end=' ')
        #c=a+b
        #a=b
        #b=c
        a, b = b, a+b
        
    print()
#fib(10000)
    