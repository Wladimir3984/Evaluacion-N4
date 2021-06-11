#2

nombres=["Paula", "German", "Pedro", "Esteban", "Paula", "Ricardo", "Nicole", "Francisca", "Pedro", "Pedro", "Ricardo"]
apellidos=["Suarez", "Sanchez", "Ruiz", "Vega", "Suarez", "Gonzales", "Gonzalez", "Gonzalez"]
repetidos=[]
duplicado=0

for x in range(len(nombres)):
    duplicado=x+1
    for y in range(duplicado, len(nombres)):
        if nombres[x]==nombres[y] and nombres[x] not in repetidos:
            repetidos.append(nombres[x])
duplicado=0
for x in range(len(apellidos)):
    duplicado=x+1
    for y in range(duplicado, len(apellidos)):
        if apellidos[x]==apellidos[y] and apellidos[x] not in repetidos:
            repetidos.append(apellidos[x])

print(repetidos)