#utilidad
from time import sleep
import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
class Pasajero:
    def __init__(self):
        nombre = Pasajero.giveNombre()
        rut = Pasajero.giveRut()
        telefono = Pasajero.giveNum()
        banco = Pasajero.giveBanco()
        
    @staticmethod
    def giveNombre(): 
        nombre = input("Nombre -> ")
        if len(nombre) > 2 and nombre.isalpha():
            return nombre
        print("¡Nombre invalido!")
        sleep(2)
        clear()
        return Pasajero.giveNombre()
    @staticmethod
    def giveRut():
        pass         
    @staticmethod
    def giveNum():
        pass  
    @staticmethod
    def giveBanco():
        pass  

def generarListaAsientos(): #listo
    return [[num for num in range(1,7)],
            [num for num in range(7,13)],
            [num for num in range(13,19)],
            [num for num in range(19,25)],
            [num for num in range(25,31)],
            
            [num for num in range(31,37)],
            [num for num in range(37,43)]]

def verAsientosDisponibles(listaAsientos): #Hay que decorarlo
    print(listaAsientos[0])
    print(listaAsientos[1])
    print(listaAsientos[2])
    print(listaAsientos[3])
    print(listaAsientos[4])
    print(listaAsientos[5])
    print(listaAsientos[6])

#test
asientos = generarListaAsientos() 

asientos[0][3] = "X"      
asientos[4][2] = "X"      
asientos[6][5] = "X"   
verAsientosDisponibles(asientos)

