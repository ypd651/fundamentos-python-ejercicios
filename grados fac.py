def farhrenheit_a_celsius(farhenheit):
    return (farhenheit-32)*5/9

f = float(input("ingrese grados f: "))
c = farhrenheit_a_celsius(f)

print ("grados celsius:", c)