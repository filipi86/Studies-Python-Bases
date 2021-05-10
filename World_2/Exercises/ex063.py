print('-' * 45)
print('Sequencia de Fibinacci')
print('-' * 45)
n = int(input('Quantos termos voce quer mostrar? '))
t1 = 0
t2 = 1
print('=' * 45)
print('{} --> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' --> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont +=1
print(' --> ACABOU')
print('=' * 45)