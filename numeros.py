quantidade = int(input('Quantos números você deseja digitar?: '))
numeros = []

for i in range(quantidade):
    n = int(input(f'número {i+1}: '))
    numeros.append(n)


while True:

    cont = input('deseja adicionar outro número? (s/n): ').lower()
    if cont != 's':
        break
    else:
        j = int(input('Digite um número: '))
        numeros.append(j)


ordem = input('Como você quer ordená-los? (crescente/decrescente): ').lower()
mensagem = {
    'crescente' : sorted(numeros),
    'decrescente': sorted(numeros, reverse=True)
}

print(mensagem.get(ordem, 'ordem inválida'))

par = []
impar= []
for a in numeros:
    if a % 2 == 0:
        par.append(a)
    else:
        impar.append(a)

print(f'Em sua lista você possui {len(par)} números pares e {len(impar)} números ímpares')