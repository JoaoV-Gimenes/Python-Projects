import pandas as pd

def menu():
  return input('O que deseja realizar?\n' + '<I> Inserir novo usuário\n' + '<E> Excluir usuário\n' + 
                 '<L> Listar usuários\n' + '<P> Pesquisar usuário\n').upper()

def inserir(banco):
  nome = input('Digite o nome do usuário: ').upper()
  if nome in banco['Nome'].values:
    return 'Usuário já existe!'

  banco.loc[len(banco)] = {
      'nome' : nome, 
      'departamento' : input('Departamento: '), 
      'salário' : int(input('Salário: '))
   }
  print('Usuário adicionado com sucesso!')
  return banco

def excluir(banco):
    usuario = input('Digite qual usuário deseja remover: ').upper()

    if usuario in banco['Nome'].values:
        banco = banco[banco['Nome'] != usuario]
        print(f'{usuario} removido!')
        return banco
    else:
        print(f'usuario {usuario} não encontrado!')
        return banco

def pesquisaU(banco):
  usuario = input('Digite qual usuário deseja pesquisar: ')
  return banco[usuario]

def pesquisaGeral(banco):
  valor = input('valor para busca: ')
  df_busca = banco.columns[banco.isin([valor]).any()]
  return banco[df_busca]

def pesquisar():
  print('')

def listar(banco):
    print(banco)

opcoes = {
    'I' : inserir,
    'E' : excluir,
    'L' : listar,
    'P' : pesquisar
}