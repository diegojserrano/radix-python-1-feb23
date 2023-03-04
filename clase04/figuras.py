# Ingresar primero el tamaño deseado para la figura

tamaño = int(input("Ingrese el tamaño de la figura"))

# Dibujar con un solo print la siguiente figura
# *
# **
# ***
# ****
# *****
# ******
print("Figura 1")
m="*"
for i in range(1,tamaño+1):
    print(m*i)


#######################################
# ******
# *****
# ****
# ***
# **
# *
#

print("Figura 2")
for i in range(tamaño,0,-1):
    print(m * i)
#######################################
#       *
#      **
#     ***
#    ****
#   *****
#  ******
#

print("Figura 3")
for i in range(1, tamaño+1):
    print(" " * (tamaño-i)  + m * i)
