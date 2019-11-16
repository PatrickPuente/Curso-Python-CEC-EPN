# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 09:53:03 2019

@author: CEC
"""
file = open("devices.txt", "a")
while True:
    newItem = input("ingrese un nuevo item: ")
    if newItem == "exit":
        print("All done!")
        break
    else:
        file.write(newItem + "\n")
file.close()
