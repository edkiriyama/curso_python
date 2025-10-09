'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreve "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"
'''

nome = input('Digite seu Nome:')

if nome.isnumeric():
    print('Erro: Digite apenas texto, não números')
else:
    tamanho_nome = len(nome)
    if tamanho_nome >= 1 and tamanho_nome < 5:
        print('Seu nome é curto')
    elif tamanho_nome > 6:
        print('Seu nome é muito Grande')
    else:
        print('Seu nome é normal')