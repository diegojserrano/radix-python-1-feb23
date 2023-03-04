# Ingresar un número por teclado y mostrar su tabla de multiplicar


m = int(input("Ingrese un número: "))

print(f"Tabla de multiplicar del {m}")

for i in range(0, 11):
    resultado = m * i
    print(f"{m:>3} x {i:>3} = {resultado:>4}")