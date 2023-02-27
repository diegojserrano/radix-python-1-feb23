# Un comercio necesita informar el importe final a pagar a un
# determinado proveedor. Para ello debe ingresar la categoría
# (que puede ser categoría ’A’ o ’B’) y el importe original a abonar.
# Considerar las siguientes condiciones para el cálculo del importe final a pagar:
# Si el cliente es categoría A y el monto a pagar supera a
# los 1000 pesos debe aplicarse un descuento del 5%.
# Si el cliente es categoría B y el importe a pagar oscila
# entre 1500 y 2500 pesos debe aplicarse un descuento del 2%.
# Para ambas categorías en caso de no cumplirse las condiciones
# especificadas no se aplicará ningún tipo de descuento sobre
# el importe que se le debe abonar.

categoria = input("Ingrese la categoría A o B: ")
importe = float(input("Ingrese el importe original: "))


if categoria == "A" and importe > 1000:
    total = importe * 0.95
elif categoria == "B" and 1500 <= importe <= 2500: # las comparaciones encadenadas siempre son con and
    total = importe * 0.98
else:
    total = importe

print(f"Del importe original de {importe} debe abonar {total}")