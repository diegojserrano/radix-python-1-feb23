def mayor_2(n1, n2):
    mayor = n1 if n1 > n2 else n2
    return mayor

def mayor_3(n1, n2, n3):
    return mayor_2(mayor_2(n1, n2), n3)


def es_positivo(n):
    return n >= 0


def es_par(n):
    return n % 2 == 0


def esta_entre(n, a, b):
    if a > b:
        a, b = b, a
    return a < n < b
