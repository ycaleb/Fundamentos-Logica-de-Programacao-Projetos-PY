# LOGICA DE PROGRAMAÇÃO (PYTHON)#
# ------------------------------------------------------------#
## ---PROJETO 3--- ##

# >>RADAR DE VELOCIDADE SENDO 80KM/H VELOCIDADE MAXIMA<<

'''
input velocidade
velocidade_maxima = 80km
if velocidade <= velocidadee_maxima
print "NAO LEVOU MULTA"
if velocidade > velocidade maxxima e velocidadee <= velocidade_maxima +10
print "MULTA LEVE"
if velocidade > velocidade maxima +11 e velocidade <- velocidade_maxxima +20
print "MULTA GRAVE
if velocidade > velocidade_maxima +20
print "MULTA GRAVISSIMA:
'''

velocidade = int(input("Digite sua velocidade\n"))
velocidade_max = 80
if velocidade <= velocidade_max:
    print('Não levou multa')
elif velocidade > velocidade_max and velocidade <= velocidade_max + 10:
    print('Multa leve aplicada')
elif velocidade > velocidade_max + 111 and velocidade <= velocidade_max + 20:
    print('Multa grave aplicada')
elif velocidade > velocidade_max + 20:
    print('Multa gravíssima aplicada')
