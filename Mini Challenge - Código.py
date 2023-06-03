import pandas as pd
import random

df = pd.read_excel("C:/Users/User/Downloads/Mini challenge - Semana 1.xlsx").sample(frac=1).reset_index(drop=True)  # Lê o arquivo .xlsx e embaralha suas linhas

n = len(df["Nome"])

restritos = []
bixos = []
for i in range(n):  # Separa os nomes restritos e os bixos em listas separadas
    if df["Restrição"][i] == 1:
        restritos.append(df["Nome"][i])
    else:
        bixos.append(df["Nome"][i])

grupo1 = [restritos[0]]  # Pegamos 1 restrito para cada lista, e uma fatia dos dos bixos
grupo1.extend(bixos[:4])

grupo2 = [restritos[1]]
grupo2.extend(bixos[4:8])

grupo3 = [restritos[2]]
grupo3.extend(bixos[8:12])
          
grupo4 = [restritos[3]]
grupo4.extend(bixos[12:])

print(grupo1, grupo2, grupo3, grupo4, sep="\n")
