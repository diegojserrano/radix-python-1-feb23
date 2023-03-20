# Leer el archivo de números
# Calcular y mostrar
#   * Suma de todos
#   * Cantidad de impares
#   * Promedio de pares

archivo = open("numeros.txt", "rt")

suma = suma_pares = 0
cantidad_pares = cantidad_impares = 0

while True:
    linea = archivo.readline()
    if not linea: break
    numero = int(linea)
    suma += numero
    if numero % 2 == 0:
        cantidad_pares += 1
        suma_pares += numero
    else:
        cantidad_impares += 1

print(f"Suma de todos: {suma}")
print(f"Cantidad de impares: {cantidad_impares} ")

if cantidad_pares > 0:
    promedio = suma_pares / cantidad_pares
    print(f"El promedio de los pares es {promedio:6.2f}")
else:
    print("No se encontraron números pares")

archivo.close()
