def contar_vocales():
    texto = input("ingrese su palabra: ")
    contador = 0

    for letra in texto:
        if letra in "aeiouAEIOU":
            contador += 1

    print ("cantidad de vocales:" , contador)
contar_vocales()