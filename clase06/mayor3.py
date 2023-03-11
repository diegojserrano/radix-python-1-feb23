def mayor_2(a,b):
    if a > b:
        mayor = a
    else:
        mayor = b
    return mayor



n1 = int(input("Ingrese un valor"))
n2 = int(input("Ingrese un valor"))
n3 = int(input("Ingrese un valor"))

mayor = mayor_2(n1, n2)
mayor = mayor_2(mayor, n3)

print(mayor)