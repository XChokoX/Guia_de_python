# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 13:26:04 2023

@author: Lab-105_Pc10
"""

palabras = ["Hola", "Como estas" , "adiosssss" , "ayuda"]

cantidaPalabras = []
contador = 0
indice = 0
auxiliar = 0

for i in palabras:
    i = i.replace()    
    cantidad = len(i)
    
    print(f"{cantidad}")    
    
    if(cantidad > auxiliar):
        auxiliar = cantidad
        indice = contador
    
    contador = contador + 1
    

