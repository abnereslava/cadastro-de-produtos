from time import sleep
positivo = ['s', 'sim', 'yes', 'y']
negativo = ['n', 'não', 'nao', 'no']
continuar = True
continuar2 = True

produtos = []
valores = []

while continuar == True:
    nome = str(input('\nInsira o nome de um novo produto: '))
    if nome.isnumeric() or nome.isspace():
        print('Nome inválido. Reiniciando cadastro do produto.')
        sleep(1)
        continue
    valor = input('Insira o preço do produto (centavos separados por ponto): ')
    try:
        valor = float(valor)
    except:
        print('Valor inválido. Reiniciando cadastro do produto.')
        continue
    produtos.append(nome)
    valores.append(valor)
    while continuar2 == True:
        resposta = input('Gostaria de continuar? [s/n]: ').lower()
        if resposta in positivo:
            break
        if resposta in negativo:
            continuar = False
            break
        else:
            continue

print('')
sleep(0.5)
print('-' * 40)
sleep(0.5)
print(f'{"LISTA DE PRODUTOS":^40}')
sleep(0.5)
print('-' * 40)
sleep(0.5)
print('')
sleep(0.5)

for i, j in zip(produtos, valores):
    print(f'{i:.<40}', end='')
    print(f'R$ ', end='')
    print(f'{j:.2f}')
    sleep(0.5)
