# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 11:28:19 2023

@author: Lab-105_Pc10
"""
import random

numeroRandom = random.randint(0, 10)

entrada = True
contador = 0

while(entrada  == True):
    
    numero = input("Ingrese un numero: ")
    numero = int(numero)
    
    if(numero == numeroRandom):
        print("Valor encontrado")
        entrada = False
    
    elif(numero > numeroRandom):
        print("el numero es mas pequeño")
    
    elif(numero < numeroRandom):
        print("el numero mas grande")