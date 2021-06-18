import numpy as np
import os
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

while True:
    clearConsole()
    print("Bienvenido al juego, adivina el número")
    while True:
        try:
            rango=int(input("Ingresa el rango máximo de los números: "))
            if rango<0 or rango>=999999:
                print("Ingrese un rango correcto.")
            else:
                break
        except:
            print("Solo números.")

    arreglo=np.random.randint(0, rango, size=10)        

    while True:
        try:
            adivina=int(input("Adivina uno de los 10 números: "))
            if adivina<0 or adivina>rango:
                print("Ingresa un valor correcto, así nunca ganarás.")
            else:
                break
        except:
            print("Solo números")

    for x in range(10):
        if adivina==arreglo[x]:
            print("Felicidades. Ganaste")
            input("Presione enter para continuar...")
            break
        elif x==9 and adivina!=arreglo[x]:
            print("Te equivocaste, estos eran los números")
            print(arreglo)
            input("Presione enter para continuar...")