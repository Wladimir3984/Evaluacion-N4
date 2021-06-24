#utilidad
from time import sleep
import os
import numpy as np
from funciones import *

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
def generarMatrizAsientos(): #LISTO, GENERADA MATRIZ DE STRINGS
    matrizAsientos = np.full((42), "10") #Curioso que si pongo en vez de "10" pongo "unNumeroMenorQue10" ya no funciona bien
        
    for idx in range(0,42):
       matrizAsientos[idx] = str(idx+1)
       
    matrizAsientos = matrizAsientos.reshape(7,6) 
    
    return matrizAsientos

class Pasajero:
    cantidadPasajeros = 0
    
    def __init__(self):
        self.nombre = giveNombre()
        self.rut = giveRutCv()
        self.telefono = giveNum()
        self.banco = giveBanco()
        self.numAsiento = 0
        Pasajero.addPasajero()
    
    def __eq__(self, other):
        return self.numAsiento == other.numAsiento
        
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
        self.numAsiento = num 
        
    @classmethod
    def addPasajero(cls):
        cls.cantidadPasajeros+=1
          
    @classmethod
    def delPasajero(cls):
        cls.cantidadPasajeros-=1
        
    @classmethod
    def getCantidadPasajeros(cls):
        return Pasajero.cantidadPasajeros
    
class Avion:
    pasajeros = []
    asientos = generarMatrizAsientos()
    
    @classmethod
    def comprarVuelo(cls,pasajero): 
        #retorna True si el vuelo fue comprado y False si el pasaje ya estaba usado
        cls.pasajeros.append(pasajero)
        
        for fila in range(0,7):
            for asiento in range(0,6):
                if str(pasajero.numAsiento) == cls.asientos[fila][asiento]:
                    cls.asientos[fila][asiento] = "X"
                    return True
                
        return False
                    
    @classmethod
    def anularVuelo(cls,pasajero): 
        #elimina de la lista de pasajeros el pasajero, actualiza la matriz de asientos cambiando la x
        #a el numero de asiento que corresponde y disminuye en 1 Pasajero.cantidadPasajeros
        #retorna True si se elimina correctamente y False si el pasajero no existe
        if pasajero in Avion.pasajeros:
            Avion.asientos = Avion.asientos.reshape(42)
            Avion.asientos[pasajero.numAsiento-1] = str(pasajero.numAsiento) #de "x" a numero
            Avion.asientos = Avion.asientos.reshape(7,6)
            
            cls.pasajeros.remove(pasajero) #elimina pasajero
            Pasajero.delPasajero() #disminuye en 1 Pasajero.cantidadPasajeros
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
    def verPasajerosInscritos(cls): #IMPLEMENTAR POR LUCAS
        cls.pasajeros[0].toString()
  
#test
clear()
pasajero1 = Pasajero()
pasajero1.setNumAsiento(29)

pasajero2 = Pasajero()
pasajero2.setNumAsiento(29)

print(Avion.comprarVuelo(pasajero1))
print(Avion.comprarVuelo(pasajero2))

Avion.verAsientosDisponibles()


print(Avion.anularVuelo(pasajero2))
print("")
Avion.verAsientosDisponibles()

print(Pasajero.cantidadPasajeros)
print(len(Avion.pasajeros))

""" pasajero = Pasajero()
pasajero.setNumAsiento(23)
Avion.comprarVuelo(pasajero)
print("sadsadsa")
#Avion.verPasajerosInscritos() NO IMPLEMENTADO
Avion.verAsientosDisponibles()
print("commit desde rama r") """



""" pasajero2 = Pasajero()
pasajero1.toString()
pasajero2.toString()
pasajero1.setNumAsiento(19)
pasajero1.setTelefono(124324234)
pasajero1.setNombre("juan") """





