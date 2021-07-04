import numpy as np
import os
from math import pi

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#LISTAS ENUNCIADO 2
nombres=["Pablo", "Pedro", "Luis", "Ana", "Lisa", "Carmen", "Jorge", "Victor", "Jorge"]
nombres2=["Jorge", "Lisa", "Pedrinho", "Ana", "Juan", "Diego", "Victor", "Jorge"]
repetidos=[]

#FUNCIÓN COMPARACIÓN ENUNCIADO 5 (OPCION 4)
def comparacion(numero1, numero2):
    if numero1>numero2:
        return 1
    elif numero1<numero2:
        return -1
    elif numero1==numero2:
        return 0

#FUNCIÓN AREA-PERIMETRO ENUNCIADO 6 (OPCION 5)
def area_circulo(radio):
    return pi * (radio**2)
def perimetro_cuadrado(largo, alto):
    return largo+largo+alto+alto



opcion=0
while opcion!=8:
    clearConsole()
    opcion=0 
    print("="*100)
    print("1. Enunciado 2\n2. Enunciado 3\n3. Enunciado 4\n4. Enunciado 5\n5. Enunciado 6\n6. Enunciado 7\n7. Enunciado 8\n8. Salir")
    print("="*100)
    while opcion<1 or opcion>8:
        try:
            opcion=int(input("=>"))
            if opcion<1 or opcion>8:
                print("Ingrese una opción válida.")
        except:
            print("Ingrese solo números.")

    if opcion==1: #ENUNCIADO 2
        clearConsole()
        print(f"Las listas son:\n1. {nombres}\n2. {nombres2}")
        for x in range(len(nombres)):
            for y in range(len(nombres2)):
                if nombres[x]==nombres2[y] and nombres[x] not in repetidos:
                    repetidos.append(nombres[x])            
        print(f"Los nombres repetidos son: {repetidos}")
        input("Presione ENTER para continuar...")
    


    elif opcion==2: #ENUNCIADO 3
        clearConsole()
        print("Bienvenido al juego, adivina el número")
        while True:
            try:
                rango=int(input("Ingresa el rango máximo de los números: "))
                if rango<0 or rango>=999999:
                    print("Ingrese un rango correcto.")
                else:
                    arreglo=np.random.randint(0, rango, (2, 5))
                    break
            except:
                print("Solo números mayores a 1.")

        while True:
            try:
                adivina=int(input("Adivina uno de los 10 números: "))
                if adivina<0 or adivina>rango:
                    print("Ingresa un valor correcto, así nunca ganarás.")
                else:
                    break
            except:
                print("Solo números")

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


    elif opcion==3: #ENUNCIADO 4
        clearConsole()
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
        for fila in range(numero1):
            suma=sum(arreglo[fila])
            print(f"La suma de la fila {fila+1} es {round(suma)}")
        input("Presione ENTER para continuar...")

        suma=0
        for columna in range(numero1):
            suma+=arreglo[columna]
        total=np.round((suma/numero1), decimals=1)
        print("="*100)
        print(f"El promedio de cada columna es de {total}")
        input("Presione ENTER para continuar...")
    

    elif opcion==4: #ENUNCIADO 5
        clearConsole()
        while True:
            try:
                numero1=int(input("1. Ingrese un número entero=>"))
                break
            except:
                print("Ingrese solo números.")

        while True:
            try:
                numero2=int(input("2. Ingrese un número entero=>"))
                break
            except:
                print("Ingrese solo números")

        print(f"Comparación : {comparacion(numero1, numero2)}")
        input("Presione ENTER para continuar")
    
    elif opcion==5: #ENUNCIADO 6
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
                        largo=float(input("Ingrese largo del cuadrado=>"))
                        break
                    except:
                        print("Ingrese solo números")

                while True:
                    try:
                        alto=float(input("Ingrese alto del cuadrado=>"))
                        print(f"El perímetro es de: {perimetro_cuadrado(largo, alto)}")
                        input("Presione ENTER para continuar...")
                        break
                    except:
                        print("Ingrese solo números")
    
    elif opcion==6: #ENUNCIADO 7
        clearConsole()
        while True:
            try:
                y=int(input("Ingrese un número entre 10 y 15 =>"))
                if y>=10 and y<=15:
                    break
                else:
                    print("Ingrese un número dentro del rango.")
            except:
                print("Ingrese solo números enteros.")

        x=0
        for fibo in range(y):
            z=x+y
            y=x
            x=z
            print(z)
        
        input("Presione ENTER para continuar...")
    
    elif opcion==7: #ENUNCIADO 8
        clearConsole()
        while True:
            palabra=input("Ingrese una palabra=> ").lower()
            palabra2 = "" #sumador de letras al revés
            contador=0 #contador de letras
            if palabra.replace(" ", "").isalpha(): #omitir espacios y validar que sean solo letras
                for i in palabra.replace(" ", ""): #recorrer palabra omitiendo espacios
                    contador+=1 #contar letras
                    palabra2= i + palabra2 #añadir letra en reversa
                
                if palabra.replace(" ", "") == palabra2: #comparar palabras sin espacios
                    print(f"{palabra} es un palíndromo. Tiene {contador} letras") #resultado => palabra normal y la suma de únicamente sus letras
                    input("Presione ENTER para continuar...")
                    break
                else:
                    print(f"{palabra} no es un palíndromo. Tiene {contador} letras")
                    input("Presione ENTER para continuar...")
                    break
            else:
                print("Ingrese solo letras.")