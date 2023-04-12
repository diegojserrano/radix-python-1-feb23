# Leer todo el archivo CP.txt y cargar sus datos en una lista de localidades.
# Cada localidad será un diccionario con claves: provincia, numero, nombre

# Luego de la carga:
# Mostrar todo el contenido de la lista
# Ingresada una provincia, mostrar todas las localidades de esa provincia ordenadas por numero



# Tomar la idea del programa clase14/personas.py



def crear_localidad(linea):
    datos = linea.split(";")

    localidad = dict()

    localidad["provincia"] = datos[0]
    localidad["numero"] = int(datos[1])
    localidad["nombre"] = datos[2][:-1]

    return localidad

def provincia(localidad): return localidad["provincia"]
def numero(localidad): return localidad["numero"]
def nombre(localidad): return localidad["nombre"]

def prov_nombre(localidad): return provincia(localidad) + nombre(localidad)
def cargar_localidades(nombre_archivo):
    archivo = open(nombre_archivo, "rt", encoding="ISO-8859-1")
    localidades = [crear_localidad(linea) for linea in archivo.readlines()]
    archivo.close()
    return localidades

def grabar_localidades(nombre_archivo, lista):
    archivo = open(nombre_archivo, "wt")

    for l in lista:
        archivo.write(f"{provincia(l)},{numero(l)},{nombre(l)}\n")

    archivo.close()


def listar_localidades(lista):
    for l in lista:
        print(f"| {provincia(l)} | {numero(l)} | {nombre(l):<60} |")

def contar_por_numero(lista):
    numeros = dict()

    for l in lista:
        n = numero(l)
        if n in numeros:
            numeros[n] += 1
        else:
            numeros[n] = 1

    return numeros


todas = cargar_localidades("CP.txt")
#listar_localidades(todas)

prov = input("Ingrese el código de la provincia (X, H, K): ")
encontradas = sorted([l for l in todas if provincia(l) == prov], key=numero)
listar_localidades(encontradas)
# Ingresar un texto y mostrar todas las localidades cuyo nombre incluya dicho texto, ordenadas por provincia y nombre
buscada = input("Ingrese un nombre para buscar: ")

# Alternativa secuencial
encontradas = []
for l in todas:
    if buscada in nombre(l):
        encontradas.append(l)
encontradas = sorted(encontradas, key=prov_nombre)

# Alternativa con comprensión
#encontradas = sorted([l for l in todas if buscada in nombre(l)], key=prov_nombre)

listar_localidades(encontradas)
nombre_archivo = buscada + ".csv"
grabar_localidades(nombre_archivo, encontradas)

# Por cada número mostrar la cantidad de repeticiones (pensar en un diccionario en el que la clave sea el numero)
cantidades = contar_por_numero(todas)
for n, c in cantidades.items():
    print(f"Código: {n}: {c} localidades")
