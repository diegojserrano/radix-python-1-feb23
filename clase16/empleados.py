# Cargar los datos del archivo empleados.csv
# Calcular el total a pagar de sueldos
# Contar los empleados por tipo (tres totales)
# Buscar un empleado por legajo y mostrar el sueldo a pagar


def crear_empleado(tipo, legajo, nombre, apellido, basico, extra):
    nuevo = dict()

    nuevo["tipo"] = tipo
    nuevo["legajo"] = legajo
    nuevo["nombre"] = nombre
    nuevo["apellido"] = apellido
    nuevo["basico"] = basico
    if tipo == 1: nuevo["dias"] = int(extra)
    elif tipo == 2:
        nuevo["presentismo"] = (extra == "true")

    else: nuevo["ventas"] = int(extra)

    return nuevo


def leer_linea(linea):
    datos = linea.split(',')

    tipo = int(datos[0])
    legajo = int(datos[1])
    nombre = datos[2]
    apellido = datos[3]
    basico = int(datos[4])
    extra = datos[5][:-1]

    nuevo = crear_empleado(tipo, legajo, nombre, apellido, basico, extra)

    return nuevo

def leer_archivo(nombre_archivo):
    archivo = open(nombre_archivo, "rt")

    plantel = [leer_linea(linea) for linea in archivo.readlines()]

    archivo.close()

    return plantel

def sueldo_obrero(basico, dias):
    return basico / 20 * dias

def sueldo_administrativo(basico, presentismo):
    total = basico
    if presentismo: total *= 1.13 # incrementa 13% al total
    return total
    #return basico * (1.13 if presentismo else 1)

def sueldo_vendedor(basico, ventas):
    return basico + 0.01 * ventas

def sueldo(empleado):
    if empleado["tipo"] == 1: return sueldo_obrero(empleado["basico"], empleado["dias"])
    elif empleado["tipo"] == 2: return sueldo_administrativo(empleado["basico"], empleado["presentismo"])
    else: return sueldo_vendedor(empleado["basico"], empleado["ventas"])

plantel = leer_archivo("empleados.csv")

total_sueldos = sum([sueldo(e) for e in plantel])
print(len(plantel))

print(total_sueldos)

for e in plantel:
    print(f"{e['legajo']:>6} {e['nombre']:<20} {e['apellido']:<20}{sueldo(e):>10.2f}")
