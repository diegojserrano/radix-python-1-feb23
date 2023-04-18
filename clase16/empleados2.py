import pandas as pd
import matplotlib.pyplot as plt

plantel = pd.read_csv("empleados.csv")
obreros= plantel.query('tipo == 1')
print(obreros.to_string())
print(obreros["extra"].mean())
#plantel["tipo"].plot(kind="hist")
#plt.show()
#print(plantel["basico"].sum())