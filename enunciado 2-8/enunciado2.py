def enunciado2():
    nombres=["Pablo", "Pedro", "Luis", "Ana", "Lisa", "Carmen", "Jorge", "Victor", "Jorge"]
    nombres2=["Jorge", "Lisa", "Pedrinho", "Ana", "Juan", "Diego", "Victor", "Jorge"]
    repetidos=[]
    print(f"Las listas son:\n1. {nombres}\n2. {nombres2}")
    print("")
    for x in range(len(nombres)):
        for y in range(len(nombres2)):
            if nombres[x]==nombres2[y] and nombres[x] not in repetidos:
                repetidos.append(nombres[x])            
    print(f"Los nombres repetidos son: {repetidos}")
    print("")
    input("Presione ENTER para continuar...")