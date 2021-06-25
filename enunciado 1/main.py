from clases import *
#HACER EL MENU EJECUTABLE AQUI, CUANDO YA ESTE FUNCIONANDO QUIZAS HACERLO COMO UNA FUNCION

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

#test 2 COMPRA DE DOS PASAJES SIN ANULAR

pasajero1 = Pasajero()
pasajero2 = Pasajero()

print(f"print 1 {pasajero1.setNumAsiento(1)}") #True 
print(f"print 2 {Avion.comprarVuelo(pasajero1)}")#True
print(f"print 3 {pasajero2.setNumAsiento(42)}")#True
print(f"print 4 {Avion.comprarVuelo(pasajero2)}")#True

Avion.verAsientosDisponibles()#1 y 42 comprado
print(Avion.giveNumOfPassengers())#2





