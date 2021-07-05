def comparacion(numero1, numero2):
    if numero1>numero2:
        return 1
    elif numero1<numero2:
        return -1
    elif numero1==numero2:
        return 0

def enunciado5():
    while True:
        try:
            numero1=int(input("1. Ingrese un número entero=>"))
            break
        except:
           print("")
           print("Ingrese solo números enteros.")
           print("")
    while True:
        try:
            numero2=int(input("2. Ingrese un número entero=>"))
            break
        except:
           print("")
           print("Ingrese solo números enteros.")
           print("")
    print("")       
    print(f"Comparación : {comparacion(numero1, numero2)}")
    print("")
    input("Presione ENTER para continuar")