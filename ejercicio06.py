'''Escribir una función que reemplace todas las apariciones
de una subcadena en una cadena dada con otra subcadena
dada.'''

def reemplazoSubcadedenas(cadeenaa, subcadedena, nuevaSubcadena):
    return cadeenaa.replace(subcadedena, nuevaSubcadena)
cadena = "Un guerrero nunca cede su poder ante nada, ni siquiera ante la muerte"
print(reemplazoSubcadedenas(cadena, "guerrero", "Los guerreros"))
# si la subcadena que se desea reemplazar no se encuentra en la cadena original,
# la función devolverá la cadena original sin ningún cambio.