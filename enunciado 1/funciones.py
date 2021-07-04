from time import sleep
import os
import numpy as np

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#FUNCIONES ENUNCIADO 1
mensajePedidoDatos = "Ingreso datos pasajero: "


def validNumAsiento(num, arrayAsientos):
    #retorna True si el asiento esta disponible
    if str(num) in arrayAsientos:
        return True
    return False 
  
def giveAsiento(arrayAsientos):
    clear()
    print(mensajePedidoDatos)
    print("")
    
    try:
        asiento = int(input("Asiento -> "))
    except:
        clear()
        print("¡Solo numeros!")
        sleep(2)
        clear()
        return giveAsiento(arrayAsientos)
    
    if 1<=asiento<=42:
        if validNumAsiento(asiento,arrayAsientos):
            return asiento
        
        clear()
        print("Asiento no disponible")
        sleep(2)
        clear()
        return giveAsiento(arrayAsientos)
        
    clear()
    print("¡Numero fuera de rango!")
    sleep(2)
    clear()
    return giveAsiento(arrayAsientos)
      
def giveNombre(): 
    clear()
    print(mensajePedidoDatos)
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
    return giveNombre()

def giveRutCv(): 
    clear()
    print(mensajePedidoDatos)
    print("")
    
    rutCv = input("Rut(ej: 99.999.999-9) ->")
    if rutCv.count(".") == 2 and rutCv.count("-") == 1 and rutCv[-2] == "-" and 11<=len(rutCv)<=12:
        return rutCv.split("-") 
    clear()
    print("¡Rut invalido!")
    sleep(2)
    clear()
    return giveRutCv()
        
def giveNum():
    clear()
    print(mensajePedidoDatos)
    print("")
    
    try:
        telefono = int(input("Telefono -> "))
    except:
        clear()
        print("¡Solo numeros!")
        sleep(2)
        clear()
        return giveNum()
    
    if 900000000<=telefono<=999999999:
        return telefono
    clear()
    print("¡Numero fuera de rango!")
    sleep(2)
    clear()
    return giveNum()

def giveBanco(): 
    clear()
    print(mensajePedidoDatos)
    
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
        return giveBanco()
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
            print(mensajePedidoDatos)
    
    clear()
    print("¡Opción invalida!")
    sleep(2)
    clear()
    return giveBanco()

def generarMatrizAsientos(): #LISTO, GENERADA MATRIZ DE STRINGS
        matrizAsientos = np.full((42), "10") #Curioso que si pongo en vez de "10" pongo "unNumeroMenorQue10" ya no funciona bien
            
        for idx in range(0,42):
            matrizAsientos[idx] = str(idx+1)
        
        matrizAsientos = matrizAsientos.reshape(7,6) 
        
        return matrizAsientos
