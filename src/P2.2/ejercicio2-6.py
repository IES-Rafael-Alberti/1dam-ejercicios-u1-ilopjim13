# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
#
# *
# **
# ***
# ****
# *****

def triangulo(num):
    cont = 1
    serie = ""
    while cont <= num:
        cont += 1
        serie = serie + "*"
        print(serie)

num = int(input("Introduce un numero: "))

triangulo(num)