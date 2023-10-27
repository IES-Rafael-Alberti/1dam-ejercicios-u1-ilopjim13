
def mayoredad(edad):
    #Si la edad es mayor o igual a 18 retornará que es mayor de edad y si no es asi retornará que es menor de edad
    if edad >= 18:
        return "Eres mayor de edad."
    else:
        return "Eres menor de edad."
    
edad = int(input("Introduce tu edad: "))

print(mayoredad(edad))


