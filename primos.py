rango_i = int(input("Ingrese el inicio del rango: "))

rango_f = int(input("Ingrese el final del rango: "))

if rango_f < rango_i or rango_f < 0  or rango_i < 0:

    print("El rango no es valido")

    exit(0)

primos = ""

for i in range(rango_i, rango_f + 1):
    
    
    primo = True
    for j in range(2, i):
        
        if i % j == 0:
        
            primo = False
            
            break
        
    if primo:
            
        primos = primos + ", " + str(i)

primos = primos.replace(",", "", 1)

print("Los numeros primos entre", rango_i, "y", rango_f, "es", primos)

