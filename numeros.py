#pergunta quantos númmeros o usuário quer digitar
quantidade = int(input('Quantos números você deseja digitar?: '))
#Lista para os númmeros digitados
numeros = []

for i in range(quantidade):
    n = int(input(f'número {i+1}: '))
    numeros.append(n)

#loop que pergunta ao usuário se quer adicionar outro número 
while True:

    cont = input('deseja adicionar outro número? (s/n): ').lower()
    if cont == 'n':
        #quebra o loop caso não queira adicionar 
        break
    elif cont == 's':
        #solicita o número caso deseja adicionar outro
        j = int(input('Digite um número: '))
        numeros.append(j)
    else:
        print('Digite apenas "S" ou "N"')

#pergunta a ordem em que o usuário quer ordenar os númmeros
ordem = input('Como você quer ordená-los? (crescente/decrescente): ').lower()
#cria um loop até que o usuário digite uma ordem válida
while ordem not in ['crescente', 'decrescente']:
    print('ordem inválida')
    ordem = input('Como você quer ordená-los? (crescente/decrescente): ').lower()

mensagem = {
    #ordena em ordem crescente
    'crescente' : (', '.join(map(str, sorted(numeros)))),
    #ordena em ordem decrescente
    'decrescente': (', '.join(map(str, sorted(numeros, reverse=True))))
}
#printa os números em ordem
print(f'numeros ordenados:', mensagem.get(ordem))

#Listas para armazenar numeros pares e ímpares 
par = []
impar= []
#for para analisar cada númmero digitado
for a in numeros:
    if a % 2 == 0:
        #adiciona um número na lista par caso for múltiplo de 2
        par.append(a)
    else:
        #adiciona um número na lista ímpar caso não for múltiplo de 2
        impar.append(a)
#printa a quantidade de números pares e ímpares
print(f'Em sua lista você possui {len(par)} número(s) pare(s) e {len(impar)} número(s) ímpare(s)')