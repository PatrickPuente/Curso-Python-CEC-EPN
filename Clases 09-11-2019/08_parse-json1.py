# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 12:28:20 2019

@author: CEC
"""

import urllib.parse
import requests


main_api="https://www.mapquestapi.com/directions/v2/route?"
orig="Washington"
dest = "Baltimaore"
key="yEVp6k4jMgDo899V9Nsd3p4faI713flh"
'''url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
json_data = requests.get(url).json()
print(json_data)'''

#json 2

'''print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status ==0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")'''

#json 3
while True:
    orig = input("Starting Location: ")
    dest = input("Destination: ")
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))