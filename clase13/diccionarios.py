dias_mes = { "ene": 31, "feb": 28, "mar": 31 }
nombres1 = ["abr", "jun","sep","nov"]
nombres2 = ["may", "jul","ago","oct","dic"]

for mes in nombres1:
    dias_mes[mes] = 30
for mes in nombres2:
    dias_mes[mes] = 31

print(dias_mes)
print("Keys")
for x in dias_mes.keys(): print(x)
print("Values")
for x in dias_mes.values(): print(x)
print("Pares")
for x, y in dias_mes.items(): print(f"{x} - {y}")

print("Meses de 31 días")
for nombre, dias in dias_mes.items():
    if dias == 31:
        print(f"{nombre} - {dias}")

mes = input("¿Que mes quiere ver?")
while mes != "":
    print (dias_mes[mes] if mes in dias_mes else "No existe")
    mes = input("¿Que mes quiere ver?")
