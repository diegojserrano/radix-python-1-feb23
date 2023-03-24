def leer_archivo(nombre):
    archivo = open(nombre, "rt")

    personas = [linea[:-1] for linea in archivo.readlines()]

    archivo.close()

    return personas

def mostrar_lista(lista):
    for x in lista:
        print(x)

def edad(per):
    return int(per.split(";")[3])

def nombre(per):
    return per.split(";")[1]

def documento(per):
    return int(per.split(";")[0])

def promedio_edades(lista):

    edades = [edad(per) for per in lista]
    return sum(edades) / len(edades)

def filtrar_por_nombre(lista, nom):

    return [per for per in lista if nombre(per) == nom]

def cantidad_documento_en_rango(lista, minimo, maximo):
    return len([0 for per in lista if minimo <= documento(per) <= maximo])


personas = leer_archivo("personas2.txt")
#mostrar_lista(personas)
print(f"Promedio de edades: {promedio_edades(personas)}")
nombre_buscado = input("A quién quiere buscar")
encontradas = filtrar_por_nombre(personas, nombre_buscado)
mostrar_lista(encontradas)
print(f"Hay {len(encontradas)} personas que se llaman {nombre_buscado}")
print(f"Hay {cantidad_documento_en_rango(personas, 22537486,22537486)} personas en el rango solicitado")
