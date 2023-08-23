# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 14:16:20 2023

@author: Choko
"""
while(True):
    palabra = input("Ingrse su primera palabra: ")
    palabra = palabra[::-1]
    largo = len(palabra)

    if(largo >= 3):
        break

while(True):
    palabra_b = input("Ingrse su segunda palabra: ")
    palabra_b = palabra_b[::-1]
    largo = len(palabra_b)

    if(largo >= 3):
        break

contador = 0

for i in range(0,3):
   
    if(palabra[i] == palabra_b[i]):
        contador = contador + 1
    
    else:
        break
        
if(contador == 3):
    print("Rima")

if(contador == 2):
    print("Rima poco")

else:
    print("No riman")

