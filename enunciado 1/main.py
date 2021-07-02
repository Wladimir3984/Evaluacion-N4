from clases import *
#HACER EL MENU EJECUTABLE AQUI, CUANDO YA ESTE FUNCIONANDO HACERLO COMO UNA FUNCION PARA IMPORTARLO
#A UN PROGRAMA PRINCIPAL DONDE ESTEN TODOS LOS ENUNCIADOS

#test 1 TRATAR DE COMPRAR UN PASAJE COMPRADO: OK
""" pasajero1 = Pasajero()
pasajero2 = Pasajero()

print(f"print 1 {pasajero1.setNumAsiento(29)}") #True 29
print(f"print 2 {Avion.comprarVuelo(pasajero1)}")#True
print(f"print 3 {pasajero2.setNumAsiento(29)}")#False porque el 29 ya esta comprado
print(f"print 4 {Avion.comprarVuelo(pasajero2)}")#False porque no existe el pasaje numero "0"

Avion.verAsientosDisponibles()#29 comprado


print(f"print 5 {Avion.anularVuelo(pasajero1)}")#True
print("")
Avion.verAsientosDisponibles()#nada comprado

print(Avion.giveNumOfPassengers())#0 """

#test 2 COMPRA DE DOS PASAJES SIN ANULAR: OK

""" pasajero1 = Pasajero()
pasajero2 = Pasajero()

print(f"print 1 {pasajero1.setNumAsiento(1)}") #True 
print(f"print 2 {Avion.comprarVuelo(pasajero1)}")#True
print(f"print 3 {pasajero2.setNumAsiento(42)}")#True
print(f"print 4 {Avion.comprarVuelo(pasajero2)}")#True

Avion.verAsientosDisponibles()#1 y 42 comprado
print(Avion.giveNumOfPassengers())#2 """

#test 3 probar validarPasajero
""" clear()
pasajero1 = Pasajero()
pasajero2 = Pasajero()

pasajero1.setNumAsiento(42)
pasajero2.setNumAsiento(32)

Avion.comprarVuelo(pasajero1)
Avion.comprarVuelo(pasajero2)

print(Avion.validarPasajero())# """


opcion=0
while opcion!=5:
    opcion=0 
    print("="*100)
    print("1. Ver asientos disponibles\n2. Comprar asiento\n3. Anular vuelo\n4. Modificar datos de pasajero\n5. Salir")
    print("="*100)
    while opcion<1 or opcion>5:
        try:
            opcion=int(input("=>"))
            if opcion<1 or opcion>5:
                print("Ingrese una opción válida.")
        except:
            print("Ingrese solo números.")

    if opcion==1: #Ver asientos
        Avion.verAsientosDisponibles()

    elif opcion==2: 
        if Avion.disponibilidadAsientos():
            pasajero = Pasajero()
            if Avion.comprarVuelo(pasajero):
                print("Asiento reservado éxitosamente.")
            else:
                print("Ese asiento no se encuentra disponible.")
        else:
            print("No existen asientos disponibles.")    
    
    elif opcion==3:
        rut=input("Ingrese su rut: ")
        if rut.count(".") == 2 and rut.count("-") == 1 and rut[-2] == "-" and 11<=len(rut)<=12:
           # print(f"{rut} {pasajero.rut[0]}")
            if rut=="-".join(pasajero.rut):
                Avion.anularVuelo(pasajero)
                print("Reserva eliminada éxitosamente.")
            else:
                print("Ese rut no se encuentra registrado.")
        else:
            print("Rut inválido.")
            
    elif opcion==4:
        Avion.modificarPasajero()