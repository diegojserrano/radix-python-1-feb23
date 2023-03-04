# Ingresar una cantidad de días
# y luego la temperatura de cada uno de los días
# Calcular y mostrar:

#   * Cantidad de días con temperatura menor a 10
#   * Cantidad de días con temperatura mayor a 30
#   * Promedio de todas las temperaturas

dias = int(input("Ingrese la cantidad de días: "))
contador_menor_10 = contador_mayor_30 = 0
acumulador_temperaturas = 0

# Tantas vueltas como el valor de la variable días
for i in range(dias):
    temperatura = float(input("Ingrese la temperatura: "))
    if temperatura < 10:
        contador_menor_10 += 1
    elif temperatura > 30:
        contador_mayor_30 += 1
    acumulador_temperaturas += temperatura

promedio = acumulador_temperaturas / dias
print(f"Días con temp. menor a 10: {contador_menor_10}")
print(f"Días con temp. mayor a 30: {contador_mayor_30}")
print(f"Suma de temperaturas: {acumulador_temperaturas}")
print(f"Promedio de temperaturas: {promedio}")