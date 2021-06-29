from funciones import *

class Avion:
    
    pasajeros = []
    asientos = generarMatrizAsientos()
    
    @classmethod
    def modificarNombre(cls, indice):
        pass
    
    @classmethod
    def modificarTelefono(cls, indice):
        pass
    
    @classmethod
    def validarPasajero(cls):
        check1 = "✘"
        check2 = "✘"
        idx1 = 0
        idx2 = -1
        
        while True:
            clear()
            
            if check1 == "✔" and check2 == "✔" and idx1 == idx2:
                print(f"""Validar datos pasajero 
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
        while True: 
            try:
                print("Validación datos Pasajero")
                rutCv = input("Rut(ej: 99.999.999-9) ->")
                asiento = int(input("Asiento(1-42) -> "))
                
                if (rutCv.count(".") == 2 and rutCv.count("-") == 1 and rutCv[-2] == "-" and 11<=len(rutCv)<=12 and 1<=asiento<=42):
                    break 
                
                clear()
                print("¡Datos invalidos!")
                sleep(2)
                clear()
            except:
                clear()
                print("¡Solo numeros!")
                sleep(2)
                clear()
        
        for i in range(len(Avion.pasajeros)):
             if Avion.pasajeros[i].rut == rutCv and Avion.pasajeros[i].numAsiento == asiento:
                 print("""
                Dato a modificar:
                1. Nombre
                2. Telefono
                opción -> """,end = "")
             opcion = int(input())
             
             if opcion == 1: 
                 Avion.modificarNombre(i)
             elif opcion == 2:
                 Avion.modificarTelefono(i)
        
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
    def anularVuelo(cls,pasajero): 
        #elimina de la lista de pasajeros el pasajero, actualiza la matriz de asientos cambiando la x
        #a el numero de asiento que corresponde 
        #retorna True si se elimina correctamente y False si el pasajero no existe
        if pasajero in Avion.pasajeros:
            Avion.asientos = Avion.asientos.reshape(42)
            Avion.asientos[pasajero.numAsiento-1] = str(pasajero.numAsiento) #de "x" a numero
            Avion.asientos = Avion.asientos.reshape(7,6)
            
            cls.pasajeros.remove(pasajero) #elimina pasajero
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
    
    @classmethod
    def giveNumOfPassengers(cls):
        return len(cls.pasajeros)
    
    @classmethod
    def verPasajerosInscritos(cls): #IMPLEMENTAR POR LUCAS
        cls.pasajeros[0].toString()

class Pasajero:
    
    def __init__(self):
        self.nombre = giveNombre()
        self.rut = giveRutCv()
        self.telefono = giveNum()
        self.banco = giveBanco()
        self.numAsiento = 0
        
    def toString(self): 
        print(f"""
              
              Nombre:   {" ".join(self.nombre).title()}
              Run:      {self.rut[0]}-{self.rut[1]}
              Telefono: {self.telefono}
              Banco:    {" ".join(self.banco).title()}
              Asiento:  #{self.numAsiento}
              """)
     
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setTelefono(self, telefono): #validar telefono
        self.telefono = telefono
        
    def setNumAsiento(self, num):
        if str(num) in Avion.asientos:
            self.numAsiento = num 
            return True
        return False  