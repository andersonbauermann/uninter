# ---------Calculadora de custo final do produto mais frete-------------


print('Bem-vindo a loja do Anderson Bauermann Feltes')
# Início entrada dos dados
valor = float(input('Entre com o valor do produto:')) # Recebe o valor unitário de cada produto
quantidade = int(input('Entre com a quantidade de itens:')) # Recebe a quantidade de produtos
# Fim entrada dos dados

# Início saída dos dados
vt = valor * quantidade
if quantidade >= 0 and quantidade < 11: #Processa pedidos de 0 a 10 un
    print('O valor sem frete é de: R$ {}' .format(vt))
    print('O valor total com frete é de: R$ {} (Frete total de R$ {})' .format((vt + 30.00), 30.00))
elif quantidade >=11 and quantidade < 101: #Processa pedidos de 11 a 100 un
    print('O valor sem frete é de: R$ {}' .format(vt))
    print('O valor total com frete é de: R$ {} (Frete total de R$ {})' .format((vt + 60.00), 60.00))
elif quantidade >= 101 and quantidade < 1001: #Processa pedidos de 101 até 1000 un
    print('O valor sem frete é de: R$ {}'.format(vt))
    print('O valor total com frete é de: R$ {} (Frete total de R$ {})'.format((vt + 120.00), 120.00))
else:
    print('O valor sem frete é de: R$ {}'.format(vt)) #Processa acima de 1001 un
    print('O valor total com frete é de: R$ {} (Frete total de R$ {})'.format((vt + 240.00), 240.00))
# Fim saída dos dados
