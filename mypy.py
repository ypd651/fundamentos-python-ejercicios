def kelvin_a_celsius(k):
    return k - 273.15

def celsius_a_kelvin(c):
    return c + 273.15

def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

def kelvin_a_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def fahrenheit_a_kelvin(f):
    return (f - 32) * 5/9 + 273.15


def menu():
    print("\n🌡️ MENÚ DE CONVERSIÓN DE TEMPERATURA")
    print("1. Celsius → Kelvin")
    print("2. Kelvin → Celsius")
    print("3. Celsius → Fahrenheit")
    print("4. Fahrenheit → Celsius")
    print("5. Kelvin → Fahrenheit")
    print("6. Fahrenheit → Kelvin")
    print("7. Salir")


while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "7":
        print("Programa finalizado")
        break

    temperatura = float(input("Ingrese la temperatura: "))

    if opcion == "1":
        print("Resultado:", celsius_a_kelvin(temperatura), "K")

    elif opcion == "2":
        print("Resultado:", kelvin_a_celsius(temperatura), "°C")

    elif opcion == "3":
        print("Resultado:", celsius_a_fahrenheit(temperatura), "°F")

    elif opcion == "4":
        print("Resultado:", fahrenheit_a_celsius(temperatura), "°C")

    elif opcion == "5":
        print("Resultado:", kelvin_a_fahrenheit(temperatura), "°F")

    elif opcion == "6":
        print("Resultado:", fahrenheit_a_kelvin(temperatura), "K")

    else:
        print("❌ Opción inválida, intente de nuevo")