# Ingresar 3 números.
# Indicar el valor del mayor (si se repiten, mostrar cualquiera)

n1 = int(input("Ingrese un número"))
n2 = int(input("Ingrese un número"))
n3 = int(input("Ingrese un número"))


#if n1 > n2:
#    if n1 > n3:
#        mayor = n1
#    else:
#        mayor = n3
#else:
#    if n2 > n3:
#        mayor = n2
#    else:
#        mayor = n3


#if n1 > n2 and n1 > n3:
#    mayor = n1
#else:
#    if n2 > n3:
#        mayor = n2
#    else:
#        mayor = n3


if n1 > n2:
    mayor = n1
else:
    mayor = n2

if n3 > mayor:
    mayor = n3

print(f"El mayor es {mayor}")