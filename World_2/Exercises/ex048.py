soma = 0
cont = 0
cont_impar = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
    cont_impar +=1
print('Existem {} valores solicitados IMPARES, porem existe apenas {} diviziveis por 3 que somados sao {}'.format(cont_impar, cont, soma))