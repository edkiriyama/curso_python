# nome = 'Edgard'
# print(nome[2])
# print(nome[-2])
# print('edy' in nome)
# print('edy' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')