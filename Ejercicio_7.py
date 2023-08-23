# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 14:08:20 2023

@author: Choko
"""

numero = input("Ingrese un valor: ")
numero = int(numero)
auxiliar = 1

if(numero > 0):
    for i in range(1,numero+1):
       
       
       auxiliar = i * auxiliar 
       print(f"{auxiliar}")


else:
    print("El valor tiene que ser mayor a 0")
    

