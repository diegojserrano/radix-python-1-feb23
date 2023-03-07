# Ingresar una nota entre 1 y 10 inclusive.
# Validar que el dato esté en el intervalo correcto.


nota = int(input("Ingrese una nota: "))

while not 0 < nota <= 10: # Mientras no esté en el rango aceptable
    print("La nota no es válida")
    nota = int(input("Ingrese una nota: "))

print(f"Ud. ingresó {nota}")