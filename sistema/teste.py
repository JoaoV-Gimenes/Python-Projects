dic = {
    'a' : ['dia', 22, 'PROGRAMAÇÂO'],
    'b' : ['mes', 22, 'PYHTON']
}
d = dic.values()

# Cada chave vira uma coluna
df = pd.DataFrame(dic)
print(df)
#      a    b
# 0  dia  mes
# 1   22   22
# 2  PROGRAMAÇÃO  PYTHON

# Ou cada chave vira uma linha
df = pd.DataFrame.from_dict(dic, orient='index')
print(df)
#      0   1            2
# a  dia  22  PROGRAMAÇÃO
# b  mes  22       PYTHON