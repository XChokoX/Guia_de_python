# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 13:14:18 2023

@author: Lab-105_Pc10
"""

def area_circulo(x):
    
    a = x**2
    operacion = 3.14 * a

    
    print(f"Area: {operacion}")
   
   
    return operacion

def volumen(k,t):
    
    ñ = k * t
    print(f"Volumen: {ñ}")
    
    return

radio = input("Ingrese el valor radio del circulo: ")
radio = float(radio)

area_circulo(radio)

altura = input("Ingrese la altura de su cilindo: ")
altura = float(altura)

radioc = input("Ingrese el valor radio del circulo: ")
radioc = float(radioc)

s = area_circulo(radioc)

volumen(s,altura)
