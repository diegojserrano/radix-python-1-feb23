def dibujar_triangulo(tamaño):
    m = "* "
    for i in range(1, tamaño + 1):
        print(m * i)

tam = int(input("Ingrese un tamaño (fin con 0) : "))
while tam != 0:
    print()
    dibujar_triangulo(tam)
    tam = int(input("Ingrese un tamaño (fin con 0) : "))
