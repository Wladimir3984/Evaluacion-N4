import numpy as np
import os
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

while True:
    try:
        numero1=int(input("Ingrese un número entre 3 y 6: "))
        if numero1>=3 and numero1<=6:
            break
        else:
            print("Entre 3 y 6")
    except:
        print("Solo números.")

while True:
    try:
        numero2=int(input("Ingrese un número entre 3 y 6: "))
        if numero2>=3 and numero2<=6:
            break
        else:
            print("Entre 3 y 6")
    except:
        print("Solo números.")

arreglo=np.zeros([numero1,numero2])
print(arreglo)

for x in range(numero1):
    for y in range(numero2):
        while True:
            try:
                num=int(input("Ingrese numero: "))
                arreglo[x][y]=num
                clearConsole()
                print(arreglo)
                break
            except:
                print("Solo números.")
suma=0
for fila in range(len(arreglo)):
    suma+=arreglo[fila]
print("="*100)
print(f"Las sumas por fila de cada fila es :{suma}")

suma=0
for columna in range(numero1):
    suma+=arreglo[columna]
print("="*100)
print(f"Los promedios de las columnas son : {suma/numero1}")