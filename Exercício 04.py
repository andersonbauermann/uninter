# Exercício 4

# Início das variáveis
lista_funcionarios = []
id_func = 0
# Fim das variáveis

# Início de cadastros funcionários
def cadastro_func(id):
    print('-----Menu de cadastro de funcionários-----')
    print('O ID do funcionário é: {}' .format(id))
    nome = input('Nome do funcionário:')
    setor = input('Setor do funcionário:')
    salario = float(input('Salário do funcionário:'))
    dicionario_func = {'id': id, 'nome': nome, 'setor': setor, 'salario': salario}
    lista_funcionarios.append(dicionario_func.copy())
# Fim cadastros funcionários

# Início de consulta de funcionários
def consulta_func():
    print('-----Menu de consulta de funcionários-----')
    while True:
        menu_consulta = input('Escolha a opção desejada: \n' +
                              '1 - Consultar todos os funcionários \n' +
                              '2 - Consultar funcionário por ID \n' +
                              '3 - Consultar funcionário por setor \n' +
                              '4 - Return \n' +
                              '>>>')
        if menu_consulta == '1':
            print('Você selecionou a opção 1 - Consultar todos os funcionários')
            for func in lista_funcionarios:
                print('--------------------------------------------')
                for key, value in func.items():  # procura todos os funcionários no dicionário func
                    print('{}: {}' .format(key, value))
        elif menu_consulta == '2':
            print('Você selecionou a opção 2 - Consultar funcionário por ID')
            id_desejado = int(input('Informe o ID do funcionário: '))
            for func in lista_funcionarios:
                if func['id'] == id_desejado:
                    print('--------------------------------------------')
                    for key, value in func.items():
                        print('{}: {}'.format(key, value))
        elif menu_consulta == '3':
            print('Você selecionou a opção 3 - Consultar funcionário por setor')
            setor_desejado = input('Informe o setor do funcionário: ')
            for func in lista_funcionarios:
                if func['setor'] == setor_desejado:
                    print('--------------------------------------------')
                    for key, value in func.items():
                        print('{}: {}'.format(key, value))
        elif menu_consulta == '4':
            return # Retorna para o main
        else:
            print('Opção inválida, tente novamente.')
            continue
# Fim consulta de funcionários

# Início de remoção de funcionários
def remover_func():
    print('-----Menu de remoção de funcionários-----')
    remover = int(input('Informe o ID do funcionário que deseja remover: '))
    for func in lista_funcionarios:
        if func['id'] == remover:
            lista_funcionarios.remove(func)
            print('Funcionário removido.')
# Fim remoção de funcionários

# Início Main

print('Bem-vindo ao Controle de Funcionários do Anderson Bauermann Feltes')
while True:
    menu_principal = input('Escolha a opção desejada: \n' +
                           '1 - Cadastrar funcionário \n' +
                           '2 - Consultar funcionário \n' +
                           '3 - Remover funcionário \n' +
                           '4 - Sair \n' +
                           '>>>')
    if menu_principal == '1':
        id_func += 1
        cadastro_func(id_func)
    elif menu_principal == '2':
        consulta_func()
    elif menu_principal == '3':
        remover_func()
    elif menu_principal == '4':
        break
    else:
        print('Opção inválida, tente novamente.')
        continue

# Fim Main