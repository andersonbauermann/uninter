# Cardário para escolha do cliente
print('Bem-vindo a sorveteria do Anderson Bauermann Feltes')
print('----------------------------------------------Cardápio------------------------------------------------')
print('| Código | Descrição             |  Tamanho P (500ml)  |  Tamanho M (1000ml)  |  Tamanho G (2000ml)  |')
print('|   TR   | Sabores Tradicionais  |        R$6,00       |       R$10,00        |       R$18,00        |')
print('|   ES   | Sabores Especiais     |        R$7,00       |       R$12,00        |       R$21,00        |')
print('|   PR   | Sabores Premium       |        R$8,00       |       R$14,00        |       R$24,00        |')
print('------------------------------------------------------------------------------------------------------')
print()
subtotal = 0  # Variável valor total recebe o valor 0 inicialmente
while True:
    cod = input('Informe o sabor do sorvete desejado (TR|ES|PR):')  # Recebe o código do sorvete
    if cod == 'TR':  # Testa as opções válidas de sabor
        tam = input('Qual o tamanho do sorvete que você deseja? (P|M|G)')  # Recebe o tamanho do sorvete desejado
        # Início testes das variáveis de tamanho
        if tam == 'P':  # Teste da opção válida de tamanho
            subtotal += 6  # Variável acumuladora para calculo do valor total
            print('Você pediu um sorvete sabor TRADICIONAL tamanho P no valor de R$6,00.')
            print('---------------------------------------------------------------------------------------------------')
            sair = input('Você deseja fazer mais algum pedido? (S/N)')
            if sair == 'N':
                break  # Quebra o laço de repetição
        elif tam == 'M':  # Teste da opção válida de tamanho
            subtotal += 10  # Variável acumuladora para calculo do valor total
            print('Você pediu um sorvete sabor TRADICIONAL tamanho M no valor de R$10,00.')
            print('---------------------------------------------------------------------------------------------------')
            sair = input('Você deseja fazer mais algum pedido? (S/N)')
            if sair == 'N':
                break  # Quebra o laço de repetição
        elif tam == 'G':
            subtotal += 18  # Variável acumuladora para calculo do valor total
            print('Você pediu um sorvete sabor TRADICIONAL tamanho G no valor de R$18,00.')
            print('---------------------------------------------------------------------------------------------------')
            sair = input('Você deseja fazer mais algum pedido? (S/N)')
            if sair == 'N':
                break  # Quebra o laço de repetição
        else:
            if tam != ('P' or 'M' or 'G'):  # Operador de comparação
                print('-----------------------------------------------------------------------------------------------')
                print('Nós não temos essa opção de tamanho. Selecione uma opção de nosso cardápio.')
                print('-----------------------------------------------------------------------------------------------')
                continue  # Retorna o laço de repetição
    elif cod == 'ES':  # Testa as opções válidas de sabor
        tam = input('Qual o tamanho do sorvete que você deseja? (P|M|G) ')  # Recebe o tamanho do sorvete desejado
        # Início testes das variáveis de tamanho
        if tam == 'P':  # Teste da opção válida de tamanho
            subtotal += 7  # Variável acumuladora para calculo do valor total
            print('Você pediu um sorvete sabor ESPECIAL tamanho P no valor de R$7,00.')
            print('---------------------------------------------------------------------------------------------------')
            sair = input('Você deseja fazer mais algum pedido? (S/N)')
            if sair == 'N':
                break  # Quebra o laço de repetição
        elif tam == 'M':  # Teste da opção válida de tamanho
            subtotal += 12  # Variável acumuladora para calculo do valor total
            print('Você pediu um sorvete sabor ESPECIAL tamanho M no valor de R$12,00.')
            print('---------------------------------------------------------------------------------------------------')
            sair = input('Você deseja fazer mais algum pedido? (S/N)')
            if sair == 'N':
                break  # Quebra o laço de repetição
        elif tam == 'G':  # Teste da opção válida de tamanho
            subtotal += 21  # Variável acumuladora para calculo do valor total
            print('Você pediu um sorvete sabor ESPECIAL tamanho G no valor de R$21,00.')
            print('---------------------------------------------------------------------------------------------------')
            sair = input('Você deseja fazer mais algum pedido? (S/N)')
            if sair == 'N':
                break  # Quebra o laço de repetição
        else:
            if tam != ('P' or 'M' or 'G'):  # Operador de comparação
                print('-----------------------------------------------------------------------------------------------')
                print('Nós não temos essa opção de tamanho. Selecione uma opção de nosso cardápio.')
                print('-----------------------------------------------------------------------------------------------')
                continue  # Retorna o laço de repetição
    elif cod == 'PR':  # Testa as opções válidas de sabor
        tam = input('Qual o tamanho do sorvete que você deseja? (P|M|G) ')  # Recebe o tamanho do sorvete desejado
        # Início testes das variáveis de tamanho
        if tam == 'P':  # Teste da opção válida de tamanho
            subtotal += 8  # Variável acumuladora para calculo do valor total
            print('Você pediu um sorvete sabor PREMIUM tamanho P no valor de R$8,00.')
            print('---------------------------------------------------------------------------------------------------')
            sair = input('Você deseja fazer mais algum pedido? (S/N)')
            if sair == 'N':
                break  # Quebra o laço de repetição
        elif tam == 'M':  # Teste da opção válida de tamanho
            subtotal += 14  # Variável acumuladora para calculo do valor total
            print('Você pediu um sorvete sabor PREMIUM tamanho M no valor de R$14,00.')
            print('---------------------------------------------------------------------------------------------------')
            sair = input('Você deseja fazer mais algum pedido? (S/N)')
            if sair == 'N':
                break  # Quebra o laço de repetição
        elif tam == 'G':  # Teste da opção válida de tamanho
            subtotal += 24  # Variável acumuladora para calculo do valor total
            print('Você pediu um sorvete sabor PREMIUM tamanho G no valor de R$24,00.')
            print('---------------------------------------------------------------------------------------------------')
            sair = input('Você deseja fazer mais algum pedido? (S/N)')
            if sair == 'N':
                break  # Quebra o laço de repetição
        else:
            if tam != ('P' or 'M' or 'G'):  # Operador de comparação
                print('-----------------------------------------------------------------------------------------------')
                print('Nós não temos essa opção de tamanho. Selecione uma opção de nosso cardápio.')
                print('-----------------------------------------------------------------------------------------------')
                continue  # Retorna o laço de repetição
    else:
        if cod != ('TR' or 'ES' or 'PR'):  # Operador de comparação
            print('---------------------------------------------------------------------------------------------------')
            print('Nós não temos esse sabor. Selecione um sabor de nosso cardápio.')
            print('---------------------------------------------------------------------------------------------------')
            continue  # Retorna o laço de repetição
print('O valor total do pedido é de R$ {:.2f}.'.format(subtotal))  # Saída dos dados após o laço de repetição ser quebrado
