
tipo = 0
importe = 0
suma_importe_1 = suma_importe_2 = suma_importe_3 = 0
cantidad_1 = cantidad_2 = cantidad_3 = 0
mayor = tipo_mayor = codigo_mayor = 0
cargó_datos = False

codigo = int(input("Ingrese el código: "))
while codigo != 0:
    cargó_datos = True
    tipo = int(input("Ingrese el tipo (1,2,3): "))
    importe = float(input("Ingrese el importe: "))

    if importe > mayor:
        mayor = importe
        tipo_mayor = tipo
        codigo_mayor = codigo


    if tipo == 1:
        suma_importe_1 += importe
        cantidad_1 += 1
    elif tipo == 2:
        suma_importe_2 += importe
        cantidad_2 += 1
    else:
        suma_importe_3 += importe
        cantidad_3 += 1
    codigo = int(input("Ingrese el código: "))

if cargó_datos:
    print("Datos del mayor")
    print(f"Codigo: {codigo_mayor}")
    print(f"Tipo {tipo_mayor}")
    print(f"Importe: {mayor}")

    print("Cantidad y suma de importes por tipo")
    print("| Tipo | Cantidad | Suma importes |")
    print(f"|   1  | {cantidad_1:>8} | {suma_importe_1:>13.2f} |")
    print(f"|   2  | {cantidad_2:>8} | {suma_importe_2:>13.2f} |")
    print(f"|   3  | {cantidad_3:>8} | {suma_importe_3:>13.2f} |")
else:
    print("No cargó ningún artículo")