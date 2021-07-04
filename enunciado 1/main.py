from clases import *
from funciones import clear #<-----USAR FUNCION clear() PARA LIMPIAR CONSOLA
#HACER EL MENU EJECUTABLE AQUI, CUANDO YA ESTE FUNCIONANDO HACERLO COMO UNA FUNCION PARA IMPORTARLO
#A UN PROGRAMA PRINCIPAL DONDE ESTEN TODOS LOS ENUNCIADOS

opcion=0
while opcion!=5:
    clear()
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
        clear()
        Avion.verAsientosDisponibles()

    elif opcion==2: 
        clear()
        if Avion.disponibilidadAsientos():
            pasajero = Pasajero()
            if Avion.comprarVuelo(pasajero):
                print("Asiento reservado éxitosamente.")
            else:
                print("Ese asiento no se encuentra disponible.")
        else:
            print("No existen asientos disponibles.")    
    
    elif opcion==3:
        clear()
        while True:
            print("Lista de pasajes comprados")
            print("")
            if Avion.verPasajerosInscritos():
                try:
                    asiento = int(input("Num pasaje a eliminar -> "))
                except:
                    clear()
                    print("¡Solo numeros!")
                    sleep(2)
                    clear()
                    continue
                
                if Avion.anularVuelo(asiento):
                    clear()
                    print("Vuelo eliminado correctamente")
                    sleep(2)
                    clear()
                    break
                elif 1<=asiento<=42: 
                    clear()
                    print("Numero de vuelo no reservado")
                    sleep(2)
                    clear()
                    break
                else: 
                    clear()
                    print("¡No existen pasajes con ese numero!")
                    sleep(2)
                    clear()
                    break
            else: 
                clear()
                print("No hay vuelos reservados")
                sleep(2)
                clear()
                break
                
                    
               
    elif opcion==4:
        clear()
        Avion.modificarPasajero()