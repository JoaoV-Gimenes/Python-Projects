combustivel = input('Qual combustível você deseja usar? (E/D): ').lower() #solicita o combustível desejado

#lista de preços e descontos
preco = {
    'e' : {'preco':1.7 , 'desconto_ate_15': 0.02, 'desconto_acima_15': 0.04},
    'd' : {'preco':2 , 'desconto_ate_15': 0.03, 'desconto_acima_15': 0.05}
}

#confirma se o combustível pedido é válido
if combustivel in preco:
    #pergunta a quantidade de litros do combustível
    volume = int(input('Quantos litros?: '))
    #liga o combustível digitado com o seu preço/L
    valor = preco[combustivel]['preco']
    #aplica o desconto dependendo da quantidade de combustível
    if volume <= 15:
        desconto = preco[combustivel]['desconto_ate_15']
    else:
        desconto = preco[combustivel]['desconto_acima_15']
    
    #calcular o valor final com desconto
    valor_final = (volume * valor) * (1-desconto)
    print(f'valor a pagar: {valor_final}')

else:
    print('combustivel inválido')
