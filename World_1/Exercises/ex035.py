print('\033[32m-='*20)
print('\033[1;40mAnalisador de Triangulos\033[m')
print('\033[32m-=\033[m'*20)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triangulo !!')
else:
    print('Os segmentos acima NAO PODEM FORMAR um triangulo !!!')