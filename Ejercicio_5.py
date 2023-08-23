# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 12:45:10 2023

@author: Lab-105_Pc10
"""

palabra = input("Ingrese una palabra: ")
palabra = palabra.lower()

letra = input("Ingrese una letra: ")

contador = 0

for i in palabra:
    #print(f"{i}")
    
    if(i == letra):
        contador = contador + 1
        


print(f"{contador}")