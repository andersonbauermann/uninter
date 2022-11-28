# Aluno: Anderson Bauermann Feltes | RU: 3920734
# Exercício 3 da atividade prática

# Início da função metragem_limpeza
def metragem_limpeza():
    while True:
        try:
            print('----------------------------- Menu 1 de 3 - Metragem de limpeza -------------------------------')
            metragem = int(input('Qual a metragem do estabelicimento a ser limpo (m²)? '))
            if (metragem >= 30) and (metragem < 300):
                return 60 + (0.3 * metragem)
            elif (metragem >= 300) and (metragem < 700):
                return 120 + (0.5 * metragem)
            else:
                print('Somente aceitamos estabelecimentos com metragem de 30m² a 699m². Entre com um valor válido!')
                continue
        except ValueError: # Tratamento do erro caso o usuário entre com uma variável string ou um float
            print('Somente são aceitos valores inteiros de metragem.')
# Fim da função metragem_limpeza

# Início da função tipo_limpeza
def tipo_limpeza():
    while True:
        print('------------------------------- Menu 2 de 3 - Tipo de Limpeza ---------------------------------')
        tipo_limp = input('Qual o tipo de limpeza que você deseja? \n ' +
                          'B - Básica: Indicada para sujeiras semanais ou quinzenais. \n ' +
                          'C - Completa: Indicada para sujeiras antigas e/ou não rotineiras. \n' +
                          '>>')
        tipo_limp = tipo_limp.upper()
        if tipo_limp == 'B':
            print('Você selecionou a limpeza BÁSICA.')
            return 1.00
        elif tipo_limp == 'C':
            print('Você selecionou a limpeza COMPLETA.')
            return 1.30
        else:
            print('Você informou uma opção que não temos, entre com B para limpezas básicas e C para limpeza completas.')
            continue
# Fim da função tipo_limpeza

# Início da função adicional_limpeza
def adicional_limpeza():
    print('---------------------------- Menu 3 de 3 - Adicional de limpeza -------------------------------')
    acumulador = 0
    while True:
        adicionais = input('Deseja mais algum serviço extra? \n' +
                           '0 - Não deseja nada mais. | Encerrar. \n' +
                           '1 - Passar 10 peças de roupas | R$10,00 \n' +
                           '2 - Limpeza de um forno/forno de micro-ondas | R$ 12,00 \n' +
                           '3 - Limpeza de uma geladeira/freezer | R$ 20,00 \n' +
                           '>>')
        if adicionais == '0':
            return acumulador
        elif adicionais =='1':
            print('Você selecionou a opção 1. (Passar 10 peças de roupa)')
            acumulador += 10
            continue
        elif adicionais =='2':
            print('Você selecionou a opção 2. (Limpeza de um forno/forno de micro-ondas)')
            acumulador += 12
            continue
        elif adicionais =='3':
            print('Você selecionou a opção 3. (Limpeza de uma geladeira/freezer)')
            acumulador += 20
            continue
# Fim da função adicional_limpeza

# Início programa principal

print('Bem-vindo ao programa de Serviços de Limpeza do Anderson Bauermann Feltes.')
print('***********************************************************************************************')
valor_metragem = metragem_limpeza() # Recebe o valor da função
multiplicador = tipo_limpeza() # Recebe o valor da função
adicionais = adicional_limpeza() # Recebe o valor da função
valor_total = (valor_metragem * multiplicador) + adicionais # Calcula o valor total
print('O valor total da limpeza é de R${:.2f} (metragem: R${:.2f} * tipo: {} + adicional: R${:.2f}).' .format(valor_total, valor_metragem, multiplicador, adicionais))

# Fim do programa principal



