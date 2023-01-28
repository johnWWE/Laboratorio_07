'''Escribir una función que divida una cadena dada en una
lista de subcadenas cada vez que aparezca un carácter
específico.'''
def dividirCadenas():
    cadenas=input("Introduce cadenas separadas por comas [,]")
#separar en subcaadenas
    subcadenas=cadenas.split(", ") #Hacemos que se separe en subcadenas cada vezz que aparece el caracter coma (,)
    return subcadenas
print(dividirCadenas())
