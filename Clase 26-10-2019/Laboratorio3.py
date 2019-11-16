# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:07:21 2019

@author: CEC
"""
#Micodigo Definicion de Funcion
def isYearLeap(year):
 if year%4==0:     
     if year%100==0:         
         if year%400==0:
             return True
         else:
             return False
     else:
         return True
 else:
     return False
     

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
