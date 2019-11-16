# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:21:55 2019

@author: 1-26-PB-L2-13
"""

nativeVLAN=1
dataVLAN=100

if nativeVLAN==dataVLAN:
    print("The native VLAN and the data VLAN are the same")
else:
    print("The native VLAN and the data VLAN are different")
    

a=int(input("Cual es el numero de IPv4: "))
if a>=1 and a<=99:
    print("Es un estandar IPv4")
elif a>=100 and a<=199:
    print("Es una extencion IPv4")
else:
    print("Este valor no es un estandar o extension de IPv4 ACL")
 