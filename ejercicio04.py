'''Escribir una función que determine la frecuencia de cada
carácter en una cadena dada y devuelva un diccionario.'''
def FrecuenciaCaracter():
    cadena =input("Introduzca la cadena que quiera que sea determinada la frecuencia de sus caracteres: ")
    frecuencia ={}   # en el almacenaremos  las frecuencias de cada letra
    #buscamos si el caracter se encuentra en la cadena, recorriendola
    for caracter in cadena:
        if caracter in frecuencia:
            frecuencia[caracter]+=1   # si la letra ya se encuentra en el diccionario, solo le incrementamos en 1
        else:
            frecuencia[caracter]=1  # si aun no estaba, simplemente es 1
    return frecuencia
print(FrecuenciaCaracter())

#usando el metodo count()
print("Usando el metodo count ")
def contarFrecuencia():
    caadena1     = input("Ingresa  la cadena que desee: ")
    # Crea un diccionario vacío para almacenar las frecuencias
    frecuencia1 = {}
    # Recorre cada carácter en la cadena
    for char in caadena1:
        # Utiliza el método count() para contar la frecuencia del carácter
        frecuencia1[char] = caadena1.count(char)
    # Devuelve el diccionario con las frecuencias
    return frecuencia1
print(contarFrecuencia())
