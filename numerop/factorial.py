def factorial():
    n = int(input("ingrese un numero "))
    resultado = 1

    for i in range(1, n + 1):
        resultado *= 1

    print ("el resultado es:" , resultado)
factorial()