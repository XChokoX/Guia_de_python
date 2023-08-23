# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 11:52:23 2023

@author: Lab-105_Pc10
"""
print("1) centrimero -> pulgadas")
print("2) metros -> kilometros")
print("3) onzas-> gramos")
print("4) milla -> kilometros")
print("5) celcius -> fahrenheit")
print("6) salir")

entrada = True


while(entrada == True):

    metodo = input("metodo: ")
    metodo = int(metodo)

    
    if(metodo == 1):
        medida = input("Ingrese los centimetros: ")
        medida = float(medida)
        medida = medida * 0.39370
        print(f" {medida} pulgadas")

    elif(metodo == 2):
        medida = input("Ingrese los metros: ")
        medida = float(medida)
        medida = medida / 1000
        print(f" {medida} kilometros")

    elif(metodo == 3):
        medida = input("Ingrese las onzas: ")
        medida = float(medida)
        medida = medida * 28.349523125
        print(f" {medida} gramos")

    elif(metodo == 4):
        medida = input("Ingrese las millas: ")
        medida = float(medida)
        medida = medida / 0.62137
        print(f" {medida} kilometros")

    elif(metodo == 5):
        medida = input("Ingrese sus grados celsis: ")
        medida = float(medida)
        medida = ((medida * 9) / 5) + 32
        print(f" {medida} fahrenheit")
        
    elif(metodo == 6):
        entrada = False
        print("Adios")
        
    else:
        print("Ingrese un metodo corecto")
        