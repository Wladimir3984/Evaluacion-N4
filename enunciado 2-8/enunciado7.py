def enunciado7():
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