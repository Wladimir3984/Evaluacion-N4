from funciones import *

class Avion:
    
    pasajeros = []
    asientos = generarMatrizAsientos()
    
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