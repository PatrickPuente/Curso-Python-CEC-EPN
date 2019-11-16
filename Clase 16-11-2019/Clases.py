# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 08:18:50 2019

@author: CEC
"""


class Empployee:
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Empployee.empCount += 1
        def displayCount(self):
            print("Total employee %d")%Empployee.empCount
        def displayEmployee(self):
            print("Name: {}, Salary: {}".format(self.name, self.salary))

emp1 = Empployee("Zara", 2000)
emp2 = Empployee("Manni", 5000)