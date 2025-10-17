'''
Iterando strings com while

Resultado Final
*E*d*g*a*r*d*
'''

nome = 'Edgard'
tamanho_nome = len(nome)

print(f'O nome digitado foi: {nome}')
print(f'Tamanho do nome: {tamanho_nome}')


indice = 0
novo_nome = ''
while indice < tamanho_nome:
    letra = nome[indice]
    novo_nome += letra
    indice +=1

print(novo_nome)
       
