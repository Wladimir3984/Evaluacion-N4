import numpy as np

def enunciado3():
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