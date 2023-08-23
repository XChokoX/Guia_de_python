# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 12:19:15 2023

@author: Lab-105_Pc10
"""

numero = input("Ingrse un numero: ")
numero = int(numero)
contador = 0

for i in range(1,numero+1,1):
  ##  print(f"{i}")
        
    if(numero % i == 0):
        contador = contador + 1
print(f"{contador}")

if(contador < 3):
    print("es un  numero primo")

else:
    print("No es un numero primo")      
    
