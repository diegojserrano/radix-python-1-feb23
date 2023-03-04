# Ingresar un texto, mostrar todas las minúsculas del mismo
# Si el usuario ingresa "Juan"
# El programa debe mostrar:
# u
# a
# n

texto = input("Ingrese un texto: ")
for letra in texto:
    if "a" <= letra <= "z": # es minúscula
        print(letra)