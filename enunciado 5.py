def comparacion(numero1, numero2):
    if numero1>numero2:
        return 1
    elif numero1<numero2:
        return -1
    elif numero1==numero2:
        return 0

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