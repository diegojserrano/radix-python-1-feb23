# Se necesita desarrollar un programa para el área de recursos humanos de
# una empresa que permita informar el jornal de un determinado operario.
# Usted deberá cargar por teclado el código de turno que el operario trabajó
# ese día (1- representa Diurno y 2- representa Nocturno) y la cantidad de horas
# trabajadas.
# La política de trabajo en la empresa es que los operarios de la misma
# pueden trabajar en el turno # diurno o nocturno. Si un operario trabaja
# en el turno nocturno el pago es 406 pesos la hora, si lo
# hace en el turno diurno cobra 355 pesos la hora.

turno = int(input("Ingrese el turno (1- Diurno, 2- Nocturno)"))
horas = int(input("Ingrese la cantidad de horas trabajadas"))

if turno == 1:
    sueldo_hora = 355
    nombre_turno = "Diurno"
else:
    sueldo_hora = 406
    nombre_turno = "Nocturno"

sueldo = horas * sueldo_hora


print(f"El sueldo por cada hora de turno {nombre_turno} es $ {sueldo_hora}")
print(f"El empleado debe cobrar $ {sueldo}")
