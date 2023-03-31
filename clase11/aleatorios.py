import random

# Número float al azar entre 0 y 1, sin incluir al 1.
random.random()

# Número entero en un rango, sin incluir el extremo mayor
random.randrange(1,100)

# Número entero en un rango, incluyendo ambos extremos
random.randint(1,100)


def tirar_bola():
    return random.randint(0,36)