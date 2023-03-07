# Ingresar números positivos como negativos
# hasta que llegue un 0.
# Informar el valor del mayor y menor respectivamente

#Doble carga
cargo_un_numero = False
n = int(input("Ingrese un número. Fin con 0:")) # Este es el primero
mayor = menor = n

while n != 0:
    cargo_un_numero = True
    if n > mayor:
        mayor = n
    elif n < menor:
        menor = n
    n = int(input("Ingrese un número"))

if cargo_un_numero: # Si cargó un número
    print(f"El mayor de todos es {mayor}")
    print(f"El menor de todos es {menor}")
else:
    print("No ingresó ningún número")
print("Hasta luego")