def imprimir_tabla_multiplicar(n):
    print("-" * 20)
    print("|" + f"Tabla del {n}".center(18) + "|")
    print("-" * 20)
    for i in range(11):
        print(f"| {n:>3} x {i:>2} = {n*i:>5} |")
    print("-" * 20)

