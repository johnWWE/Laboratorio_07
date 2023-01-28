'''Escribir una función que determine la longitud de la
subcadena más larga que no contiene ninguna letra
repetida.'''
def subcadenaLargaSinRepeticiones(cadena):
    divisar = ""   #vacia
    longitudMax = 0 #
    longitud = 0 #longitud actual inicializada en 0
    for char in cadena:
        if char not in divisar:
            divisar += char
            longitud += 1
        else:
            if longitud > longitudMax:
                longitudMax = longitud
            divisar = char
            longitud = 1
    if longitud > longitudMax:
        longitudMax = longitud
    return longitudMax

cadena = input("Introduce la cadena: ")
print("La longitud de la subcadena más larga sin letras repetidas es: ", subcadenaLargaSinRepeticiones(cadena))
