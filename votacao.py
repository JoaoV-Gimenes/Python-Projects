candidatos = {i: 0 for i in range(1,5)} #faz o dicionário referente à quantidade de votos para cada candidato (iniciados em 0)

#solicita 10 votos
for _ in range (1, 11):
    voto = int(input('Em qual candidato você deseja votar? (1, 2, 3 ou 4): '))
    #
    while voto not in candidatos:
        print("Candidato não existente")
        voto = int(input('Em qual candidato você deseja votar? (1, 2, 3 ou 4): '))
    candidatos[voto] += 1

print('\n Resultado da votação\n')
for a in range(1,5):
    print(f'votos do candidato {a}: {candidatos[a]} votos')

total = max(candidatos[c] for c in range(1,5))
empate = [i for i in range(1,5) if candidatos[i]==total]

while len(empate) > 1:
    print(f' houve empate entre os candidatos', *empate ,'\n Para desempate, haverá mmais uma votação entre os candidatos empatados')
    
    votacao2 = {c: 0 for c in range(1,5) if c in empate}
    
    for _ in range(1,11):
        voto2 = int(input(f'Em qual candidato você deseja votar? {', '.join(map(str,empate))}: '))
        while voto2 not in votacao2:
            voto2 = int(input(f'Em qual candidato você deseja votar? {', '.join(map(str,empate))} '))
        votacao2[voto2] += 1
    print('\n Resultado da votação\n')

    for v in range(len(empate)):
        print(f'votos do candidato {empate[v]}: {votacao2[empate[v]]} votos')
    total = max(votacao2.values())
    empate = [c for c in votacao2 if votacao2[c]==total]
print(f'O vencedor é o candidato {empate[0]}')
            