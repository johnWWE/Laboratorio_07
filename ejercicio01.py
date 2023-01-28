'''Escribir una función que determine si una cadena es un
palíndromo (se lee igual en ambos sentidos) o no:'''

def palindromo():
    cadena =input("Introduzca  una frase u oracion que quiere determinar: ")
    #convertamos la frase u oracion en minusculas, ya que en minusculas o mayusculas son iguales
    cadena=cadena.lower()
    #tambien debemos borrar los espaacios vacios que puedan estar sujetas a la oracion
    cadena=cadena.replace(" ", "")
    #evaluar si la cadena iantroducida es igual a su inversa
    if cadena == cadena[::-1]:
        return "La Cadena Introducida ES Palindromo..."
    else:
        return "la cadena Introducida NO es Palindromo... "
print(palindromo())
