def generarListaAsientos():
    return [num for num in range(1,43)]

def mostrarAsientosDisponibles(listaAsientos):
    print(f" {listaAsientos[0]}   {listaAsientos[1]}   {listaAsientos[2]}", end= "      ")
    print(f"  {listaAsientos[3]}   {listaAsientos[4]}   {listaAsientos[5]}")
    print("")
    print(f" {listaAsientos[6]}   {listaAsientos[7]}   {listaAsientos[8]}", end= "      ")
    print(f"  {listaAsientos[9]}  {listaAsientos[10]}  {listaAsientos[11]}")
    print("")
    
    for primFila in range(12,38,6):
        print(f" {listaAsientos[primFila]}  {listaAsientos[primFila+1]}  {listaAsientos[primFila+2]}", end= "       ")
        print(f"{listaAsientos[primFila+3]}  {listaAsientos[primFila+4]}  {listaAsientos[primFila+5]}")
        print("")

#test
asientos = generarListaAsientos() 
asientos[15-1] = "X "      #Si la X no se inserta con un espacio se deforma todo
asientos[15] = "X "     
asientos[30] = "X "     
mostrarAsientosDisponibles(asientos)
