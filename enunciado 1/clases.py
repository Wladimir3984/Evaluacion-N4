from funciones import *

class Avion:
    
    pasajeros = []
    asientos = generarMatrizAsientos()
    
    @classmethod
    def disponibilidadAsientos(cls):
        disponibles=False
        for x in range(7):
            for j in range(6):
                if cls.asientos[x][j] != "X":
                    disponibles=True
        return disponibles
     
    @classmethod
    def modificarNombre(cls, indice, nombre):
        cls.pasajeros[indice].nombre = nombre
    
    @classmethod
    def modificarTelefono(cls, indice, telefono):
        cls.pasajeros[indice].telefono = telefono
    
    @classmethod
    def validarPasajero(cls):
        #retorna indice del pasajero validado para modificarlo
        #False si se cancela la operación   
        clear()
        check1 = "✘"
        check2 = "✘"
        idx1 = 0
        idx2 = -1
        
        while True:
            clear()
            
            if check1 == "✔" and check2 == "✔" and idx1 == idx2:
                print(f"""
              Validar datos pasajero 
              
              Run ({check1}) Asiento ({check2}) 
              1. Modificar pasajero
              2. Cancelar modificación 
              opc -> """, end="")

                try:
                    opc = int(input(""))
                except:
                    clear()
                    print("¡Solo numeros!")
                    sleep(2)
                    continue
                if 1<=opc<=2:
                    if opc == 1: return idx1
                    else: return False
                
                clear()
                print("¡Opción invalida!")
                sleep(2)
                continue
            
            elif check1 == "✔" and check2 == "✔" and idx1 != idx2:
                check1 = "✘"
                check2 = "✘"
                idx1 = 0
                idx2 = -1
                
            else:
                auxDatoOk = False
                print(f"""Validar datos pasajero 
                1. Run     ({check1})  
                2. Asiento ({check2})
                3. Cancelar validación
                opc -> """, end="")

                try:
                    opc = int(input(""))
                except:
                    clear()
                    print("¡Solo numeros!")
                    sleep(2)
                    clear()
                    continue
                
                if 1<=opc<=3:
                    if opc == 1:
                        rutCv = input("Rut(ej: 99.999.999-9) -> ")
                        
                        if rutCv.count(".") == 2 and rutCv.count("-") == 1 and rutCv[-2] == "-" and 11<=len(rutCv)<=12:
                            for i in range(len(Avion.pasajeros)):
                                if "-".join(Avion.pasajeros[i].rut) == rutCv:
                                    auxDatoOk = True
                                    idx1 = i
                                    break
                            
                            if auxDatoOk: check1 = "✔"
                            else: check1 = "✘"
                            
                    elif opc == 2:
                        try:
                            asiento = int(input("Asiento -> "))
                        except:
                            check2 = "✘"
                            clear()
                            print("¡Solo numeros!")
                            sleep(2)
                            clear()
                        
                        for i in range(len(Avion.pasajeros)):
                            if Avion.pasajeros[i].numAsiento == asiento:
                                auxDatoOk = True
                                idx2 = i
                                break
                        
                        if auxDatoOk: check2 = "✔"
                        else: check2 = "✘"
                        
                    else: return False
                
                else: 
                    clear()
                    print("¡Opción invalida!")
                    sleep(2)
                
    @classmethod
    def modificarPasajero(cls):
        clear()
        if len(cls.pasajeros) > 0:    
            indicePasajero = cls.validarPasajero()
            clear()
            while True:  
                print(f""" 
                    Modificar {"-".join(cls.pasajeros[indicePasajero].rut)}
                    1.Modificar nombre   ( {" ".join(cls.pasajeros[indicePasajero].nombre)} ) 
                    2.Modificar telefono ( {cls.pasajeros[indicePasajero].telefono} )
                    3.Salir
                    opc -> """, end="")
                try:
                    opc = int(input(""))
                except:
                    clear()
                    print("¡Solo numeros!")
                    sleep(2)
                    clear()
                    continue
                
                if 1<=opc<=3:
                    if opc == 1:
                        clear()
                        print(f"""Nombre actual: {" ".join(cls.pasajeros[indicePasajero].nombre)}""")
                        print("")
                        nuevoNombre = input("Nuevo nombre -> ").split(" ")
                        isValidName = True
                        for parteNombre in nuevoNombre:
                            if not (len(parteNombre) > 2 and parteNombre.isalpha):
                                isValidName = False
                        if isValidName: 
                            cls.modificarNombre(indicePasajero,nuevoNombre )
                            clear()
                            print("El nombre se a modificado correctamente")
                            sleep(2)
                            clear()
                            continue
                        clear()
                        print("¡Nombre invalido!")
                        sleep(2)
                        clear()
                        
                    elif opc == 2:
                        clear()
                        print(f"Telefono actual: {cls.pasajeros[indicePasajero].telefono}  ")
                        print("")
                        try:
                            nuevoTelefono = int(input("Nuevo telefono -> "))
                        except:
                            clear()
                            print("¡Solo numeros!")
                            sleep(2)
                            clear()
                            continue
                        
                        if 900000000<=nuevoTelefono<=999999999:
                            cls.modificarTelefono(indicePasajero,nuevoTelefono)
                            clear()
                            print("El telefono se a modificado correctamente")
                            sleep(2)
                            clear()
                            continue
                            
                        
                        clear()
                        print("¡Telefono invalido(fuera de rango)!")
                        sleep(2)
                        clear()
                        
                    
                    else: return 
                else:
                    clear()
                    print("¡Opción invalida!")
                    sleep(2)
                    clear()
        else:
            clear()
            print("No hay vuelos reservados")
            sleep(2)
            clear()
           
    @classmethod
    def comprarVuelo(cls,pasajero): 
        #retorna True si el vuelo fue comprado y False si el pasaje ya estaba usado
        
        for fila in range(0,7):
            for asiento in range(0,6):
                if str(pasajero.numAsiento) == cls.asientos[fila][asiento]:
                    cls.asientos[fila][asiento] = "X"
                    cls.pasajeros.append(pasajero)
                    return True
                
        return False
                    
    @classmethod
    def anularVuelo(cls, asiento): 
        #elimina de la lista de pasajeros el pasajero, actualiza la matriz de asientos cambiando la x
        #a el numero de asiento que corresponde 
        #retorna True si se elimina correctamente y False de lo contrario
        idxPasajero = -1
        for i in range(len(cls.pasajeros)):
            if cls.pasajeros[i].numAsiento == asiento:
                idxPasajero = i
                break
                
                 
        if idxPasajero > -1:
            Avion.asientos = Avion.asientos.reshape(42)
            Avion.asientos[cls.pasajeros[idxPasajero].numAsiento - 1] = str(cls.pasajeros[i].numAsiento) #de "x" a numero
            Avion.asientos = Avion.asientos.reshape(7,6)
            
            cls.pasajeros.remove(cls.pasajeros[idxPasajero]) #elimina pasajero
            return True
        
        return False
        
    @classmethod
    def verAsientosDisponibles(cls): #decorar
        print(cls.asientos[0])
        print(cls.asientos[1])
        print(cls.asientos[2])
        print(cls.asientos[3])
        print(cls.asientos[4])
        print(cls.asientos[5])
        print(cls.asientos[6])
        print("")
        input("presione ENTER para salir")
    
    @classmethod
    def giveNumOfPassengers(cls):
        return len(cls.pasajeros)
    
    @classmethod
    def verPasajerosInscritos(cls):
        if not len(cls.pasajeros) == 0:
            for pasajero in cls.pasajeros:
                pasajero.toString()
            return True
        
        else: return False
class Pasajero:
    
    def __init__(self):
        self.nombre = giveNombre()
        self.rut = giveRutCv()
        self.telefono = giveNum()
        self.banco = giveBanco()
        self.numAsiento = giveAsiento(Avion.asientos)
        
    def toString(self): 
        """ Telefono: {self.telefono}
        Banco:    {" ".join(self.banco).title()} """
        
        print(f"| Pasaje: #{self.numAsiento}| Nombre: {self.nombre[0].title()} | Run: {self.rut[0]}-{self.rut[1]}")
        print("")
     
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setTelefono(self, telefono): #validar telefono
        self.telefono = telefono
        
