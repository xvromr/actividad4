def terminos():

    numero = int(input("Ingrese la cantidad de terminos a generar: "))

    if numero < 0:

        print("El numero no es valido")

        return

    fib1 = 0

    fib2 = 1

    suma = 0

    for i in range(numero):

        suma = fib2 + suma

        print(fib2, end=" ")

        aux = fib2

        fib2 = fib2 + fib1

        fib1 = aux


    print("\nLa suma es:",suma)

def limite():
    
    numero = int(input("Ingrese el limite de la suma: "))

    if numero < 0:

        print("El numero no es valido")

        return

    fib1 = 0

    fib2 = 1

    suma = 0

    while suma < numero:

        suma = fib2 + suma

        print(fib2, end=" ")

        aux = fib2

        fib2 = fib2 + fib1

        fib1 = aux


    print("\nLa suma es:",suma)


opc = input("1. Terminos a generar \n2. Limite de generacion \n Ingrese una opcion: ")

if opc == "1":

    terminos()

elif opc == "2":

    limite()

else:

    print("La opcion no es valida")