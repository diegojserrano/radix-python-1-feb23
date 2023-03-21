# Leer el archivo de numeros en una lista
# Calcular e imprimir:
#     * Cantidad de números mayores que el promedio

def leer_archivo(nombre):
    archivo = open(nombre,"rt")
    lista = []

    while True:
        linea = archivo.readline()
        if linea == "": break # se terminó el archivo entonces corto el ciclo
        lista.append(int(linea))

    archivo.close()
    return lista


def mostrar_lista(lista):
    print(len(lista)) # len = length
    for x in lista:
        print(x, end=", ")

def calcular_promedio(lista):
    suma = 0
    for x in lista:
        suma += x

    promedio = suma / len(lista)
    return promedio

def contar_mayores_que(lista, piso):
    cant_mayores = 0
    for x in lista:
        if x > piso:
            cant_mayores = cant_mayores + 1
    return cant_mayores



def calcular_promedio_entre(lista, minimo, maximo):
    suma = 0
    cantidad = 0

    for x in lista:
        if minimo <= x <= maximo: # condición de filtro
            suma += x
            cantidad += 1

    promedio = 0
    if cantidad > 0:
        promedio = suma / cantidad

    return promedio

# El menor número impar del lote

def menor(lista):
    menor = None # la variable menor está vacía

    for x in lista:
        if menor is None or x < menor:
            menor = x

    return menor


def es_par(n):
    return n % 2 == 0


def es_impar(n):
    return n % 2 != 0


def menor_impar(lista):
    menor = None # la variable menor está vacía

    for x in lista:
        if es_impar(x): # Si es impar
            if menor is None or x < menor:
                menor = x

    return menor


def listar_invertido(lista):
    for i in range(len(lista)-1, -1, -1):
        print(lista[i])


lista = leer_archivo("numeros.txt")
mostrar_lista(lista)
promedio = calcular_promedio(lista)
cant_mayores_prom = contar_mayores_que(lista, promedio)
promedio_2 = calcular_promedio_entre(lista, 200, 400)
menor_impares = menor_impar(lista)
menor_todos = menor(lista)
print()
print(f"El promedio es {promedio}")
print(f"Hay {cant_mayores_prom} mayores que el promedio")
print(f"El promedio de los números entre 200 y 400 es {promedio_2}")
print(f"El menor de todos es: {menor_todos}")
print(f"El menor de los impares es: {menor_impares}")