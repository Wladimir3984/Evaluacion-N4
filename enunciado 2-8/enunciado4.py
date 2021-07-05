import numpy as np
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def enunciado4():
    while True:
        try:
            numero1=int(input("Ingrese un número entre 3 y 6 (FILA): "))
            if numero1>=3 and numero1<=6:
                break
            else:
                print("Entre 3 y 6")
        except:
            print("Solo números.")

    while True:
        try:
            numero2=int(input("Ingrese un número entre 3 y 6 (COLUMNA): "))
            if numero2>=3 and numero2<=6:
                break
            else:
                print("Entre 3 y 6")
        except:
            print("Solo números.")
    clearConsole()
    arreglo=np.zeros([numero1,numero2])
    print(arreglo)

    for x in range(numero1):
        for y in range(numero2):
            while True:
                try:
                    num=float(input(f"Ingrese numero[{x}][{y}] : "))
                    arreglo[x][y]=num
                    clearConsole()
                    print(arreglo)
                    break
                except:
                    print("Solo números.")
    suma=0
    print("")
    for fila in range(numero1):
        suma=sum(arreglo[fila])
        print(f"La suma de la fila {fila+1} es {round(suma,1)}")
    print("")

    suma=0
    for columna in range(numero1):
        suma+=arreglo[columna]
    total=np.round((suma/numero1), decimals=1)
    print("="*100)
    print("")
    i = 0
    for prom in total:
        print(f"El promedio de la columna {i+1} es de {prom}")
        i+=1
    print("")
    input("Presione ENTER para salir...")