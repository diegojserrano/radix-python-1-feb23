
def apellido(persona):
    return persona["apellido"]

def apellido_nombre(persona):
    return persona["apellido"] + ", " + persona["nombre"]

def crear_persona(documento, nombre, apellido, edad):
    nueva_persona = dict()

    nueva_persona["documento"] = documento
    nueva_persona["nombre"] = nombre
    nueva_persona["apellido"] = apellido
    nueva_persona["edad"] = edad
    return nueva_persona

plantel = dict()

archivo = open("personas2.txt","rt")

for linea in archivo.readlines():
    valores = linea.split(";")
    doc = int(valores[0])
    nom = valores[1]
    ape = valores[2]
    edad = int(valores[3])
    persona1 = crear_persona(doc,nom,ape,edad)
    plantel[persona1["documento"]] = persona1

archivo.close()


# Calcular el promedio de edades de las personas
suma = 0
for persona in plantel.values():
    suma += persona["edad"]

#suma = sum([persona["edad"] for persona in plantel.values()])
promedio = suma / len(plantel)


print(f"Promedio de edades---: {promedio} ")

# Cuantas personas se llaman PEREZ
cantidad_perez = sum([1 for persona in plantel.values() if apellido(persona) == "PEREZ"])
print(f"Cantidad de PEREZ=: {cantidad_perez} ")


for x in sorted(plantel.values(), key = apellido_nombre):
    print(f"| {x['documento']:>8} | {x['nombre']:<20} | {apellido(x):<10} | {x['edad']:>2} |")