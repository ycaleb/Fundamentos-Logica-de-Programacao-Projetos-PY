# LOGICA DE PROGRAMAÇÃO (PYTHON)#
# ------------------------------------------------------------#
## ---PROJETO 1--- ##

# >> CRIAR UM PROGRAMA QUE RECEBE UM NUMERO E IMPRIME SEU FATORIAL<< #

'''
Pseudocódigo:

input numero
if numero > 0
if numero = inteiro
fatorial = 1
loop de 1 ate numero
fatorial = fatorial * numero
print (fatorial)
'''

numero = int(input('Digite um numero: '))
if numero > 0:
    # as multiplicações iniciam em 1
    fatorial = 1
    # usa-se +1 pois range não conta o ultimo numero, assim será contado
    for item in range(1, numero + 1):
        fatorial = fatorial*item
    print(fatorial)
