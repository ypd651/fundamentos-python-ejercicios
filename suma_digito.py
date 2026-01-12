def suma_digitos():
    numero = int(input("ingrese un numero"))
    suma = 0

    for d in numero:
        if d.isdigit():
            suma += int(d)

    return suma