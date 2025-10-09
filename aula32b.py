'''
Faça um programa que pergunte a hora ao usuário e , baseando-se no horário
descrito, exiba a saudação aproximada.
Ex: Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23
'''

horario = input('Que horas são (Digite somente as horas): ')

try:
    horario_int = int(horario)
    if horario_int >=0 and horario_int <12:
        print('Bom dia')
    elif horario_int >=12 and horario_int <18:
        print('Boa tarde')
    else:
        print('Boa noite')

except:
    print('Digite o horário corretamente (somente as horas)')