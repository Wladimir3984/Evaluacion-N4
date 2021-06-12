while True:
    try:
        numero=int(input("Ingrese un número entre 10 y 15 =>"))
        if numero>=10 and numero<=15:
            break
        else:
            print("Ingrese un número dentro del rango.")
    except:
        print("Ingrese solo números enteros.")

x=0
y=1
for fibo in range(numero):
    z=x+y
    y=x
    x=z
    print(z)