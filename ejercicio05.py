''' Escribir una función que determine la longitud de la
subcadena más larga que contiene solo dígitos.'''
def subcadenaLargaConDigitos():
    cadena = input("Ingresa : ")  # Pide la cadena al usuario
    subcadenaLarga = ""  # variable para almacenar la subcadena más larga
    subcadena = ""  # variable para almacenar la subcadena actual
    # Recorremos cada carácter en la cadena
    for caracter in cadena:
        # Si el carácter es un dígito numérico, agrega al carácter a la subcadena actual
        if caracter.isnumeric():  #metodo para ver si las subcadenas tienen digito o no
            subcadena += caracter
        # Si el carácter no es un dígito numérico,
        else:
            # si la subcadena actual es más larga que la subcadena más larga, actualiza la subcadena más larga
            if len(subcadena) > len(subcadenaLarga):
                subcadenaLarga = subcadena
            # reinicia la subcadena actual
            subcadena = ""
    # Si la subcadena actual es más larga que la subcadena más larga, actualiza la subcadena más larga
    if len(subcadena) > len(subcadenaLarga):
        subcadenaLarga = subcadena
    # Devuelve la longitud de la subcadena más larga
    return len(subcadenaLarga)
print(subcadenaLargaConDigitos())