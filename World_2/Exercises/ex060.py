'''from math import factorial
n = int(input('Digite um numero para calcular seu Factorial: '))
f = factorial(n)
print('O factorial de {} Eh {}!!!!.'.format(n, f))'''
from time import sleep
n = int(input('Digite um numero para Calcular o Factorial: '))
c = n
f = 1
print('Calculando {} !!! = ...'.format(n), end='')
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('Validando....')
sleep(2)
print('Total eh = {} !!!'.format(f))
#print('O factoria de {} eh {} !!!!.'.format(n, f))

