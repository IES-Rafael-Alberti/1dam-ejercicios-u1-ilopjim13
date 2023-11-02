# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

def deletrear(palabra):
    cont = palabra.len()
    letra = palabra[-1]
    while cont > 0:
        cont = cont - 1
        print(letra)

palabra = input("Introduce una palabra")

def main():
    deletrear(palabra)

if __name__ == "__main__":
    main()
