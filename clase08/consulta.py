def mostrar_archivo(nombre):
    archivo = open(nombre,"rt")
    while True:
        linea = archivo.readlines()
        if not linea: break
        print(linea, end="")
#for linea in archivo.readlines():
    #    print(linea,end="")
    archivo.close()

# Abrir el archivo indicado por el nombre
# Recorrerlo linea a linea
# Mostrar aquellas lineas que contengan el texto buscado

def buscar_mostrar(nombre, buscado):
    archivo = open(nombre,"rt")
    numero_linea = 0
    while True:
        linea = archivo.readline()
        if not linea: break
        numero_linea += 1
        if buscado in linea.upper():
            print(f"Linea {numero_linea}: {linea}", end="")
    archivo.close

def buscar_personas(nombre, apellido):
    archivo = open(nombre, "rt")
    numero_linea = 0
    while True:
        linea = archivo.readline()
        if not linea: break
        numero_linea += 1
        datos = linea.split(";")
        documento = int(datos[0])
        nombre = datos[1]
        apellido = datos[2]
        edad = int(datos[3])
        if buscado == apellido.upper():
            print(f"{apellido} {nombre}")

nombre = input("Ingrese el nombre del archivo: ")
#mostrar_archivo(nombre)
buscado = input("Ingrese el texto a buscar: ").upper()
#buscar_mostrar(nombre, buscado)
buscar_personas(nombre, buscado)