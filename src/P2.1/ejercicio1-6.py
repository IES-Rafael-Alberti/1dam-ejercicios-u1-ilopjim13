def curso(nombre, sexo):
    #Si es mujer y tiene un nombre anterior a la M o si es hombre y tiene un nombre posterior a la N estarán en el grupo A sino estarán en el grupo B
    if nombre < "M" or nombre < "m" and sexo == "mujer":
        return "Estas en el grupo A."
    elif nombre > "N" or nombre > "n" and sexo == "hombre":
        return "Estas en el grupo A."
    else:
        return "Estas en el grupo B."

nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo: ")

print(curso(nombre, sexo))