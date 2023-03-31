import random
def es_menor(n): # true si n esta entre 1 y 18 inclusive
    return 1 <= n <= 18

def tirar_bola():
    return random.randint(0,36)
def es_par(n):
    return n % 2 == 0
def docena(n):
    return ((n-1) // 12) + 1
def calle(n): # dado un número n, informe el menor numero de la calle que lo contiene
    return n - ((n-1) % 3)


cantidad = random.randint(2000,4000)
jugadas = [tirar_bola() for i in range(cantidad)]

cantidad_0 = len([0 for nro in jugadas if nro == 0])

cantidad_pares = len([0 for nro in jugadas if nro != 0 and es_par(nro)])
cantidad_impares = len([0 for nro in jugadas if not es_par(nro)])

cantidad_docena1 = len([0 for nro in jugadas if docena(nro) == 1])
cantidad_docena2 = len([0 for nro in jugadas if docena(nro) == 2])
cantidad_docena3 = len([0 for nro in jugadas if docena(nro) == 3])

cantidad_menores = len([0 for nro in jugadas if es_menor(nro)])

porcentaje = cantidad_menores / cantidad # guardo tanto por 1

docenas = [docena(nro) for nro in jugadas if nro != 0]


print(f"Se jugaron {cantidad} jugadas")
print(f"Salieron {cantidad_0} ceros")
print(f"Salieron {cantidad_pares} pares")
print(f"Salieron {cantidad_impares} impares")
print(f"Cantidad por docena: 1={cantidad_docena1},  2={cantidad_docena2}, 3={cantidad_docena3}")
print(f"Porcentaje de menores: {porcentaje:.2%}")

apostado = int(input("Ingrese un número"))
inicio_calle = calle(apostado)
fin_calle = inicio_calle + 2
numeros_calle = [nro for nro in jugadas if inicio_calle <= nro <= fin_calle]

print(f"Números de la calle del {apostado}: {numeros_calle}")