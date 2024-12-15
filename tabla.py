numero = int(input("Ingrese un numero: "))

rango_i = int(input("Ingrese el inicio del rango: "))

rango_f = int(input("Ingrese el final del rango: "))

if rango_f < rango_i or rango_f < 0  or rango_i < 0 or numero < 0:

    print("El rango no es valido")

    exit(0)

for i in range(rango_i, rango_f + 1):

    print(numero, "x", i, "=", numero*i)

