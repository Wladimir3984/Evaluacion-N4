#2

nombres=["Pablo", "Pedro", "Luis", "Ana", "Lisa", "Carmen", "Jorge", "Victor", "Jorge"]
nombres2=["Jorge", "Lisa", "Pedrinho", "Ana", "Juan", "Diego", "Victor", "Jorge"]
repetidos=[]

for x in range(len(nombres)):
    for y in range(len(nombres2)):
        if nombres[x]==nombres2[y] and nombres[x] not in repetidos:
            repetidos.append(nombres[x])            
print(repetidos)