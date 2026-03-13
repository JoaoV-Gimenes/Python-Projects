combustivel = input('Qual combustível você deseja usar? (E/D): ').lower()

preco = {
    'e' : {'preco':1.7 , 'desconto_ate_15': 0.02, 'desconto_acima_15': 0.04},
    'd' : {'preco':2 , 'desconto_ate_15': 0.03, 'desconto_acima_15': 0.05}
}

if combustivel in preco:
    volume = int(input('Quantos litros?: '))
    valor = preco[combustivel]['preco']
    if volume <= 15:
        desconto = preco[combustivel]['desconto_ate_15']
    else:
        desconto = preco[combustivel]['desconto_acima_15']
    
    valor1 = volume * valor
    valor2 = valor1 * (1-desconto)
    print(f'valor a pagar: {valor2}')

else:
    print('combustivel inválido')
