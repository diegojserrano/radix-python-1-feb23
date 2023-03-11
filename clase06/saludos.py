def saludar(nombre="Usuario"):
    print(f"Hola {nombre}!")
    print("Hoy es miercoles")


def despedir():
    print("Muchas gracias")
    print("Hasta luego")



usuario  = input("Ingrese su nombre")

saludar()
saludar(usuario)
print("linea 1")
print("linea 2")
saludar("Ana")
print("linea 3")
print("linea 4")
despedir()
