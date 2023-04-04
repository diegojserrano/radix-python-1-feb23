import random

plantel = dict()

archivo = open("personas2.txt", "rt")

while True:
    linea = archivo.readline()
    if linea == "": break
    valores = linea.split(";")
    doc = int(valores[0])
    nombre = valores[1] + " " + valores[2]
    plantel[doc] = nombre

archivo.close()

#print("Búsqueda de personas por documento")
#doc = int(input("Ingrese un documento: "))
#while doc != 0:
#    if doc in plantel:
#        print(plantel[doc])
#    else:
#        print("No existe")
#    doc = int(input("Ingrese un documento: "))


#print("Búsqueda de personas por nombre")
#nom = input("Ingrese un nombre: ")
#while nom != "":
#    encontrados = {doc:nombre for doc, nombre in plantel.items() if nom in nombre}
#    print(encontrados)
#    nom = input("Ingrese un nombre: ")


perez = {doc:nombre for doc, nombre in plantel.items() if "PE" in nombre}
carl = {doc:nombre for doc, nombre in plantel.items() if "CA" in nombre}
pe_ca = dict(perez.items() & carl.items())
print(perez)
print(carl)
print(pe_ca)


# cargar el archivo de inscriptos en un conjunto de numeros
# generar un nuevo diccionario con los documentos y nombres de los inscriptos

archivo_inscriptos = open("inscriptos.txt","rt")

inscriptos = {int(linea) for linea in archivo_inscriptos.readlines()}

archivo_inscriptos.close()

documentos_inscriptos =  plantel.keys() & inscriptos
print("Documentos", len(documentos_inscriptos),documentos_inscriptos)

personas_inscriptas = {doc: plantel[doc] for doc in documentos_inscriptos}
print("Inscriptos", personas_inscriptas )

#### Alternativa sin comprensiones ni operaciones de conjuntos
archivo_inscriptos = open("inscriptos.txt","rt")
personas_inscriptas = dict()

while True:
    linea = archivo_inscriptos.readline()
    if linea == "": break
    doc = int(linea)
    if doc in plantel:
        personas_inscriptas[doc] = plantel[doc]

archivo_inscriptos.close()
print("Inscriptos", personas_inscriptas )
