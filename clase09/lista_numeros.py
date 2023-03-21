
# Crea una lista vacía
lista = []


# Agrega datos
lista.append(343)
lista.append(567)
lista.append(12)


# Imprime la lista
print(lista)

# Recorrido
for x in lista:
    print(x)

# sumar todos los elementos de la lista
suma = 0
for x in lista: # Por cada x que pertenece a la lista
    suma += x


# Acceso indexado
print(lista[2]) # imprime el tercer casillero
print(lista[-1]) # imprime el último
print(lista[-2]) # imprime el anteúltimo

for i in range(len(lista)): # Recorre toda la lista con índices
    print(lista[i])

for i in range(3): # Recorre los tres primeros
    print(lista[i])

# Extraer los primeros 5 elementos
primeros_5 = lista[0:5] # Rebanada


