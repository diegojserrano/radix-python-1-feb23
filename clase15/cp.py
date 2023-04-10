# Leer todo el archivo CP.txt y cargar sus datos en una lista de localidades.
# Cada localidad será un diccionario con claves: provincia, numero, nombre

# Luego de la carga:
# Mostrar todo el contenido de la lista
# Ingresada una provincia, mostrar todas las localidades de esa provincia ordenadas por numero
# Ingresar un texto y mostrar todas las localidades cuyo nombre incluya dicho texto, ordenadas por provincia y nombre
# Por cada número mostrar la cantidad de repeticiones


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

def cargar_localidades(nombre_archivo):

    archivo = open(nombre_archivo, "rt", encoding="ISO-8859-1")
    #localidades = []

    #while True:
    #    linea = archivo.readline()
    #    if linea == "": break
    #    localidades.append(crear_localidad(linea))

    #return localidades

    localidades = [crear_localidad(linea) for linea in archivo.readlines()]
    archivo.close()
    return localidades

def listar_localidades(lista):
    for l in lista:
        print(f"| {provincia(l)} | {numero(l)} | {nombre(l):<60} |")


todas = cargar_localidades("CP.txt")
#listar_localidades(todas)

prov = input("Ingrese el código de la provincia (X, H, K): ")
encontradas = sorted([l for l in todas if provincia(l) == prov], key=numero)
listar_localidades(encontradas)
