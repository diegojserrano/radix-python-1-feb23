import random

numeros = set()
nombres = {"DIEGO", "EMMANUEL", "FERNANDO", "LEANDRO"}

print(numeros)
print(nombres)

numeros.update([2,3,5,7,98,6,3])


#for x in range(1000):
#    numeros.add(random.randint(1000,10000))



print("Lista de números: tamaño", len(numeros))
for n in numeros:
    print(n)

print("Lista de nombres")
for nom in nombres:
    print(nom)


nombres2 = {"RUBEN", "JUAN","LEANDRO","DIEGO"}
todos = nombres.union(nombres2)
repetidos = nombres.intersection(nombres2)
diferencia1 = nombres.difference(nombres2)
diferencia2 = nombres2.difference(nombres)
diferencia_simetrica = nombres.symmetric_difference(nombres2)
print(todos)
print(repetidos)
print(diferencia1)
print(diferencia2)
print(diferencia_simetrica)
