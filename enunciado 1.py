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
    mensajePedidoDatos = "Ingreso datos pasajero: "
    
    def __init__(self):
        self.nombre = giveNombre()
        self.rut = giveRutCv()
        self.telefono = giveNum()
        self.banco = giveBanco()
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
    
    def setTelefono(self, telefono): #validar telefono
        self.telefono = telefono
        
    def setNumAsiento(self, num):#crear magic method de igualdad para este atributo
        self.numAsiento = num #para validar que no este comprado un asiento para comprarlos
        
    @classmethod
    def addPasajero(cls):
        cls.cantidadPasajeros+=1
          
    @classmethod
    def getCantidadPasajeros(cls):
        return Pasajero.cantidadPasajeros
    
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
    def verPasajerosInscritos(cls): #IMPLEMENTAR POR LUCAS
        cls.pasajeros[0].toString()
  
#test
pasajero1 = Pasajero()
pasajero1.setNumAsiento(29)
Avion.comprarVuelo(pasajero1)
Avion.verAsientosDisponibles()
Avion.verPasajerosInscritos()

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





