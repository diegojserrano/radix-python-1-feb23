numero1 = float(input("Ingrese un número: "))
numero2 = float(input("Ingrese otro número: "))

suma = numero1 + numero2
diferencia = numero1 - numero2
producto = numero1 * numero2

print(f"Suma: {suma}")
print(f"Diferencia: {diferencia}")
print(f"Producto: {producto}")

if numero2 != 0:
    cociente = numero1 / numero2
    print(f"Cociente: {cociente:8.3f}")
else:
    print("No puedo dividir por cero")
