# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:43:56 2019

@author: 1-26-PB-L2-13
"""

devices=["R1","R2","R3","S1","S2"]

    
switches=[]
print(switches)
for item in devices:
    if "S" in item:
        switches.append(item)

print(switches)