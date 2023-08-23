# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 14:28:58 2023

@author: Choko
"""

diccionario = {}
total = 0

while(True):
    
    articulo = input("Nombre del articulo: ")
    precio = input("Ingrese el valor del articulo: ")
    precio = float(precio)
    
    
    diccionario[articulo] = precio
    
    total = precio + total
    

    seguir = input("\n¿Quiere agregar otro producto (si / no)?:  ")
    
    if(seguir == "no"):
        break


print("Lista de compra ")
for llave, valor in diccionario.items():
    print(f"Articulo = {llave} / Precio = {valor}")


print(f"Precio total de la comproa: {total}")

