import random

boleta = {3,7,12,29,31,4}
sorteadas = set()

#Alternativa 1
#bolillas = [i for i in range(1,37)]
#random.shuffle(bolillas)
#sorteadas = set(bolillas[:10])

#Alternativa 2
sorteadas = set(random.sample(range(1,37),10))

aciertos = boleta.intersection(sorteadas)

print(boleta)
print(sorteadas)
print(aciertos)
print(f"Cantidad de aciertos: {len(aciertos)}")
