# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

def contra(palabra):
    contra = "contraseña"
    while palabra != contra:
        palabra = input("Contraseña incorrecta vuelve a intentarlo: ")
    return "Contraseña correcta."

palabra = input("Introduce la contraseña: ")

print(contra(palabra))