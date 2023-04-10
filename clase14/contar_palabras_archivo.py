import re
# Ingresar oraciones por teclado. Contar cada palabra, es decir, por cada palabra del texto informar cuántas veces apareció.

# Diccionario en el que la clave sea una palabra y el valor un contador
# Una sola vez
glosario = dict()

archivo1 = open("Quijote.txt", "rt")

for linea in archivo1.readlines():
    for palabra in re.sub("[^a-z áéíóúñ]","",linea.lower()).split():
       if palabra in glosario:
            glosario[palabra] += 1
       else:
            glosario[palabra] = 1

repetidas = {x:y for x,y in glosario.items() if y > 100}
ordenadas_cantidad = sorted(repetidas.items(), key=lambda x:x[1])
ordenadas_alfabeticamente = sorted(repetidas.keys())

print("Repetidas ordenadas por cantidad: ", len(repetidas))
for x,y in ordenadas_cantidad:
    print(f"{x:<20}: {y:>5}")

print("Repetidas ordenadas alfabeticamente: ", len(repetidas))
for x in ordenadas_alfabeticamente:
    print(f"{x:<20}: {repetidas[x]:>5}")

mayor = 0
pal_mayor = ""
for pal,cant in repetidas.items():
    if cant > mayor:
        mayor = cant
        pal_mayor = pal

print(f"Palabra más repetida: {pal_mayor:<20}: {mayor:>5}")
