numero = int(input("Ingrese un numero: "))

suma = 0

for i in range(1, numero):

    if numero % i == 0:

        suma = suma + i

if suma == numero:

    print("El numero", numero, "es un numero perfecto")

else:
    print("El numero", numero, "no es un numero perfecto")