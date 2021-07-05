import numpy as np
from time import sleep
import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
def enunciado3():
    print("Bienvenido al juego, adivina el número")
    while True:
        try:
            rango=int(input("Ingresa el rango máximo de los números(>19): "))
            if rango<20 or rango>=999999:
                clear()
                print("Ingrese un rango correcto.")
                sleep(2)
                clear()
            else:
                arreglo=np.random.randint(0, rango+1, (2, 5))
                break
        except:
            clear()
            print("Solo números enteros.")
            sleep(2)
            clear()
            

    while True:
        clear()
        try:
            adivina=int(input(f"Adivina uno de los 10 números entre 0 y {rango}: "))
            if adivina<0 or adivina>rango:
                print("Ingresa un valor correcto, así nunca ganarás.")
            else:
                break
        except:
            clear()
            print("Solo números.")
            sleep(2)
            clear()

    for x in range(2):
        for j in range(5):
            if adivina==arreglo[x][j]:
                print("Felicidades. Ganaste")
                input("Presione enter para continuar...")
                break
        else:
            if x==1 and j==4 and adivina!=arreglo[x][j]:
                print("Te equivocaste, estos eran los números")
                print(arreglo)
                input("Presione enter para continuar...")
            continue
        break