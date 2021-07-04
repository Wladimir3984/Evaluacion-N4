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
            precioPasaje = 78900
            pasajero = Pasajero()
            
            if 31<=pasajero.numAsiento<=42: # VIP
                precioPasaje = 240000
            
            if pasajero.banco == "BancoDuoc": #15% descuento por ser del banco duoc
                precioPasaje -= precioPasaje*0.15 
            
            while True:
                clear()
                print(f"Precio pasaje: ${precioPasaje}")
                aceptaCompra = input("¿Acepta la compra del pasaje?(si/no) -> ").upper()
                
                if aceptaCompra == "SI":
                    if Avion.comprarVuelo(pasajero):
                      clear()
                      print("Asiento reservado éxitosamente.")
                      sleep(2)
                      break
                  
                    else:
                        clear()
                        print("Ese asiento no se encuentra disponible.")
                        sleep(2)
                        break
                elif aceptaCompra == "NO":
                    break
                
                else: 
                    clear()
                    print("respuesta invalida")
                    sleep(2)
                    continue
            
        else:
            clear()
            print("No existen asientos disponibles.")  
            sleep(2)  
            
    
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