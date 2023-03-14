#import comparaciones: obliga a llamar a las funciones como comparaciones.funcion
from comparaciones import *
from random import *

cantidad = int(input("Ingrese la cantidad de jugadas"))
cantidad_0 = cantidad_pares = cantidad_impares = 0
cantidad_todos = cantidad_menores = 0
cantidad_docena_1 = cantidad_docena_2 = cantidad_docena_3 = 0

for i in range(cantidad):
    n = randint(0,36)
    if n == 0:
        cantidad_0 += 1
    else:
        if es_par(n):
            cantidad_pares += 1
        else:
            cantidad_impares += 1

        if esta_entre(n,0,13):
            cantidad_docena_1 += 1
        elif esta_entre(n,11,25):
            cantidad_docena_2 += 1
        else:
            cantidad_docena_3 += 1

        if esta_entre(n,0,19):
            cantidad_menores += 1
        cantidad_todos += 1

porcentaje_menores = cantidad_menores / cantidad_todos

print(f"Cantidad de veces que salio 0: {cantidad_0}")
print(f"Cantidad de pares: {cantidad_pares}")
print(f"Cantidad de impares: {cantidad_impares}")
print(f"Cantidad en primera docena: {cantidad_docena_1}")
print(f"Cantidad en segunda docena: {cantidad_docena_2}")
print(f"Cantidad en tercera docena: {cantidad_docena_3}")
print(f"Porcentaje de menores: {porcentaje_menores:.2%}")