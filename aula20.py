primeiro_valor = input('Digite um valor:')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'primeiro_valor={primeiro_valor} é maior do que o segundo_valor={segundo_valor}')
elif primeiro_valor < segundo_valor:
    print(f'segundo_valor={segundo_valor} é maior do que o primeiro_valor={primeiro_valor}')
else:
    print('Os dois valores são iguais')