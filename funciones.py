from time import sleep
import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#FUNCIONES INPUTS PASAJERO ENUNCIADO 1
mensajePedidoDatos = "Ingreso datos pasajero: "

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
