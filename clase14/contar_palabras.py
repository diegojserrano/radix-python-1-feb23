import re
# Ingresar oraciones por teclado. Contar cada palabra, es decir, por cada palabra del texto informar cuántas veces apareció.

# Diccionario en el que la clave sea una palabra y el valor un contador
# Una sola vez
glosario = dict()

oracion = input("Ingrese el texto: ")

while oracion != "FIN":
    for palabra in re.sub("[^a-z áéíóúñ]","",oracion.lower()).split():
       if palabra in glosario:
            glosario[palabra] += 1
       else:
            glosario[palabra] = 1
    oracion = input("Ingrese el texto: ")

repetidas = {x:y for x,y in glosario.items() if y > 1}

print("Repetidas: ", len(repetidas))
print(repetidas)