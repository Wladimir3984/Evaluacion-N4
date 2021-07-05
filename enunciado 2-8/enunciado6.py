import os
from math import pi        
def area_circulo(radio):
    return pi * (radio**2)
def perimetro_cuadrado(lado):
    return lado+lado+lado+lado

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def enunciado6():
    opcion=0
    while opcion!=3:
        clearConsole()
        opcion=0
        print("1. Calcular área de círculo.")
        print("2. Calcular perímetro cuadrado.")
        print("3. Salir")
        while True:
            try:
                opcion=int(input("=>"))
                if opcion>=1 or opcion<=3:
                    break
            except:
                print("Ingrese solo números.")

        if opcion==1:
            clearConsole()
            while True:
                try:
                    radio=float(input("Ingrese el radio del círculo=>"))
                    print(f"El área es de: {area_circulo(radio)}")
                    input("Presione ENTER para continuar...")
                    break
                except:
                    print("Ingrese solo números.")

        elif opcion==2:
            clearConsole()
            while True:
                try:
                    lado=float(input("Ingrese un lado del cuadrado=>"))
                    print(f"El perímetro es de: {perimetro_cuadrado(lado)}")
                    input("Presione ENTER para continuar...")
                    break
                except:
                    print("Ingrese solo números")
