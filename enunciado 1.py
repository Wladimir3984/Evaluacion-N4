#utilidad
from time import sleep
import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
class Pasajero:
    mensajePedidoDatos = "Ingreso datos pasajero: "
    
    def __init__(self):
        self.nombre = Pasajero.giveNombre().title()
        self.rut = Pasajero.giveRutCv()
        self.telefono = Pasajero.giveNum()
        self.banco = Pasajero.giveBanco()
        
    def toString(self): #Mejorar: que el rut salga con puntos, tendria que retirnar un str en giveRutCv()
        print(f"""
              
              nombre:   {self.nombre}
              rut:      {self.rut[0]}-{self.rut[1]}
              telefono: {self.telefono}
              banco:    {self.banco}
              """)
        
    @staticmethod
    def giveNombre(): #Error: no permite ingresar espacios(solo ingresa primer nombre)
        clear()
        print(Pasajero.mensajePedidoDatos)
        print("")
        
        nombre = input("Nombre -> ")
        if len(nombre) > 2 and nombre.isalpha():
            return nombre
        clear()
        print("¡Nombre invalido!")
        sleep(2)
        clear()
        return Pasajero.giveNombre()
    
    @staticmethod
    def giveRutCv(): #No estoy seguro de la validación, en el rango de numeros
        clear()
        print(Pasajero.mensajePedidoDatos)
        print("")
        
        rutCv = input("Rut(ej: 99999999-9) ->")
        if rutCv.count(".") == 0 and rutCv.count("-") == 1 and rutCv[-2] == "-":
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
    def giveBanco(): #Error: Tampoco permite espacios en el apartado "otros"
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
                banco = input("\nNombre banco -> ")
                if banco.isalpha():
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
""" asientos = generarListaAsientos() 

asientos[0][3] = "X"      
asientos[4][2] = "X"      
asientos[6][5] = "X"   
verAsientosDisponibles(asientos) """

""" pruebaRut = Pasajero.giveRutCv()
print(pruebaRut) """

pasajero = Pasajero()
pasajero.toString()

