# Ingresar un conjunto de temperaturas, finalizar la carga
# cuando se reciba un 1000. Sólo aceptar temperaturas entre
# -20 y 50 grados.
# Informar:
#     * Cantidad de días con temperatura bajo cero
#     * Promedio de temperaturas
#     * Promedio de temperaturas de los días cálidos,
#     es decir con temp. mayor a 20
#     * Mostrar "Si" o "No" para indicar si hubo algún día
#     con más de 40 grados.
#     * La mayor temperatura de los días que no fueron cálidos

temp = float(input("Ingrese una temperatura"))
while (not -20 <= temp <= 50) and temp != 1000:
    print("Temperatura no válida")
    temp = float(input("Ingrese una temperatura"))

cantidad = cantidad_bajo_cero = cantidad_dias_calidos = 0
suma_todas = suma_dias_calidos = 0
hubo_40_grados = False
hubo_dias_frios = False
mayor = 0
while temp != 1000:
    suma_todas += temp
    cantidad += 1
    if temp > 20:
        suma_dias_calidos += temp
        cantidad_dias_calidos += 1
        if temp > 40:
            hubo_40_grados = True
    else:
        if temp < 0:
            cantidad_bajo_cero += 1
        if not hubo_dias_frios or temp > mayor:
            mayor = temp
        hubo_dias_frios = True
    temp = float(input("Ingrese una temperatura"))
    while (not -20 <= temp <= 50) and temp != 1000:
        print("Temperatura no válida")
        temp = float(input("Ingrese una temperatura"))

if cantidad > 0:
    print(f"Hubo {cantidad_bajo_cero} días con temperaturas bajo cero")
    promedio = suma_todas / cantidad
    print(f"El promedio de todas las temperaturas fue de {promedio:5.2f}")
    if cantidad_dias_calidos > 0:
        promedio_dias_calidos = suma_dias_calidos / cantidad_dias_calidos
        print(f"En los días cálidos la temperatura promedio fue de {promedio_dias_calidos}")
    else:
        print("No hubo ningún día cálido")
    print("Hubo días con más de 40 grados?")
    if hubo_40_grados:
        print("SI")
    else:
        print("NO")
    if hubo_dias_frios:
        print(f"En los días fríos la mayor temperatura fue de {mayor}")
    else:
        print("No hubo ningún día frío")
else:
    print("No ingresó ninguna temperatura válida")