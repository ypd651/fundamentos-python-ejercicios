def saludar():
    nombre = input("ingrese nombre ")
    saludo = input("ingrese un saludo")

    if saludo == "":
        saludo = "hola"

    print (saludo + " , " + nombre)
saludar() 