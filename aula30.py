'''
CONSTANTE = 'Variáveis' que não vão mudar
muitas condições no mesmo if(ruim)
    <- Contagem de complexidade (ruim)
'''

velocidade = 65 #velocidade atual do carro
local_carro = 90 #local em que o carro está na estrada

RADAR_1 = 60 # velovidade máxima de radar 1
LOCAL_1 = 100 #local onde o radar 1 está
RADAR_RANGE = 1 #A distância onde o radar pega

velocidade_carro_passa_radar = velocidade > RADAR_1
carro_passou_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar1 and velocidade_carro_passa_radar

if velocidade_carro_passa_radar:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar1:
    print('Carro multado em radar 1')

if carro_multado_radar_1:
    print('carro multado em radar 1')