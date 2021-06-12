while True:
    palabra=input("Ingrese una palabra=> ").lower()
    palabra2 = "" #sumador de letras al revés
    contador=0 #contador de letras
    if palabra.replace(" ", "").isalpha(): #omitir espacios y validar que sean solo letras
        for i in palabra.replace(" ", ""): #recorrer palabra omitiendo espacios
            contador+=1 #contar letras
            palabra2= i + palabra2 #añadir letra en reversa
        
        if palabra.replace(" ", "") == palabra2: #comparar palabras sin espacios
            print(f"{palabra} es un palíndromo. Tiene {contador} letras") #resultado => palabra normal y la suma de únicamente sus letras
            break
        else:
            print(f"{palabra} no es un palíndromo. Tiene {contador} letras")
            break
    else:
        print("Ingrese solo letras.")