# Del archivo quijote.txt imprimir todas las palabras que no existan en el diccionario del idioma ingles.
# Bajar el libro de https://github.com/diegojserrano/radix-python-1-feb23/blob/main/clase08/Quijote.txt
# Bajar el diccionario de https://github.com/dwyl/english-words/blob/master/words_alpha.txt
import re
import time

def palabas_unicas(nombre_archivo):
    archivo1 = open(nombre_archivo,"rt")

    todas = set()

    for linea in archivo1.readlines():
        todas.update(re.sub("[^a-z ]","",linea.lower()).split())


    #while True:
    #    linea = archivo1.readline().lower()
    #    if not linea: break
    #    palabras = re.sub("[^a-zA-Z ]","",linea).split()
    #    todas.update(palabras)

    return todas


inicio = time.time()
todas_quijote = palabas_unicas("Quijote.txt")
diccionario = palabas_unicas("words_alpha.txt")
inexistentes = todas_quijote.difference(diccionario)
fin = time.time()

duracion  = fin - inicio
print(len(todas_quijote))
print(len(diccionario))
print(len(inexistentes))
print(sorted(inexistentes))
print(duracion)

