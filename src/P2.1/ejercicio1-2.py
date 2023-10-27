def pasar(psw, contra):
    if psw >= contra:
        return "La contraseña es correcta."
    else:
        return "La contraseña es incorrecta"

psw = "contraseña"

contra = input("Introduce la contraseña: ")

print(pasar(psw, contra))