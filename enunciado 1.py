#utilidad
from time import sleep
import os
import numpy as np

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
def generarMatrizAsientos(): #LISTO, GENERADA MATRIZ DE STRINGS
    matrizAsientos = np.full((7,6), "10") #Curioso que si pongo en vez de "10" pongo "unNumeroMenorQue10" ya no funciona bien

    for i in range(1,38,6):
        inicioFila = [num for num in range(1,38,6)]
        
        for row in range(7):
            for col in range(6):
                matrizAsientos[row][col] = str(inicioFila[row]+col)
    
    return matrizAsientos

class Pasajero:
    cantidadPasajeros = 0
    mensajePedidoDatos = "Ingreso datos pasajero: "
    
    def __init__(self):
        self.nombre = Pasajero.giveNombre()
        self.rut = Pasajero.giveRutCv()
        self.telefono = Pasajero.giveNum()
        self.banco = Pasajero.giveBanco()
        self.numAsiento = 0
        Pasajero.addPasajero()
        
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
    
    def setTelefono(self, telefono):
        self.telefono = telefono
        
    def setNumAsiento(self, num):
        self.numAsiento = num
        
    @classmethod
    def addPasajero(cls):
        cls.cantidadPasajeros+=1
          
    @classmethod
    def getCantidadPasajeros(cls):
        return Pasajero.cantidadPasajeros
    
    @staticmethod
    def giveNombre(): 
        clear()
        print(Pasajero.mensajePedidoDatos)
        print("")
        
        nombre = input("Nombre -> ").split(" ")
        isValidName = True
        for parteNombre in nombre:
            if not (len(parteNombre) > 2 and parteNombre.isalpha):
                isValidName = False
        if isValidName: return nombre
        
        clear()
        print("¡Nombre invalido!")
        sleep(2)
        clear()
        return Pasajero.giveNombre()
    
    @staticmethod
    def giveRutCv(): 
        clear()
        print(Pasajero.mensajePedidoDatos)
        print("")
        
        rutCv = input("Rut(ej: 99.999.999-9) ->")
        if rutCv.count(".") == 2 and rutCv.count("-") == 1 and rutCv[-2] == "-" and 11<=len(rutCv)<=12:
            return rutCv.split("-") 
        clear()
        print("¡Rut invalido!")
        sleep(2)
        clear()
        return Pasajero.giveRutCv()
          
    @staticmethod
    def giveNum():
        clear()
        print(Pasajero.mensajePedidoDatos)
        print("")
        
        try:
            telefono = int(input("Telefono -> "))
        except:
            clear()
            print("¡Solo numeros!")
            sleep(2)
            clear()
            return Pasajero.giveNum()
        
        if 900000000<=telefono<=999999999:
            return telefono
        clear()
        print("¡Numero fuera de rango!")
        sleep(2)
        clear()
        return Pasajero.giveNum()
    
    @staticmethod
    def giveBanco(): 
        clear()
        print(Pasajero.mensajePedidoDatos)
        
        print(""" 
        Banco
        1.BancoDuoc
        2.Otro
        opcion -> """, end="")
        try:
            opcion = int(input(""))
        except:
            clear()
            print("¡Solo numeros!")
            sleep(2)
            clear()
            return Pasajero.giveBanco()
        if 1<=opcion<=2:
            if opcion == 1:
                return "BancoDuoc"
            
            while True:
                banco = input("\nNombre banco -> ").split(" ")
                isValidBanco = True
                
                for compBanco in banco:
                    if not compBanco.isalpha and len(compBanco) > 2:
                        isValidBanco = False
                
                if isValidBanco:
                    return banco
                
                clear()
                print("¡Solo letras!")
                sleep(2)
                clear()
                print(Pasajero.mensajePedidoDatos)
        
        clear()
        print("¡Opción invalida!")
        sleep(2)
        clear()
        return Pasajero.giveBanco()
    
class Avion:
    pasajeros = []
    asientos = generarMatrizAsientos()
    
    @classmethod
    def comprarVuelo(cls,pasajero): #falta: hacer el proceso de compra de vuelo según enunciado
        cls.pasajeros.append(pasajero)
        
        for fila in range(0,7):
            for asiento in range(0,6):
                if str(pasajero.numAsiento) == cls.asientos[fila][asiento]:
                    cls.asientos[fila][asiento] = "X"
                    
    @classmethod
    def anularVuelo(cls,pasajero): #implementar
        pass     
    
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
    def verPasajerosInscritos(cls):#implementar
        pass
  
#test

pasajero = Pasajero()
pasajero.setNumAsiento(23)
Avion.comprarVuelo(pasajero)
print("sadsadsa")
#Avion.verPasajerosInscritos() NO IMPLEMENTADO
Avion.verAsientosDisponibles()
print("commit desde rama r")
