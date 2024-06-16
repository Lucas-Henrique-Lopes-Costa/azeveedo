# leia um arqquivo csv e teste cada link que está na coluna Imagens e se não tiver status 200, coloque na coluna encontrado como false

import pandas as pd 
import requests

df = pd.read_csv('arquivo.csv')

def testar_link(link):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            print('Link encontrado ' + link)
            return True
        else:
            print('Link não encontrado ' + link)
            # coloca no falta.md
            with open('falta.md', 'a') as f:
                f.write(
                    f'Link não encontrado: {link}\n\n'
                )
            return False
    except:
        return False
    
df['encontrado'] = df['Imagens'].apply(testar_link)

df.to_csv('arquivo.csv', index=False)

print('Arquivo salvo com sucesso')
