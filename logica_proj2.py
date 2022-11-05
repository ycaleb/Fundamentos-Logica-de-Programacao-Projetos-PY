# LOGICA DE PROGRAMAÇÃO (PYTHON)#
# ------------------------------------------------------------#
## ---PROJETO 2--- ##

# >>PROGRAMA QUE PERMITE AO USUARIO CHUTAR UM NUMERO ATÉ ACERTAR VALOR ALEATORIO GERADO NO INICIO<< #

'''
PSEUDOCODIGO

input valor de 1 a 10
input chute
if chute > valor
print "chute maior que o valor gerado"
if chute < valor
print "chute menor que o valor gerado"
if chute = valor
print "Voce acertou"
'''
# biblioteca random para gerar valor aleatorio
import random

valor = random.randint(1, 10)
# laço de repetição para nao encerrar programa antes de acertar
acertou = False
while acertou == False:
    chute = int(input('Chute um valor de 1 a 10 \n'))
    if chute > valor:
        print('Chutou maior que valor gerado \n')
    elif chute < valor:
        print('Chutou menor que valor gerado \n')
    elif chute == valor:
        acertou = True
        print('Você acertou!')
