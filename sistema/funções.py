
def menu():
    return input('O que deseja realizar?\n' + '<I> Inserir novo usuário\n' + '<E> Excluir usuário\n' + '<L> Listar usuário\n' + '<P> Pesquisar usuário\n').upper()

opcoes = {
    'I' : 'inserir',
    'E' : 'excluir',
    'L' : 'listar',
    'P' : 'pesquisar'
}

def inserir(banco):
    banco[input('Digite o apelido do usuário: ').tittle()] = [input('Digite o nome do usuário: ').tittle(), input('Digite a última estação acessada: '), input('Digite a ultima data de acesso (dd/mm/yy): ')]
    return banco

def excluir(banco, usuario):
    banco.remove(usuario)
    return f'{usuario} removido!'

def pesquisaU(banco, usuario):
    return banco[usuario]

def pesquisaN(banco, usuario, nome):
    return banco[usuario][nome]

def pesquisaE(banco, usuario, estacao):
    return banco[usuario][estacao]

def pesquisaD(banco, usuario, data):
    return banco[usuario][data]

    