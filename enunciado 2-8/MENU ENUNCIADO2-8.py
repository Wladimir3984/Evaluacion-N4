import os
from enunciado2 import *
from enunciado3 import *
from enunciado4 import *
from enunciado5 import *
from enunciado6 import *
from enunciado7 import *
from enunciado8 import *

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

opcion=0
while opcion!=8:
    
    opcion=0 
    
    while opcion<1 or opcion>8:
        try:
            clearConsole()
            print("="*100)
            print("1. Enunciado 2\n2. Enunciado 3\n3. Enunciado 4\n4. Enunciado 5\n5. Enunciado 6\n6. Enunciado 7\n7. Enunciado 8\n8. Salir")
            print("="*100)
            
            opcion=int(input("=>"))
            if opcion<1 or opcion>8:
                clearConsole()
                print("Ingrese una opción válida.")
                sleep(2)
                clearConsole()
        except:
            clearConsole()
            print("Ingrese solo números enteros.")
            sleep(2)
            clearConsole()

    if opcion==1: #ENUNCIADO 2
        clearConsole()
        enunciado2()

    elif opcion==2: #ENUNCIADO 3
        clearConsole()
        enunciado3()

    elif opcion==3: #ENUNCIADO 4
        clearConsole()
        enunciado4()

    elif opcion==4: #ENUNCIADO 5
        clearConsole()
        enunciado5()
    
    elif opcion==5: #ENUNCIADO 6
        enunciado6()

    elif opcion==6: #ENUNCIADO 7
        clearConsole()
        enunciado7()
    
    elif opcion==7: #ENUNCIADO 8
        clearConsole()
        enunciado8()