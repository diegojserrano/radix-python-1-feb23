# Desde el ejercicio de la clase 9
#
# * Listar todos los elementos de casilleros con indices impares
# * Sumar los últimos 100 elementos de la lista
# * Mostrar los números que se encuentren entre un rango indicado
# por el usuario pero en forma invertida (es decir, en orden inverso al de la carga)
# *** Por cada item desarrollar una función que reciba al menos la lista
# y que retorne un resultado, sin mostrar nada.

def leer_archivo(nombre):
    archivo = open(nombre,"rt")

    lista = [int(linea) for linea in archivo.readlines()]

    archivo.close()
    return lista


def mostrar_lista(lista):
    print(len(lista)) # len = length
    for x in lista:
        print(x, end=", ")

def filtrar_indices_impares(lista):
    return lista[1::2]

def sumar_ultimos(lista,cantidad):
    return sum(lista[-cantidad:])

def filtrar_rango(lista, minimo, maximo):
    #seleccionados = []

    #for x in lista:
    #    if minimo <= x <= maximo:
    #        seleccionados.append(x)

    #return seleccionados[::-1]

    return [x for x in lista if minimo <= x <= maximo][::-1]

def calcular_promedio(lista):
    if not lista: return 0
    return sum(lista) / len(lista)

def contar_mayores_que(lista, piso):
    return len([0 for x in lista if x > piso])

def calcular_promedio_entre(lista, minimo, maximo):
    return calcular_promedio([x for x in lista if minimo <= x <= maximo])


numeros = leer_archivo("numeros.txt")
mostrar_lista(numeros)
indices_impares = filtrar_indices_impares(numeros)
print()
print(f"Se seleccionaron {len(indices_impares)} elementos")
mostrar_lista(indices_impares)
print()
print(f"La suma de los ultimos 100 es: {sumar_ultimos(numeros,100)}")
filtrados = filtrar_rango(numeros, 100, 200)
mostrar_lista(filtrados)
