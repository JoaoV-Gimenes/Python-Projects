import pandas as pd

dic = {
    'a' : ['dia', 22, 'PROGRAMAÇÂO'],
    'b' : ['mes', 22, 'PYHTON'],
    'c' : ['dia', 53 , 'OI']
}

# Cada chave vira uma coluna
df = pd.DataFrame(dic)
print(df)
#      a    b
# 0  dia  mes
# 1   22   22
# 2  PROGRAMAÇÃO  PYTHON

resultado = df.columns[df.isin(['dia']).any()]
print(resultado)