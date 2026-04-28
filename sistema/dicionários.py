import pandas as pd
from sistema.funções import *

df = pd.DataFrame(columns=['Nome', 'Departamento', 'Salário'])
while True:
  objetivo = opcoes.get(menu())
  if objetivo:
    objetivo(df)
  else:
    print('Opção inválida!')
