from math import pi        
def area_circulo(radio):
    result=pi * (radio**2)
    print(result)
def perimetro_cuadrado(largo, alto):
    result=largo+largo+alto+alto
    print(result)
opcion=0

while opcion!=3:
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
        while True:
            try:
                radio=float(input("Ingrese el radio del círculo=>"))
                area_circulo(radio)
                break
            except:
                print("Ingrese solo números.")

    elif opcion==2:
        
        while True:
            try:
                largo=float(input("Ingrese largo del cuadrado=>"))
                break
            except:
                print("Ingrese solo números")

        while True:
            try:
                alto=float(input("Ingrese alto del cuadrado=>"))
                perimetro_cuadrado(alto, largo)
                break
            except:
                print("Ingrese solo números")