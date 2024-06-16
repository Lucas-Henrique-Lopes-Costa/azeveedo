# leia um arqquivo csv e teste cada link que está na coluna Imagens e coluna Nome e se não tiver status 200, coloque na coluna encontrado como false, alem disso vai criando um arquivo falta.md que mostra o Nome e o link que não foi encontrado depois da um quebra de linha

import pandas as pd
import requests

df = pd.read_csv('teste.csv')
f = open("falta.md", "w")

for index, row in df.iterrows():
    if requests.get(row['Imagens']).status_code != 200:
        df.loc[index, 'encontrado'] = False
        f.write(row['Nome'] + " " + row['Imagens'] + "\n")
    if requests.get(row['Nome']).status_code != 200:
        df.loc[index, 'encontrado'] = False
        f.write(row['Nome'] + " " + row['Imagens'] + "\n")

df.to_csv('teste.csv', index=False)
f.close()
